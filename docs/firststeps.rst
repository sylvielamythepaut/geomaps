First Steps Tutorial
====================

This is an easy to follow tutorial that gets you up to speed with *ecmwf-geomaps*
to visualise meteorological data.
It assumes you have basic Python programming knowledge.

So, let's start with plotting a simple map:

.. code-block:: python

    from ecmwf.geomaps import GeoMap
    
    geomap = GeoMap()
    geomap.coastlines(land_colour="grey")
    geomap.show()

.. image:: _static/example-plots/firststeps-coast.png
  :width: 100%
