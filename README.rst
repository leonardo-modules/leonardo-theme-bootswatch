
=========================
Leonardo Bootswatch Theme
=========================

Bootswatch http://bootswatch.com/ bundled as Leonardo theme.

Installation
============

.. code-block:: bash

    pip install leonardo-theme-bootswatch

    # or as extras

    pip install django-leonardo[bootswatch]

No next steps reuires, Leonardo automaticaly detects this theme and adds it to ``INSTALLED_APPS``, but if you want, you could do this

.. code-block:: python

    # leonardo apps
    APPS += ['leonardo_theme_bootswatch']
    
    # or Django apps

    INSTALLED_APPS += ['leonardo_theme_bootswatch']

After installation don't forget run ``sync_all`` command.

.. code-block:: python

    python manage.py sync_all

Read More
=========

* https://github.com/django-leonardo/django-leonardo
* http://django-leonardo.readthedocs.org/en/develop/overview/modules.html