{% extends 'base.html' %}

{% block body %}
<div class="container mt-4">
    <h3>Search Results for: <span style="color:#28a745;">"{{ query }}"</span></h3>
    <hr>

    {% if query %}
        <p>You searched for: <strong>{{ query }}</strong></p>
        <!-- Add results here -->
    {% else %}
        <p>No search query provided.</p>
    {% endif %}
</div>
{% endblock %}
