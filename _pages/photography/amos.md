---
author: photography
author_profile: true

layout: archive
title: "Concrete Formwork in Tel-Aviv"
permalink: /photography/amos/
# author_profile: false
---

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/amos/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
