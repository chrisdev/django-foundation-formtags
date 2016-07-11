Usage
=====

To start use django-foundation-forms in a project you must include in your settings::

    INSTALLED_APPS = (
        'foundation_tags',
    )
    
In the template load foundation tags by::

    {% load foundation_tags %}

To use the django-form-foundation filter::

    <form class="form" action="{{ url }}" method="POST">
        {% csrf_token %}
        {{ form|as_foundation }}
    </form>
    
To use the django-form-foundation field tags::

    <form class="form" action="{{ url }}" method="POST">
        {% csrf_token %}
        {% render_field form.name %}
        
        {% render_field form.subject %}
        
        {% render_field form.message %}
    </form>