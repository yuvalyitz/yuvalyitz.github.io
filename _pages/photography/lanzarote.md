---
author: photography
author_profile: true

layout: archive
title: "Lanzarote"
permalink: /photography/lanzarote/
# author_profile: false
---

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/lanzarote/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
