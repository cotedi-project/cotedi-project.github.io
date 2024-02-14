---
title: Partners
long_title: Six countries and 16 institutions are driving the CoTEDI project. 
hero_image: 
---

<h4>{{ long_title }}</h4>
{% set allpartners = partners.research %}
{% set allpartners = allpartners.concat(partners.schools) %}

{% for partner in allpartners %}{% if not partner.ignore -%}
<card class="partner">
<div class="partnerlogo">
{%if partner.logo -%}
        {% for logo in partner.logo -%}
        <img alt="{{ partner.name }} ({{ partner.acronym }})" src="/images/partners/{{logo}}" class="logo {{ partner.acronym | lower }}">
        {%- endfor %}
{%- endif %}
</div>
<div class="partnerinfo">
    <h3>{{ partner.name }}</h3>
    <p class="country">{{ site.countries[ partner.country ] }}</p>{% if partner.team -%}{% set teamlead = partner.team | first %}
    <p class="teamlead">Led by <a href="{{ teamlead.url }}" target="_blank">{{ teamlead.name }}</a></p>{% if partner.team | length > 1 -%}
    <p class="contributors"></p><ul>
    {% for member in partner.team -%}
    {% if loop.index0 -%}
        <li>{{ member.name }}</li>
    {%- endif %}
    {%- endfor %}
    </ul>
    {%- endif %}
    {%- endif %}
</div>
</card>
{%- endif %}{% endfor %}