---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

About
======

I am a Ph.D. candidate in Algorithms and Operations Research at [Ben-Gurion University of the Negev](https://www.bgu.ac.il/en), advised by Prof. [Danny Hermelin](https://cris.bgu.ac.il/en/persons/dan-hermelin/) and Prof. [Dvir Shabtay](https://cris.bgu.ac.il/en/persons/dvir-shabtay/).

My research focuses on combinatorial optimization, scheduling, interval graphs, and parameterized complexity. I am especially interested in industry-motivated optimization problems, and in understanding the combinatorial structure that makes such problems tractable or hard.

Before my Ph.D., I completed an M.Sc. in Computer Science at [Technische Universität Berlin](https://www.tu.berlin/), advised by Prof. [Rolf Niedermeier](https://www.tu.berlin/akt/ueber-uns/leitung/rolf-niedermeier) and Prof. [Danny Hermelin](https://cris.bgu.ac.il/en/persons/dan-hermelin/). My master's thesis studied temporal interval graphs, continuing a line of work that connects graph algorithms, scheduling, and time-dependent structures.

I also hold a B.Sc. in Civil Engineering from [Technische Universität Berlin](https://www.tu.berlin/) and previously worked as a data scientist in Berlin, developing data-driven tools for construction cost estimation from building models.

<h2>Publications</h2>
{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}


<!-- New style rendering if publication categories are defined -->
{% if site.publication_category %}
  {% for category in site.publication_category  %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
        {% assign title_shown = true %}
      {% endunless %}
      {% include archive-single.html %}
    {% endfor %}
  {% endfor %}
{% else %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %}



