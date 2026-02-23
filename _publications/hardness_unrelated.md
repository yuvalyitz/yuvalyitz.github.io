---
title: "Hardness of Interval Scheduling on Unrelated Machines"
collection: publications
category: conferences
permalink: /publication/hardness_unrelated
excerpt: "Hardness results for Interval Scheduling on Unrelated Machines, including W[1]-hardness in the machine parameter and NP-completeness of the unweighted case."
date: 2022-12-14
venue: "17th International Symposium on Parameterized and Exact Computation (IPEC 2022)"
paperurl: "https://doi.org/10.4230/LIPIcs.IPEC.2022.18"
bibtexurl: "https://yuvalyitz.github.io/files/hermelin2022hardness.bib"
citation: "Danny Hermelin, Yuval Itzhaki, Hendrik Molter, and Dvir Shabtay. Hardness of Interval Scheduling on Unrelated Machines. In 17th International Symposium on Parameterized and Exact Computation (IPEC 2022). Leibniz International Proceedings in Informatics (LIPIcs), Volume 249, pp. 18:1-18:16, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2022)"
---

We provide new (parameterized) computational hardness results for Interval Scheduling on Unrelated Machines. It is a classical scheduling problem motivated from just-in-time or lean manufacturing, where the goal is to complete jobs exactly at their deadline. We are given n jobs and m machines. Each job has a deadline, a weight, and a processing time that may be different on each machine. The goal is find a schedule that maximizes the total weight of jobs completed exactly at their deadline. Note that this uniquely defines a processing time interval for each job on each machine.
Interval Scheduling on Unrelated Machines is closely related to coloring interval graphs and has been thoroughly studied for several decades. However, as pointed out by Mnich and van Bevern [Computers & Operations Research, 2018], the parameterized complexity for the number m of machines as a parameter remained open. We resolve this by showing that Interval Scheduling on Unrelated Machines is W[1]-hard when parameterized by the number m of machines. To this end, we prove W[1]-hardness with respect to m of the special case where we have parallel machines with eligible machine sets for jobs. This answers Open Problem 8 of Mnich and van Bevern’s list of 15 open problems in the parameterized complexity of scheduling [Computers & Operations Research, 2018].
Furthermore, we resolve the computational complexity status of the unweighted version of Interval Scheduling on Unrelated Machines by proving that it is NP-complete. This answers an open question by Sung and Vlach [Journal of Scheduling, 2005].

---

[View paper on LIPIcs](https://doi.org/10.4230/LIPIcs.IPEC.2022.18)  
[Download BibTeX](https://yuvalyitz.github.io/files/hermelin2022hardness.bib)
