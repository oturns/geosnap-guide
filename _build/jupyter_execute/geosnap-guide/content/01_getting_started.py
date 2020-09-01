# Getting Started

geosnap provides a set of tools for collecting data and constructing space-time datasets, identifying local neighborhoods or prototypical neighborhood types, modeling neighborhood change over time, and visualizing data at each step of the process.

geosnap works with data from anywhere in the world, but comes batteries-included with three decades of national US Census data, including boundaries for metropolitan statistical areas, states, counties, and tracts, and over 100 commonly used demographic and socioeconomic variables at the census-tract level. All of these data are stored as geopandas geodataframes in efficient [apache parquet](https://parquet.apache.org/) files and distributed through [quilt](https://quiltdata.com/). 

These data are available when you first import geosnap by streaming from our [quilt bucket](https://spatialucr.quiltdata.com/b/spatial-ucr) into memory. That can be useful if you dont need US data or if you just want to kick the tires, but it also means you need an internet connection to work with census data, and things may slow down depending on your network performance. For that reason, you can also use the `store_census` function to cache the data on your local machine for faster querying. This will only take around 400mb of disk space, speed up data operations, and remove the need for an internet connection.

 

## Using built-in data

You can access geosnap's built-in data from the `datasets` module. It contains a variable codebook as well as state, county, and MSA boundaries, in addition to boundaries and social data for three decades of census tracts. If you have stored an existing longitudinal database such as LTDB or the Geolytics Neighborhood Change Database, it will be available in `datasets` as well.

from geosnap import datasets

dir(datasets)

Everything in `datasets` is a pandas (or geopandas) geo/dataframe. To access any of the data inside, just call the appropriate attribute/method (most datasets are methods). For example, to accesss the codebook which outlines each variable in the data store, incuding its name, description, the original census sources/variable names and the formula used to calculate it, you simply call `datasets.codebook()`. We support the same variable set the Longitudinal Tract Database (LTDB).

datasets.codebook().tail()

You can also take a look at the dataframes themselves or plot them as quick choropleth maps

datasets.tracts_2000().head()

datasets.states().plot()

from matplotlib import pyplot as plt

fig, axs = plt.subplots(1,3, figsize=(15,5))
axs = axs.flatten()

datasets.tracts_1990()[datasets.tracts_1990().geoid.str.startswith('11')].dropna(subset=['median_household_income']).plot(column='median_household_income', cmap='YlOrBr', k=6, scheme='quantiles', ax=axs[0])
axs[0].set_title(1990)
axs[0].axis('off')

datasets.tracts_2000()[datasets.tracts_2000().geoid.str.startswith('11')].dropna(subset=['median_household_income']).plot(column='median_household_income', cmap='YlOrBr', k=6, scheme='quantiles', ax=axs[1])
axs[1].set_title(2000)
axs[1].axis('off')

datasets.tracts_2010()[datasets.tracts_2010().geoid.str.startswith('11')].dropna(subset=['median_household_income']).plot(column='median_household_income', cmap='YlOrBr', k=6, scheme='quantiles', ax=axs[2])
axs[2].set_title(2010)
axs[2].axis('off')


As mentioned above, you save these data locally for better performance using `geosnap.io.store_census`, which will download two quilt packages totaling just over 400mb (which is an exceedingly small file size, when you consider how much data are packed into those files). Once data are stored locally, you won't need this function again unless you want to update your local package to the most recent version on quilt.

from geosnap.io import store_census
store_census()

Using geosnap's built-in data, researchers can get a jumpstart on neighborhood analysis with US tract data, but census tracts are not without their drawbacks. Many of geosnap's analytics require that neighborhood units remain consistent and stable in a study area over time (how can you analyze neighborhood change if your neighborhoods are different in each time period?), but with each new decennial census, tracts are redrawn according to population fluctuations. Geosnap offers two methods for dealing with this challenge.

First, geosnap can create its own set of stable longitudinal units of analysis and convert raw census or other data into those units. Its `harmonize` module provides tools for researchers to define a set of geographic units and interpolate data into those units using moden spatial statistical methods. This is a good option for researchers who are interested in the ways that different interpolation methods can affect their analyses or those who want to use state-of-the-art methods to create longitudinal datasets that are more accurate than those provided by existing databases.

Second, geosnap can simply leverage existing data that has already been standardized into a set of consistent units. The `io` module provides tools for reading and storing existing longitudinal databases that, once ingested, will be available in the data store and can be queried and analyzed repeatedly. This is a good option for researchers who want to get started modeling neighborhood characteristics right away and are less interested in exploring how error propagates through spatial interpolation.   

 

## Storing Data from External Databases

The quickest way to get started with geosnap is by importing pre-harmonized census data from either the [Longitudinal Tract Database
(LTDB)](https://s4.ad.brown.edu/projects/diversity/Researcher/LTDB.htm) created by researchers from Brown University or the [Neighborhood Change Database](http://www.geolytics.com/USCensus,Neighborhood-Change-Database-1970-2000,Products.asp) created by the consulting company Geolytics. While licensing restrictions prevent either of these databases from being distributed inside geosnap, LTDB is nonetheless *free*. As such, we recommended importing LTDB data before getting started with geosnap

### Longitudinal Tract Database (LTDB)

The [Longitudinal Tract Database
(LTDB)](https://s4.ad.brown.edu/projects/diversity/Researcher/LTDB.htm) is a
freely available dataset developed by researchers at Brown University that
provides 1970-2010 census data harmonized to 2010 boundaries.

To store LTDB data and make it available to geosnap, proceed with the following:

1. Download the raw data from the LTDB [downloads
  page](https://s4.ad.brown.edu/projects/diversity/Researcher/LTBDDload/Default.aspx).
  Note that to construct the entire database you will need two archives: one
  containing the sample variables, and another containing the "full count"
  variables.
    - Use the dropdown menu called **select file type** and choose "full"; in
      the dropdown called **select a year**, choose "All Years"
    - Click the button "Download Standard Data Files"
    - Repeat the process, this time selecting "sample" in the **select file
      type** menu and "All years" in the **select a year** dropdown
2. Note the location of the two zip archives you downloaded. By default they are called 
    - `LTDB_Std_All_Sample.zip` and
    - `LTDB_Std_All_fullcount.zip`

3. Start ipython/jupyter, import geosnap, and call the `store_ltdb` function with the paths of the two zip archives you downloaded from the LTDB project page:


from geosnap.io import store_ltdb

# if the archives were in my downloads folder, the paths might be something like this
sample = "/Users/knaaptime/Downloads/LTDB_Std_All_Sample.zip"
full = "/Users/knaaptime/Downloads/LTDB_Std_All_fullcount.zip"

# uncomment to run
#store_ltdb(sample=sample, fullcount=full)

 

That function will extract the necessary data from the archives, calculate additional variables using formulas from the codebook, create a new local quilt package for storing the data, and register the database with the `datasets`. After the function has run, you will be able to access the LTDB data as a long-form geodataframe by calling the `ltdb` attribute from the data store. As with the `store_census` function above, this only needs to be run a single time to save the data as a local quit package and register it with geosnap. You won't neeed to store the data again unless there's an update to the variable formulas in the codebook.

#datasets.ltdb.head()

### Geolytics Neighborhood Change Database

The Neighborhood Change Database (ncdb) is a commercial database created by Geolytics and the Urban Institute. Like LTDB, it provides census data harmonized to 2010 tracts. NCDB data must be purchased from Geolytics prior to use. If you have a license, you can import NCDB into geosnap with the following:

1. Open the Geolytics application
2. Choose "New Request":   
![Choose "New Request"](https://github.com/spatialucr/geosnap/blob/master/docs/figs/geolytics_interface1.PNG?raw=true)
3. Select CSV or DBF
4. Make the following Selections:
    - **year**: all years in 2010 boundaries
    - **area**: all census tracts in the entire united states
    - **counts**: [right click] Check All Sibling Nodes

![](https://github.com/spatialucr/geosnap/blob/master/docs/figs/geolytics_interface2.PNG?raw=true)

5. Click `Run Report`

6. Note the name and location of the CSV you created

7. Start ipython/jupyter, import geosnap, and call the `store_ncdb` function with the path of the CSV:


from geosnap.io import store_ncdb

ncdb_path = "~/Downloads/ncdb.csv"

# note this will raise several warnings since NCDB does not contain all the underlying data necessary to calculate all the variables in the codebook

# uncomment to run
# store_ncdb(ncdb_path)

As with above, you can access the geolytics data through the `ncdb` attribute of the `datasets`

#datasets.ncdb.head()

