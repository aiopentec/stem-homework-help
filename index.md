---
layout: default
title: Home
---

<div class="subject-grid">
  <a class="subject-card subject-math" href="{{ '/math/' | relative_url }}">
    <h2>Math</h2>
    <p>{{ site.categories.math | size }} solved problems</p>
  </a>
  <a class="subject-card subject-physics" href="{{ '/physics/' | relative_url }}">
    <h2>Physics</h2>
    <p>{{ site.categories.physics | size }} solved problems</p>
  </a>
  <a class="subject-card subject-chemistry" href="{{ '/chemistry/' | relative_url }}">
    <h2>Chemistry</h2>
    <p>{{ site.categories.chemistry | size }} solved problems</p>
  </a>
  <a class="subject-card subject-stats" href="{{ '/stats/' | relative_url }}">
    <h2>Statistics</h2>
    <p>{{ site.categories.stats | size }} solved problems</p>
  </a>
</div>

## Latest Solved Problems

<ul class="post-list">
{% for post in site.posts limit: 15 %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }} <span class="tag tag-{{ post.category }}">{{ post.category }}</span></span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>
