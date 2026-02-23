---
author: photography
author_profile: true

layout: archive
title: "Pointe Helbronner, Mont Blanc"
permalink: /photography/alps/
# author_profile: false
---
<!-- alps -->

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/alps/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
