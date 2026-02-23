---
title: "Fair Repetitive Interval Scheduling"
collection: publications
category: manuscripts 
permalink: /publication/fair-repetitive-jit
excerpt: 'We study fair repetitive interval scheduling, showing NP-hardness under natural restrictions and providing algorithmic and parameterized results for several tractable cases.'
date: 2025-05-26
venue: 'Algorithmica, Volume 87, pages 1340–1368'
slidesurl: '/files/Fair2024_slides.pdf'
paperurl: 'https://doi.org/10.1007/s00453-025-01322-y'
bibtexurl: 'https://yuvalyitz.github.io/files/heeger2025fair.bib'
citation: 'Heeger, K., Hermelin, D., Itzhaki, Y., Molter, H. and Shabtay, D., 2025. Fair Repetitive Interval Scheduling. Algorithmica, 87, pp. 1340–1368.'
---
Fair resource allocation is undoubtedly a crucial factor in customer satisfaction in several scheduling scenarios. This is especially apparent in repetitive scheduling models where the same clients repeatedly submit jobs on a daily basis. In this paper, we aim to analyze a repetitive scheduling model involving a set of n clients and a set of m days. On every day, each client submits a request to process a job exactly within a specific time interval, which may vary from day to day, modeling the scenario where the scheduling is done Just-In-Time. The daily schedule is executed on a single machine that can process a single job at a time, therefore it is not possible to schedule jobs with intersecting time intervals. Accordingly, a feasible solution corresponds to sets of jobs with disjoint time intervals, one set per day. We define the quality of service that a client receives as the number of executed jobs over the m days period. Our objective is to provide a feasible solution where each client has at least k days where his jobs are processed. We prove that this problem is NP-hard even under various natural restrictions such as identical processing times and day-independent due dates. We also provide efficient algorithms for several special cases and analyze the parameterized tractability of the problem with respect to several parameters, providing both parameterized hardness and tractability results. 
