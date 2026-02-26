---
title: "Just-in-Time Scheduling in Two-Stage Flexible Flow Shops"
collection: publications
category: manuscripts
permalink: /publication/jit-two-stage-flexible-flowshop
excerpt: 'We study the two-stage flexible flow shop problem with a just-in-time objective, proving strong NP-hardness for the unweighted case and developing pseudo-polynomial, parameterized, and approximation algorithms for several structural settings.'
date: 2026-02-15
slidesurl: '/files/jit2026flowshop.pdf'
bibtexurl: 'https://yuvalyitz.github.io/files/heeger2026flowshop.bib'
venue: 'European Journal of Operational Research (EJOR), In Press.'
paperurl: 'https://doi.org/10.1016/j.ejor.2026.02.017'
citation: 'Heeger, K., Hermelin, D., Itzhaki, Y., Schieber, B., and Shabtay, D. (2026). Just-in-Time Scheduling in Two-Stage Flexible Flow Shops. European Journal of Operational Research.'
---
We study the problem of **Just-in-Time (JIT) scheduling** in a **two-stage flexible flow shop**, denoted  

$$
FF(1,m)\,||\,\sum w_j Z_j.
$$

In this setting, each job must first undergo preprocessing on a **single machine** and is then processed on one of **m identical parallel machines**. A job contributes to the objective only if it completes **exactly at its due date**.

Our goal is to maximize the total weight of just-in-time jobs.

---

### Main results

- We prove that the **unweighted problem is strongly NP-hard**, via a reduction from *Hitting Set*.  
- The reduction also implies **W[2]-hardness with respect to the number of machines** $$m$$.

---

### Positive algorithmic results

We complement these hardness results with several tractability results:

- A **pseudo-polynomial dynamic program** for fixed number of machines $m$.
- A **pseudo-polynomial dynamic program** for bounded maximum clique.
- A **pseudo-polynomial dynamic program** for second-stage processing times.
- Polynomial-time algorithms for special cases, including:
  - **Uniform preprocessing times**, and
  - Proper interval instances.
- A **Fully Polynomial-Time Approximation Scheme (FPTAS)** when key structural parameters are bounded.

---

Overall, the paper provides a systematic complexity and algorithmic study of JIT scheduling in two-stage flexible flow shops, identifying both computational barriers and tractable regimes.
