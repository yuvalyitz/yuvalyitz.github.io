---
title: "Temporal Unit Interval Independent Sets"
collection: publications
category: conferences
permalink: /publication/temporal-is
excerpt: "We study the complexity of finding large independent sets in temporal unit interval graphs, and obtain hardness, constant-factor approximation, and fixed-parameter tractability results."
date: 2022-03-14
venue: "1st Symposium on Algorithmic Foundations of Dynamic Networks (SAND 2022)"
paperurl: "https://doi.org/10.4230/LIPIcs.SAND.2022.19"
bibtexurl: "https://yuvalyitz.github.io/files/hermelin2022temporal.bib"
slidesurl: '/files/SAND2022_slides.pdf'
citation: "Danny Hermelin, Yuval Itzhaki, Hendrik Molter, and Rolf Niedermeier. Temporal Unit Interval Independent Sets. In 1st Symposium on Algorithmic Foundations of Dynamic Networks (SAND 2022). Leibniz International Proceedings in Informatics (LIPIcs), Volume 221, pp. 19:1-19:16, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2022) "
---

Temporal graphs have been recently introduced to model changes to a given network that occur throughout a fixed period of time. We introduce and investigate the Temporal Δ Independent Set problem, a temporal variant of the well known Independent Set problem. This problem is e.g. motivated in the context of finding conflict-free schedules for maximum subsets of tasks, that have certain (changing) constraints on each day they need to be performed. We are specifically interested in the case where each task needs to be performed in a certain time-interval on each day and two tasks are in conflict on a day if their time-intervals overlap on that day. This leads us to considering Temporal Δ Independent Set on the restricted class of temporal unit interval graphs, i.e., temporal graphs where each layer is unit interval. 
We present several hardness results for this problem, as well as two algorithms: The first is a constant-factor approximation algorithm for instances where τ, the total number of time steps (layers) of the temporal graph, and Δ, a parameter that allows us to model some tolerance in the conflicts, are constants. For the second result we use the notion of order preservation for temporal unit interval graphs that, informally, requires the intervals of every layer to obey a common ordering. We provide an FPT algorithm parameterized by the size of minimum vertex deletion set to order preservation.

---

[View paper on Dagstuhl LIPIcs](https://doi.org/10.4230/LIPIcs.SAND.2022.19)  
[Download BibTeX](https://yuvalyitz.github.io/files/hermelin2022temporal.bib)
