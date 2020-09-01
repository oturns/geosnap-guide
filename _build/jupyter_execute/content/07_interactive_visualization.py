# Experimental Interactive Visualization

You can test geosnap's experimental dataset explorer from the `visualize` module. This simple variable explorer will launch a [dash] app on your local machine that allows you to explore datasets for different metropolitan regions around the country

from IPython.display import Image
Image("../docs/figs/commviz.png")

To use the explorer, import the function from the visualization module and pass the dataset you'd like to explore. The current options are 'census', 'ltdb', or 'ncdb', though note that to use either of the latter, you must have registered the appropriate database using the `store_ltdb` or `store_ncdb` functions. 

The function will launch a new browser window with the interactive viz

from geosnap.visualize import explore
# uncomment to run
# explore(data='ltdb')



