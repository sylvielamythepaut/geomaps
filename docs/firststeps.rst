First Steps Tutorial
====================

This is an easy to follow tutorial that gets you up to speed with *ecmwf-geomaps*
to visualise meteorological data.
It assumes you have basic Python programming knowledge.

So, let's start with what *ecmwf-geomaps* does best:

.. code-block:: python

    from ecmwf.geomaps import GeoMap
    
    geomap = GeoMap()
    geomap.coastlines(land_colour="grey")
    geomap.show()
