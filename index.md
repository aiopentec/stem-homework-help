---
layout: default
title: Home
---

# Latest Solved Problems

{% for post in site.posts %}
- **[{{ post.title }}]({{ post.url }})** <small>{{ post.date | date: "%b %-d, %Y" }} — {{ post.category }}</small>
{% endfor %}
