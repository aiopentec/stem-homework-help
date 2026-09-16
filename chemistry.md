---
layout: page
title: Chemistry
permalink: /chemistry/
subject: chemistry
---

<ul class="post-list">
{% for post in site.categories.chemistry %}
  <li{% if forloop.index > 20 %} class="hidden-post"{% endif %}>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>

{% if site.categories.chemistry.size > 20 %}
  <button class="load-more-btn" type="button">Load more problems</button>
{% endif %}
