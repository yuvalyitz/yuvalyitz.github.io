---
layout: archive
title: "Photography"
permalink: /photography/
author: photography
author_profile: true
---

A selection of photographs from travel and construction sites. My background in civil engineering shapes my interest in structures, materials, and industrial spaces.

<div class="photography-index">
{% for album in site.data.albums %}
  <a class="album-block" href="{{ '/photography/' | append: album.slug | append: '/' | relative_url }}">
    <h2 class="album-title">{{ album.title }}</h2>
    <div class="album-thumbs">
    {% for photo in album.images limit:4 %}
      <img src="{{ photo.thumbnail | relative_url }}" alt="{{ photo.alt | escape }}" class="album-thumb" width="{{ photo.width }}" height="{{ photo.height }}" loading="lazy" decoding="async">
    {% endfor %}
    </div>
  </a>
{% endfor %}
</div>
