---
layout: default
title: Home
---

<p class="tagline">Real questions from real students, answered in full — free worked solutions across math, physics, chemistry, and statistics, added every day.</p>

<div class="subject-grid">
  <a class="subject-card subject-math" href="{{ '/math/' | relative_url }}">
    <h2>🧮 Math</h2>
    <p>{{ site.categories.math | size }} solved problems</p>
  </a>
  <a class="subject-card subject-physics" href="{{ '/physics/' | relative_url }}">
    <h2>⚛️ Physics</h2>
    <p>{{ site.categories.physics | size }} solved problems</p>
  </a>
  <a class="subject-card subject-chemistry" href="{{ '/chemistry/' | relative_url }}">
    <h2>🧪 Chemistry</h2>
    <p>{{ site.categories.chemistry | size }} solved problems</p>
  </a>
  <a class="subject-card subject-stats" href="{{ '/stats/' | relative_url }}">
    <h2>📊 Statistics</h2>
    <p>{{ site.categories.stats | size }} solved problems</p>
  </a>
</div>
<section class="stem-search">

  <h1>Find a STEM answer</h1>

  <p>
    Search worked solutions across mathematics,
    physics, chemistry and statistics.
  </p>

  <form
    action="/search/"
    method="get"
  >

    <label for="search">
      Search STEM Answered
    </label>

    <input
      id="search"
      name="q"
      type="search"
      placeholder="What are you trying to solve?"
      autocomplete="off"
    >

    <button type="submit">
      Search
    </button>

  </form>

</section>

## Latest Solved Problems

<ul class="post-list">
{% for post in site.posts limit: 15 %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }} <span class="tag tag-{{ post.category }}">{{ post.category }}</span></span>
    <h3><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>
