# Simulating Neighborhood Socio-Spatial Dynamics

By combining a few simple steps, `geosnap` is capable of simulating neighborhood change into the future. To do so, it relies on the notion of a spatially-conditioned Markov transition model. Put simply, if we know what Type a neighborhood used to be, and we know what Types of neighborhoods surround it, we can make an informed prediction about what Type the neighborhood is likely to be during the next time period. 

from geosnap import datasets, Community
import matplotlib.pyplot as plt

## Cluster Model

We start by developing a cluster model of neighborhood types, where each geographic unit can take on a different type in successive years

VARS = ['p_nonhisp_black_persons', 'p_nonhisp_white_persons', 'p_hispanic_persons', 'p_asian_persons', 'median_household_income', 'median_home_value', 'p_unemployment_rate', 'p_poverty_rate']

balt = Community.from_ltdb(msa_fips='12580', years=[1980, 1990, 2000, 2010])

balt = balt.cluster(method='ward', k=6, columns=VARS)

balt.plot_timeseries('ward', categorical=True, figsize=(24,6))

## Transition Model

For these neighborhood types we can create a transition model. The following heatmap shows which neighborhoods are likely to transition into each other type of neighborhood, and critically, how those probabilities change under different conditions of spatial context

balt.plot_transition_matrix('ward', n_rows=2, n_cols=4, figsize=(16,8), suptitle='Neighborhood Transitions in Baltimore')

Another way of visualizing the transition matrices is as a network graph where neighborhood types are represented as nodes and the transition probabilities between them are represented as edges. 

balt.plot_transition_graphs('ward', 'queen', output_dir="images/")

Here, the global (aspatial) transition matrix is laid out as a graph. We can see quickly that some neighborhood types like Type 2 have higher in-degree than out-degree, meaning many different neighborhood types transition into Type 2, but once there, Type 2 only transitions into a few other types

![img](images/ward_transitions_global.png)

## Simulating Neighborhood Change

If we expect these same socio-spatial dynamics to persist over time, then we can use our spatial Markov transition model to simulate neighborhood change into the future. The `predict` method takes a cluster model name and simulates forward for a specified number of time steps, then returns a new `Community` with the predicted data

predicted = balt.simulate('ward', base_year=2010, w_type='queen', time_steps=4)

balt.plot_timeseries('ward', categorical=True, legend=False, figsize=(20,6), title='Observed')
predicted.gdf = predicted.gdf[predicted.gdf.year!=2010] # dont include the base year
predicted.plot_timeseries('ward', categorical=True, legend=False,figsize=(20,6), title='Predicted')

The top plot shows the observed neighborhood types over the 4 time periods from 1980 to 2010. The bottom plot shows the next four predicted time periods from 2020 to 2050, assuming the underlying transition model remains constant

For a more dynamic view of the neighborhood evolution process, we can create a simple animation from these data:

balt.gdf = balt.gdf[balt.gdf.year!= 1980]  #  in 1980, Queen Anne's county wasnt in the MSA, so the different bounds make the animation awkward
combined_sequence = Community.from_geodataframes([balt.gdf, predicted.gdf])

combined_sequence.animate_timeseries('ward', categorical=True, filename='images/simulation.gif', dpi=200)

![simulation](images/simulation.gif)

