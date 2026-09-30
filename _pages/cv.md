---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /cv-json/
  - /resume-json
  - /resume
---

{% include base_path %}

Appointments
======
* **Postdoctoral researcher**<br>
Technische Universität Hamburg, Institute for Algorithms and Complexity<br>
Working with Prof. Matthias Mnich

Education
======
* **Ph.D. in Industrial Engineering & Management (Algorithms & Operations Research)**<br>
Ben-Gurion University of the Negev, 2022–2026<br>
  Thesis: Scheduling with Intervals<br>
  Advisors: Prof. Danny Hermelin & Prof. Dvir Shabtay<br>

* **M.Sc. in Computer Science**<br>
Technische Universität Berlin, 2020–2021<br>
  Thesis: Exploiting Order to Find Independent-Sets in Temporal Interval Graphs<br>
  Advisors: Prof. Rolf Niedermeier & Prof. Danny Hermelin<br>

* **B.Sc. in Civil Engineering**<br>
Technische Universität Berlin, 2014–2018<br>


Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
