---
layout: page
title: Stats
permalink: /stats/
subject: stats
---

<ul class="post-list">
{% for post in site.categories.stats %}
  <li{% if forloop.index > 20 %} class="hidden-post"{% endif %}>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>

{% if site.categories.stats.size > 20 %}
  <button class="load-more-btn" type="button">Load more problems</button>
{% endif %}
