---
author: photography
author_profile: true

layout: archive
title: "Elma"
permalink: /photography/elma/
# author_profile: false
---

<!-- Elma is a boutique hotel and arts complex in Zichron Ya’akov, housed in the former “Mivtachim” convalescent home designed by Yaakov Rechter - an Israeli architect and Israel Prize laureate (1972). Today, the complex reflects the vision of Lili Elstein, its owner and an art collector, who saved and repurposed the building as a space where hospitality and art actually share the same footprint. The hotel is threaded with a substantial on-site collection - hundreds of works displayed throughout rooms and public spaces - which makes it feel less like “art on the walls” and more like living inside a curated environment. -->

<div id="gallery">
{% for file in site.static_files %}
  {% if file.path contains '/images/photography/elma/' %}
    <a href="{{ file.path }}">
      <img src="{{ file.path }}">
    </a>
  {% endif %}
{% endfor %}
</div>
