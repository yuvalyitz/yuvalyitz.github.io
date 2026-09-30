---
layout: single
title: "The Parameterized Scheduling Zoo"
permalink: /scheduling-zoo/
author_profile: true
---

<a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo">
  <img src="/images/projects/scheduling-zoo.png" alt="Screenshot of the Parameterized Scheduling Zoo problem map" style="border: 1px solid var(--global-border-color); border-radius: 6px;">
</a>

An interactive browser for scheduling complexity results, built on [The Scheduling Zoo](https://schedulingzoo.lip6.fr/). Explore related problems, follow reductions, and identify open questions.

<p>
  <a href="https://yuvalyitz.github.io/parameterized-scheduling-zoo/#/schedulingzoo" class="btn btn--large">Open the Zoo &rarr;</a>
  <a href="https://github.com/yuvalyitz/parameterized-scheduling-zoo" class="btn btn--inverse btn--large"><i class="fab fa-github"></i> Source on GitHub</a>
</p>

### What you can do

- **Browse the Scheduling Zoo.** Filter problems in Graham's three-field notation α \| β \| γ, and follow reductions between them.
- **Design problem maps.** Build your own map of related problems and export it as TikZ.
- **Look up results per parameter.** Explore recorded tractability and hardness results by parameter, with references. Missing entries may reflect gaps in the dataset.
- **Contribute results.** Propose classifications and reductions, then submit them using “Send my classifications”.

<div class="notice--warning" markdown="1">
**Work in progress.** The parameterized results are an early seed dataset and are still being checked. If you find a missing result, a wrong classification, or a better reference, please [email me](mailto:{{ site.author.email }}) or [open an issue](https://github.com/yuvalyitz/parameterized-scheduling-zoo/issues).
</div>

I’m developing the Zoo into a shared reference for scheduling complexity. Contributions of results, references, and corrections are welcome. If you would like to collaborate, [email me](mailto:{{ site.author.email }}).

### Acknowledgements

The overview map is built from The Scheduling Zoo's bibliography and notation files, © Christoph Dürr, used under the MIT License.
