# Visualize the neighborhood sequences within each sequence cluster

import numpy as np
import pandas as pd
%matplotlib inline

## An example of LA

Suppoose we have applied two sequence methods to assess the dissimilarity of neighborhood sequences and obtained two clusterings on neighborhood sequences. These two neighborhood sequences clusterings are stored as two columns in a csv file together with neighborhood types in 1970, 1980, 1990, 2000, and 2010.

We first read the csv file:

df_LA = pd.read_csv("data/LA_sequences.csv", converters={'GEO2010': lambda x: str(x)})
df_LA.head()

The two neighborhood sequences clusterings labels are store in "seqC1" and "seqC2". We can call the index plot function in `geosnap` to visualize the compositions of sequences within each cluster:

from geosnap.visualize import indexplot_seq

### (1) "seqC1"

indexplot_seq(df_LA, clustering="seqC1", palette="pastel")

indexplot_seq(df_LA, clustering="seqC1", palette="pastel", ncols=4)

indexplot_seq(df_LA, clustering="seqC1", palette="pastel", ncols=2)

### (2) "seqC2"

indexplot_seq(df_LA, clustering="seqC2", palette="pastel")

