---
author: photography
author_profile: true

layout: archive
title: "Concrete Work at Elwood, Melbourne"
permalink: /photography/construction/
# author_profile: false
---
Scenes from concrete and shotcrete construction work.

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/construction/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
