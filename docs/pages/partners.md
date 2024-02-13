---
title: Partners
---

## Universities

{% for partner in partners.research %}{% if not partner.ignore -%}
<div class="partner">
<h3>{{ partner.name }} ({{ partner.country }})</h3>
</div>
{%- endif %}{% endfor %}

## Schools

{% for partner in partners.schools %} 
<div class="partner">
<h3>{{ partner.name }} ({{ partner.country }})</h3>
</div>
{% endfor %}
