---
title: "Temporal interval cliques and independent sets"
collection: publications
category: manuscripts
permalink: /publication/temporal-is-clique
date: 2023-06-15
excerpt: 'We give hardness, approximation, and parameterized results for Temporal Clique and Temporal Independent Set on temporal interval graphs.'
venue: 'Theoretical Computer Science, Volume 961, p.113885.'
paperurl: 'https://doi.org/10.1016/j.tcs.2023.113885'
bibtexurl: 'https://yuvalyitz.github.io/files/hermelin2022temporal.bib'
citation: 'Hermelin, D., Itzhaki, Y., Molter, H. and Niedermeier, R., 2023. Temporal interval cliques and independent sets. Theoretical Computer Science, 961, p.113885.'
---
Temporal graphs have been recently introduced to model changes in a given network that occur throughout a fixed period of time. The Temporal Δ Clique problem, which generalizes the well known Clique problem to temporal graphs, has been studied in the context of finding nodes of interest in dynamic networks [TCS '16]. We introduce the Temporal Δ Independent Set problem, a temporal generalization of Independent Set. This problem is e.g. motivated in the context of finding conflict-free schedules for maximum subsets of tasks, that have certain (time-varying) constraints within a given time period. We are specifically interested in the case where each task needs to be performed in a certain time-interval on each day and two tasks are in conflict on a certain day if their time-intervals on that day overlap. This leads us to consider both problems on the restricted class of temporal unit interval graphs, i.e., temporal graphs where each layer is a unit interval graph.
We present several hardness results as well as positive results. On the algorithmic side, we provide constant-factor approximation algorithms for instances of both problems where τ, the total number of time steps (layers) of the temporal graph, and Δ, a parameter that allows us to model conflict tolerance, are constants. We develop an exact FPT algorithm for Temporal Δ Clique with respect to parameter
. Finally, we use the notion of order preservation for temporal unit interval graphs that, informally, requires the intervals of every layer to obey a common ordering. For both problems, we provide an FPT algorithm parameterized by the size of minimum vertex deletion set to order preservation.
