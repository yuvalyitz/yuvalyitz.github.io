---
title: "Just-in-Time Scheduling in Two-Stage Flexible Flow Shops"
collection: talks
type: "Talk"
permalink: /talks/2025-05-05-orsis-two-stage-flexible-flow-shops/
venue: "Operations Research Society of Israel (ORSIS) Annual Meeting"
date: 2025-05-05
location: "Tel Aviv, Israel"
eventurl: "https://www.orsis.org.il/registration-information-2025"
---

Talk at the [Operations Research Society of Israel (ORSIS) Annual Meeting](https://www.orsis.org.il/registration-information-2025), Tel Aviv, 2025.

## Authors

Klaus Heeger, Danny Hermelin, Yuval Itzhaki, Baruch Schieber, and Dvir Shabtay.

## Abstract

Flow shop is a scheduling model in which a job is deemed completed once it has undergone an ordered sequence of processing stages. In the classical setting each such stage includes a single machine. The two-machine flow shop problem with the objective of maximizing the weighted number of just-in-time (JIT) jobs, jobs that are completed exactly at their due-date, is known to be ordinary NP-hard even when all jobs have unit processing time on the second machine.

We extend the analysis of the aforementioned problem to a two-stage flexible (a.k.a. hybrid) flow-shop setting, where the second stage permits the usage of a set of identical parallel machines. We focus on exact and parameterized complexity classification of the problem, providing both hardness and algorithmic results.

Particularly, we design a pseudo-polynomial time algorithm for the general problem, assuming the number of machines is fixed. In contrast, we show that when the number of machines is arbitrary, the problem becomes hard. We also provide FPT algorithms for the problem with respect to the maximal due date and the treewidth of the corresponding interval graph. Finally, we provide a 2-approximation algorithm for the case of identical processing times on the second stage.
