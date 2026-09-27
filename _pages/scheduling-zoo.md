---
layout: single
title: "The Parameterized Scheduling Zoo"
permalink: /scheduling-zoo/
author_profile: true
---

<a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo">
  <img src="/images/projects/scheduling-zoo.png" alt="Screenshot of the Parameterized Scheduling Zoo problem map" style="border: 1px solid var(--global-border-color); border-radius: 6px;">
</a>

A visual browser for [The Scheduling Zoo](https://schedulingzoo.lip6.fr/) with the aim to allow researchers to quickly identify open problems and collaboratively build a knowledge base.

<p>
  <a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo" class="btn btn--large">Open the Zoo &rarr;</a>
  <a href="https://github.com/yuvalyitz/parameterized-scheduling-zoo" class="btn btn--inverse btn--large"><i class="fab fa-github"></i> Source on GitHub</a>
</p>

### What you can do

- **Browse the Scheduling Zoo.** Filter problems in Graham's three-field notation α \| β \| γ, and follow reductions between them.
- **Design problem maps.** Build your own map of related problems and export it as TikZ.
- **Look up results per parameter.** See which parameterizations are known to be tractable, which are hard, and which are still open, with references.
- Change classification and create reductions between problems, and **share your results** (click "Send my classifications").

<div class="notice--warning" markdown="1">
**Work in progress.** The parameterized results are an early seed dataset and are still being checked. If you find a missing result, a wrong classification, or a better reference, please [email me](mailto:{{ site.author.email }}) or [open an issue](https://github.com/yuvalyitz/parameterized-scheduling-zoo/issues).
</div>

It is today more possible than ever[^db-initiatives] to organize our technical results in a structured, robust database that gives researchers a bird's-eye view over the field. If you wish to collaborate, [write me an email](mailto:{{ site.author.email }}).

[^db-initiatives]: Using initiatives like [laxarchive.org](https://laxarchive.org/).

### Acknowledgements

The overview map is built from The Scheduling Zoo's bibliography and notation files, © Christoph Dürr, used under the MIT License.
