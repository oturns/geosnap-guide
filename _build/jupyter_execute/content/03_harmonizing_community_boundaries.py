# Harmonizing Community Boundaries

from geosnap import Community

## Data prep

dc = Community.from_lodes(state_fips="11", years=[2010, 2015])

dc_tracts = Community.from_census(state_fips="11", years=2010)

# tract level data from 2010, this is the source
tracts = dc_tracts.gdf

# block level data from 2015, this is the target
blocks = dc.gdf[dc.gdf.year == 2015]

# original block-level data for 2010, this is the ground truth
test = dc.gdf[dc.gdf.year == 2010]

# rename this variable so its the same on blocks/tracts
tracts["population"] = tracts["n_total_pop"]

# community with mixed geoms
hybrid = Community.from_geodataframes([blocks, tracts])

## Harmonizing a community with areal interpolation



# this wil take the 2010 tract data and interpolate it to 2015 boundaries (the same as 2010)
# using pure area interpolation here

hybrid_area = hybrid.harmonize(2015, extensive_variables=["population"])

## Harmonizing a community with areal interpolation and auxiliary data



# this will do the same as above, but will use 2011 NLCD data to constrain the overlay to what's considered developed land

hybrid_raster = hybrid.harmonize(
    2015, extensive_variables=["population"], weights_method="land_type_area", raster='../nlcd_2011.tif'
)

interpolated_area = hybrid_area.gdf[hybrid_area.gdf.year == 2010]
interpolated_raster = hybrid_raster.gdf[hybrid_raster.gdf.year == 2010]

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(20, 8))
titles = ["truth", "area", "raster"]
for i, data in enumerate([test, interpolated_area, interpolated_raster]):
    data.plot("population", ax=axs[i])
    axs[i].set_title(titles[i])

diff = test.population - interpolated_area.population

diff.hist()
diff.describe()

diff = test.population - interpolated_raster.population

diff.hist()
diff.describe()

