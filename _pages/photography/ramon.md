---
author: photography
author_profile: true

layout: archive
title: "Mitzpe Ramon, Timna Park"
permalink: /photography/ramon/
# author_profile: false
---

<!-- The Ezra Orion Desert Sculpture Park, Mitzpe Ramon.

Timna Park, Eilat. -->

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/ramon/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
