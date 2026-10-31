---
title: "Multi-Depot Metric TSP"
collection: talks
type: "Poster"
permalink: /talks/2026-11-05-gifts-multi-depot-metric-tsp-poster/
venue: "German-Israeli Forum for Tomorrow's Scientists (GIFTS) 2026"
date: 2026-11-05
location: "Berlin, Germany"
eventurl: "https://gifts.scienceabroad.org.il/"
posterurl: "/files/poster_multi_depot_metric_tsp.pdf"
---

[Poster](/files/poster_multi_depot_metric_tsp.pdf) to be presented at the [German-Israeli Forum for Tomorrow's Scientists (GIFTS) 2026](https://gifts.scienceabroad.org.il/), organized by the German-Israeli Foundation for Scientific Research and Development (GIF) and ScienceAbroad, held on November 5, 2026, in Berlin as part of Berlin Science Week.

## Authors

Yuval Itzhaki and Matthias Mnich.

## Abstract

In Multi-Depot Metric TSP, we are given an undirected graph with metric edge weights and a set of $$d$$ depots. The task is to find a minimum-weight set of cycles (subtours) that together visit all vertices, with a depot on every subtour. For a single depot this is the classic metric TSP, for which Christofides and Serdyukov's 3/2-approximation remains the best known.

We give a 3/2-approximation for Multi-Depot Metric TSP running in time $$2^{O(d \log d)} n^{O(1)}$$. The algorithm splits the instance along candidate clusters and applies Christofides' algorithm to the pieces.
