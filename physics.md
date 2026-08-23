---
layout: page
title: Physics
permalink: /physics/
---

<ul class="post-list">
{% for post in site.categories.physics %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>
