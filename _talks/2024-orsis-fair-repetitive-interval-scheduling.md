---
title: "Fair Repetitive Interval Scheduling"
collection: talks
type: "Talk"
permalink: /talks/2024-05-27-orsis-fair-repetitive-interval-scheduling/
venue: "Operations Research Society of Israel (ORSIS) Annual Meeting"
date: 2024-05-27
location: "Be'er Sheva, Israel"
eventurl: "https://www.orsis.org.il/registration-information-2024"
---

Talk at the [Operations Research Society of Israel (ORSIS) Annual Meeting](https://www.orsis.org.il/registration-information-2024), held on May 27-28, 2024, at Ben-Gurion University of the Negev, Be'er Sheva.

## Abstract

Fair resource allocation is undoubtedly a crucial factor in customer satisfaction in several scheduling scenarios. This is even more apparent in repetitive scheduling models where the same set of clients repeatedly submit jobs on a daily basis.

In this work, we analyze a repetitive scheduling system involving a set of \(n\) clients and a set of \(q\) days. On each day, each client submits a request to process a job exactly within a specific time interval, which may vary from day to day, modeling a Just-In-Time (JIT) scheduling setting. The daily schedule is executed on a single machine, and therefore jobs with intersecting intervals cannot be scheduled together. Accordingly, a feasible solution consists of a set of jobs with disjoint time intervals, one set per day.

To ensure that the quality of service received by the clients is sufficiently fair, the objective is to find a feasible solution in which each client has at least \(k\) days on which their jobs are processed. We prove that this problem is NP-hard even under several natural restrictions, such as identical processing times and day-independent due dates. We also provide efficient algorithms for some special cases and analyze the parameterized tractability of the problem with respect to several parameters, giving both parameterized hardness and tractability results.
