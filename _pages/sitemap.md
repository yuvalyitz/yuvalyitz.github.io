---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
sitemap: false
---

- [About]({{ '/' | relative_url }})
{% for item in site.data.navigation.main %}
- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
- [Privacy]({{ '/terms/' | relative_url }})

[XML sitemap]({{ '/sitemap.xml' | relative_url }})
