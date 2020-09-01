# Working with `Community`s

the `Community` object is geosnap's central data structure. A `Community` is a dataset that stores information about a collection of neighborhoods over several time periods, including each neighborhood's physical, socioeconomic, and demographic attributes and its demarcated boundaries. Under the hood, each `Community` is simply a long-form geopandas geodataframe with some associated metadata. 

If you're working with built-in data, you instantiate a `Community` by choosing the constructor for your dataset and passing either a boundary (geodataframe) or a selection filter that defines the study area. The selection filter can be either a `GeoDataFrame` boundary or a set of [FIPS](https://www.policymap.com/2012/08/tips-on-fips-a-quick-guide-to-geographic-place-codes-part-iii/) codes. Boundary queries are often more convenient but they are  more expensive to compute and will take longer to construct.

When constructing `Community`s from fips codes, the constructor has arguments for state, county, msa, or list of any arbitrary fips codes. If more than one of these arguments is passed, geosnap will use the union. This means that each level of the hierarchy is available for convenience but you are free to mix and match msas, states, counties, and even single tracts to create your study region of choice

If you're working with your own data, you instantiate a `Community` by passing a list of geodataframes (or a single long-form).

from geosnap import Community

## Create a `Community` from built-in census data

The quickest and easiest method for getting started is to instantiate a Community using the built-in census data. To do so, you use the `Community.from_census` constructor:

# this will create a new community using data from Washington DC (which is fips code 11)
dc = Community.from_census(state_fips="11")

Note that when using `Community.from_census`, the resulting community has *unharmonized* tract boundaries, meaning that the tracts are different for each decade

To access the underlying data from a `Community`, simply call its `gdf` attribute which returns a geodataframe

dc.gdf.head()

You can easily create figures of time series plots from geosnap `Community` objects using the `plot_timeseries` class method. `plot_timeseries` uses `proplot`, a lightweight `matplotlib` wrapper with its own feature set. It also uses [`contextily`](https://github.com/geopandas/contextily) to (optionally) provide a nice basemap

dc.plot_timeseries(
    "p_nonhisp_white_persons",
    scheme="quantiles",
    cmap="Blues",
    k=6,
    alpha=0.7,
    years=[1990, 2000, 2010],
)

`plot_timeseries` default behavior is to graph every year in the provided `Community` object in chronological order with OpenStreetMaps.Mapnik from contextily as the basemap. If you pass the list `years=[]` , then `plot_timeseries` will graph in the order that the list was passed. You can also specify another map provider for contextily, or disable it by passing `False` with the parameter`ctxmap`.

The `save_fig` parameter in `plot_timeseries` tells the function to save the resulting plot with the specified name and path. Note that if the file extension is not specified then the image will be saved as a `.pdf`, and that the path specified must already exist.

## Create a `Community` from Longitudinal Employment-Household Dynamics

You can also create a `Community` from block-level LEHD census data. Unlike the decennial census, LEHD data are annual and contain information about the "workplace area characteristics" ("wac") and "residence area characteristics" ("rac") of employees. "wac" datasets contain information about where employees work, while "rac" datasets contiain information about where they live. Apart from information about the race, skill level, and income of emmployees in eaech census block, LEHD data also count the number of workers in each NAICS 2-digit industry category.

If you use the `Community.from_lodes` constructor, you can collect data from 2000 to 2015

delaware = Community.from_lodes(state_fips="10", years=[2014, 2015])

delaware.gdf.head()

delaware.gdf[delaware.gdf.year == 2015].plot(
    column="total_employees", scheme="quantiles", k=9
)

## Create a `Community` from a longitudinal database

To instantiate a `Community` from a longitudinal database, you must first register the database with geosnap using either `store_ltdb` or `store_ncdb`. Once the data are available in datasets, you can call `Community.from_ltdb` and `Community.from_ncdb`

### LTDB using fips codes

I don't know the Riverside MSA fips code by heart, so I'll slice through the `msas` dataframe in the data store to find it

from geosnap import datasets

datasets.msas()[datasets.msas().name.str.startswith("Riverside")]

riverside = Community.from_ltdb(msa_fips="40140")

riverside.plot_timeseries("p_poverty_rate", scheme="quantiles", cmap="Blues", k=6)

Instead of passing a fips code, I could use the `boundary` argument to pass the riverside MSA as a geodataframe. This is more computationally expensive because it requires geometric operations, but is more flexible because it allows you to create communities that don't nest into fips hierarchies (like zip codes, census designated places, or non-US data)

### NCDB Using a boundary

# grab the boundary for Sacramento from libpysal's built-in examples

import geopandas as gpd
from libpysal.examples import load_example

sac = load_example("Sacramento1")
sac = gpd.read_file(sac.get_path("sacramentot2.shp"))

sacramento = Community.from_ncdb(boundary=sac)

import contextily as ctx

sacramento.plot_timeseries(
    "median_household_income",
    scheme="quantiles",
    cmap="Blues",
    k=6,
    alpha=0.6,
    ctxmap=ctx.providers.Stamen.TonerLite,
    years=[1990, 2000, 2010],
)

## Create a `Community` from a list of geodataframes

If you are working outside the US, or if you have data that aren't included in geosnap (like census blocks or zip codes) then you can still create a community using the `Community.from_geodataframes` constructor, which allows you to pass a list of geodataframes that will be concatenated into the single long-form gdf structure that geosnap's analytics expect.

This constructor is typically used in cases where a researcher has several shapefiles for a study area, each of which pertainin to a different time period. In such a case, the user would read each shapefile into a geodataframe and ensure that each has a "time" column that will differentiate each time period from one another in the long-form structure (e.g. if each shapefile is a different decade, then the 1990 shapefile should have a column called "year" in which every observation has a value of 1990). Then, these geodataframes simply need to be passed in a list to the `from_geodataframes` constructor

Here, I'll use `cenpy` to grap population data from two different ACS vintages and combine them into a single community

from cenpy.products import ACS

chi13 = ACS(2013).from_place("chicago", variables="B00001_001E")

chi13["year"] = 2013

chi17 = ACS(2017).from_place("chicago", variables="B00001_001E")

chi17["year"] = 2017

chicago = Community.from_geodataframes([chi13, chi17])

chicago.plot_timeseries(
    "B00001_001E",
    cmap="Greens",
    scheme="quantiles",
    k=6,
    ctxmap=ctx.providers.Stamen.TonerLite,
    alpha=0.5,
    title='Chicago Population by Census Tract',
)

