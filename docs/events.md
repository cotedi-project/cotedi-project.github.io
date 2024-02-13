--- 
layout: index.njk
title: Upcoming Events
limit: 10
--- 
{% set presentDate %}{% thisDate %}{% endset %}

<ul class="events">{% for event in collections.event -%}
    {% if presentDate < event.date | htmlDateString -%}
    <li>
        <span class="event-date">{{ event.date | readableDate }}</span> 
        <a href="{{ event.url | url }}">{{ event.data.title | safe }}</a>
        (<i class="bi bi-geo-alt-fill"></i>{{event.data.location}})
    </li>
    {%- endif %}
{%- endfor %}</ul>

