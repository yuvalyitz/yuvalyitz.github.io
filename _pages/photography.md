---
layout: archive
title: "Photography"
permalink: /photography/
author: photography
author_profile: true
---

{% include base_path %}

This portfolio contains a small selection of my photography projects. I practice photography as a hobby, and my early background in civil engineering exposed me to construction sites and industrial spaces that aren’t usually treated as visual subjects. The appeal is both visual and technical, and the habit stayed with me through travel.

{% assign albums = "construction,alps,elma,ramon,rajasthan,amos,lanzarote,nz,fiji,berlin" | split: "," %}

{% assign album_titles =
  "construction:Concrete Work at Elwood, Melbourne,
   alps:Pointe Helbronner, Mont Blanc,
   elma:Elma,
   ramon:Mitzpe Ramon, Timna Park,
   rajasthan:Rajasthan,
   amos:Concrete Formwork in Tel-Aviv,
   lanzarote:Lanzarote,
   nz:New Zealand,
   fiji:Fiji,
   berlin:Berlin"
  | split: "," %}

<div class="photography-index">
{% for album in albums %}

  {% assign title = album %}
  {% for pair in album_titles %}
    {% assign kv = pair | split: ":" %}
    {% assign key = kv[0] | strip %}
    {% assign val = kv[1] | strip %}
    {% if key == album %}
      {% assign title = val %}
    {% endif %}
  {% endfor %}


  <a class="album-block" href="/photography/{{ album | downcase }}/">
    <h3 class="album-title">{{ title }}</h3>

    <div class="album-thumbs">
      {% assign exts = ".jpg,.jpeg,.png,.webp" | split: "," %}
      {% assign album_path = "images/photography/" | append: album | append: "/" %}
      {% assign count = 0 %}

      {% for file in site.static_files %}
        {% if file.path contains album_path %}
          {% assign ext = file.extname | downcase %}
          {% if exts contains ext %}
            <img src="{{ file.path | relative_url }}" class="album-thumb" loading="lazy">
            {% assign count = count | plus: 1 %}
          {% endif %}
        {% endif %}
        {% if count == 4 %}
          {% break %}
        {% endif %}
      {% endfor %}
    </div>
  </a>

{% endfor %}
</div>





