---
layout: page
title: Stats
permalink: /stats/
subject: stats
---

<ul class="post-list">
{% for post in site.categories.stats %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>
