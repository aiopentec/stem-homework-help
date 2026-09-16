#!/usr/bin/env python3
"""
gsc_coverage_buckets.py

Pulls every URL from a site's sitemap, checks each one against the Search
Console URL Inspection API, and reports which URLs fall into the
"Discovered - currently not indexed" and "Crawled - currently not indexed"
buckets shown on the Page Indexing report.

Unlike the Page Indexing UI (which only gives you a count), this gives you
the actual URL list per reason, plus a breakdown by URL pattern (e.g. by
subject folder) so you can see whether the stuck pages cluster around
something specific.

Usage:
    python gsc_coverage_buckets.py --site https://stemanswered.com/ \
        --sitemap https://stemanswered.com/sitemap.xml \
        --creds service_account.json

Requires:
    pip install google-auth google-auth-httplib2 google-api-python-client requests

Auth:
    Uses a Google service account JSON key that has been added as a
    "Full" user on the Search Console property (Settings > Users and
    permissions > Add user). Same credential type as gsc_coverage_check.py.

Notes:
    - The URL Inspection API is rate-limited (2,000 queries/day, ~600/min
      per project by default as of last check) so this sleeps briefly
      between calls. For a site this size (~150 URLs) that's fine; if the
      portfolio grows, increase --sleep or shard the run.
    - "Discovered" and "Crawled" bucket definitions come directly from the
      API's indexingState / verdict fields, so this stays accurate even
      if Google renames things in the UI.
"""

import argparse
import sys
import time
from collections import defaultdict
from urllib.parse import urlparse

import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def load_sitemap_urls(sitemap_url):
    """Fetch a sitemap (or sitemap index) and return a flat list of page URLs."""
    resp = requests.get(sitemap_url, timeout=30)
    resp.raise_for_status()
    text = resp.text

    # Cheap XML parsing without extra deps: pull every <loc>...</loc>
    import re
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)

    # If this was a sitemap index (points to other sitemaps), recurse.
    if any(loc.endswith(".xml") for loc in locs) and "sitemap" in sitemap_url:
        all_urls = []
        for loc in locs:
            if loc.endswith(".xml"):
                all_urls.extend(load_sitemap_urls(loc))
            else:
                all_urls.append(loc)
        return all_urls

    return locs


def url_pattern(url):
    """Bucket a URL by its first path segment, for clustering the results."""
    path = urlparse(url).path.strip("/")
    if not path:
        return "(homepage)"
    return path.split("/")[0]


def inspect_url(service, site_url, page_url):
    body = {"inspectionUrl": page_url, "siteUrl": site_url}
    result = service.urlInspection().index().inspect(body=body).execute()
    return result.get("inspectionResult", {})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", required=True, help="Search Console property URL, e.g. https://stemanswered.com/")
    ap.add_argument("--sitemap", required=True, help="Sitemap URL to enumerate pages from")
    ap.add_argument("--creds", default="service_account.json", help="Path to service account JSON key")
    ap.add_argument("--sleep", type=float, default=1.0, help="Seconds to sleep between API calls (default 1.0)")
    ap.add_argument("--limit", type=int, default=None, help="Only check the first N URLs (for a quick test run)")
    args = ap.parse_args()

    print(f"Loading sitemap: {args.sitemap}")
    urls = load_sitemap_urls(args.sitemap)
    print(f"Found {len(urls)} URLs in sitemap.")
    if args.limit:
        urls = urls[: args.limit]
        print(f"Limiting to first {len(urls)} for this run.")

    creds = service_account.Credentials.from_service_account_file(args.creds, scopes=SCOPES)
    service = build("searchconsole", "v1", credentials=creds)

    buckets = defaultdict(list)   # reason -> [urls]
    errors = []

    for i, url in enumerate(urls, 1):
        try:
            result = inspect_url(service, args.site, url)
            idx = result.get("indexStatusResult", {})
            verdict = idx.get("verdict", "UNKNOWN")
            coverage_state = idx.get("coverageState", "UNKNOWN")

            if verdict == "PASS":
                reason = "Indexed"
            else:
                # coverageState text matches the GSC UI's "reason" column,
                # e.g. "Discovered - currently not indexed",
                # "Crawled - currently not indexed", etc.
                reason = coverage_state or verdict

            buckets[reason].append(url)
            print(f"[{i}/{len(urls)}] {reason:40s} {url}")

        except Exception as e:
            errors.append((url, str(e)))
            print(f"[{i}/{len(urls)}] ERROR: {url} -> {e}")

        time.sleep(args.sleep)

    print("\n" + "=" * 70)
    print("SUMMARY BY REASON")
    print("=" * 70)
    for reason, urls_in_bucket in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
        print(f"\n{reason}  ({len(urls_in_bucket)} pages)")
        if reason != "Indexed":
            for u in urls_in_bucket:
                print(f"    {u}")

    print("\n" + "=" * 70)
    print("NOT-INDEXED URLS GROUPED BY PATH PATTERN")
    print("=" * 70)
    not_indexed = [u for r, us in buckets.items() if r != "Indexed" for u in us]
    by_pattern = defaultdict(int)
    for u in not_indexed:
        by_pattern[url_pattern(u)] += 1
    for pattern, count in sorted(by_pattern.items(), key=lambda kv: -kv[1]):
        print(f"  {pattern:30s} {count}")

    if errors:
        print("\n" + "=" * 70)
        print(f"ERRORS ({len(errors)})")
        print("=" * 70)
        for u, e in errors:
            print(f"  {u}: {e}")

    # Write a CSV alongside the console output for easy filtering in Sheets.
    import csv
    with open("gsc_coverage_buckets.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "reason", "path_pattern"])
        for reason, urls_in_bucket in buckets.items():
            for u in urls_in_bucket:
                writer.writerow([u, reason, url_pattern(u)])
    print("\nWrote gsc_coverage_buckets.csv")


if __name__ == "__main__":
    sys.exit(main())
