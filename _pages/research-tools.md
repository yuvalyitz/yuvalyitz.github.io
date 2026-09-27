---
layout: single
title: "Research Tools"
permalink: /research-tools/
author_profile: true
---

<style>
  .tool-card { display: flex; flex-wrap: wrap; gap: 1.25em; margin: 1.5em 0 2.5em; padding-bottom: 2em; border-bottom: 1px solid var(--global-border-color); }
  .tool-card:last-of-type { border-bottom: none; }
  .tool-card__img { flex: 1 1 280px; max-width: 360px; }
  .tool-card__img img { border: 1px solid var(--global-border-color); border-radius: 6px; }
  .tool-card__body { flex: 2 1 300px; }
  .tool-card__body h2 { margin-top: 0; }
  .tool-card__tag { display: inline-block; font-size: 0.7em; padding: 0.1em 0.6em; border-radius: 1em; border: 1px solid var(--global-border-color); color: var(--global-text-color-light); vertical-align: middle; margin-left: 0.4em; }
</style>

Software I build for my own research and share in the hope that it is useful to others.

<div class="tool-card">
  <div class="tool-card__img">
    <a href="/scheduling-zoo/"><img src="/images/projects/scheduling-zoo.png" alt="Parameterized Scheduling Zoo screenshot"></a>
  </div>
  <div class="tool-card__body">
    <h2>The Parameterized Scheduling Zoo</h2>
    <p>A visual browser for <a href="https://schedulingzoo.lip6.fr/">The Scheduling Zoo</a> with the aim to allow researchers to quickly identify open problems and collaboratively build a knowledge base.</p>
    <p>
      <a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo" class="btn">Open the Zoo</a>
      <a href="/scheduling-zoo/" class="btn btn--inverse">About</a>
      <a href="https://github.com/yuvalyitz/parameterized-scheduling-zoo" class="btn btn--inverse"><i class="fab fa-github"></i> Code</a>
    </p>
  </div>
</div>

<div class="tool-card">
  <div class="tool-card__body">
    <h2>Citation Ledger <span class="tool-card__tag">coming soon</span></h2>
    <p>An interactive citation graph built around a seed paper. It shows the papers the seed cites, the papers those cite in turn, and later work that cites the seed, on a timeline or tree layout. I use it for peer review, for tracing older sources, and for building a project bibliography. Data comes from Semantic Scholar.</p>
  </div>
</div>
