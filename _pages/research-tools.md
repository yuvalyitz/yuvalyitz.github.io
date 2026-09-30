---
layout: single
title: "Research Tools"
permalink: /research-tools/
author_profile: true
redirect_from:
  - /portfolio/
---

<style>
  .tool-card { display: flex; flex-wrap: wrap; gap: 1.25em; margin: 1.5em 0 2.5em; padding-bottom: 2em; border-bottom: 1px solid var(--global-border-color); }
  .tool-card:last-of-type { border-bottom: none; }
  .tool-card__img { flex: 1 1 280px; max-width: 360px; }
  .tool-card__img img { border: 1px solid var(--global-border-color); border-radius: 6px; }
  .tool-card__body { flex: 2 1 300px; }
  .tool-card__body h2 { margin-top: 0; }
</style>

Tools I develop for exploring scheduling problems and research literature.

<div class="tool-card">
  <div class="tool-card__img">
    <a href="/scheduling-zoo/"><img src="/images/projects/scheduling-zoo.png" alt="Parameterized Scheduling Zoo screenshot"></a>
  </div>
  <div class="tool-card__body">
    <h2>The Parameterized Scheduling Zoo</h2>
    <p>An interactive browser for scheduling complexity results, built on <a href="https://schedulingzoo.lip6.fr/">The Scheduling Zoo</a>. Explore related problems, follow reductions, and identify open questions.</p>
    <p>
      <a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo" class="btn">Open the Zoo</a>
      <a href="/scheduling-zoo/" class="btn btn--inverse">About</a>
      <a href="https://github.com/yuvalyitz/parameterized-scheduling-zoo" class="btn btn--inverse"><i class="fab fa-github"></i> Code</a>
    </p>
  </div>
</div>
