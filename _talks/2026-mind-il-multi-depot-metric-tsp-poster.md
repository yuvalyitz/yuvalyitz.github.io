---
title: "Multi-Depot Metric TSP"
collection: talks
type: "Poster"
permalink: /talks/2026-10-26-mind-il-multi-depot-metric-tsp-poster/
venue: "Mind-IL 2026, Computer Science Conference in Memory of Michael Rabin"
date: 2026-10-26
location: "Tel Aviv, Israel"
eventurl: "https://www.mind-il.org/conference/6a3031aea90316da446a7899"
posterurl: "/files/poster_multi_depot_metric_tsp.pdf"
---

[Poster](/files/poster_multi_depot_metric_tsp.pdf) presented at the [Computer Science conference in memory of Michael Rabin](https://www.mind-il.org/conference/6a3031aea90316da446a7899), part of Mind-IL 2026, held on October 26, 2026, at Tel Aviv University.

## Authors

Yuval Itzhaki and Matthias Mnich.

## Abstract

In Multi-Depot Metric TSP, we are given an undirected graph with metric edge weights and a set of $$d$$ depots. The task is to find a minimum-weight set of cycles (subtours) that together visit all vertices, with a depot on every subtour. For a single depot this is the classic metric TSP, for which Christofides and Serdyukov's 3/2-approximation remains the best known.

We give a 3/2-approximation for Multi-Depot Metric TSP running in time $$2^{O(d \log d)} n^{O(1)}$$. The algorithm splits the instance along candidate clusters and applies Christofides' algorithm to the pieces.
