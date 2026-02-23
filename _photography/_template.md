---
layout: single
title: "{{ title }}"
author_profile: false
toc: false
gallery: true
---

<p>{{ description }}</p>

<div id="gallery">
{% for img in images %}
  <a href="{{ img.full }}" data-pswp-width="2000" data-pswp-height="1333">
    <img src="{{ img.thumb }}">
  </a>
{% endfor %}
</div>
