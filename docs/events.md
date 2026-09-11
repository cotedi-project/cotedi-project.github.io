---
layout: events
title: Project Events
pagination:
  data: collections.event
  size: 10
  reverse: true
  alias: posts
---

<ul class="events">{% for event in collections.event -%}
<li>
<span class="event-date">{{ event.date | readableDate }}</span> 
<a href="{{ event.url | url }}">{{ event.data.title | safe }}</a>
        (<i class="bi bi-geo-alt-fill"></i>{{event.data.location}})
</li>
{%- endfor %}</ul>