# Modeling Neighborhood Dynamics

We will use the Columbus MSA as an example to illustrate the `dynamics` module of `geosnap`.

* Modeling transition rates between neighborhood types across time
* Analyzing whole neighborhood sequence

## Data preperation

* Geodemographics for neighborhood segamentation

from geosnap import Community
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import sys, os
import warnings
warnings.filterwarnings("ignore")

columbus = Community.from_ltdb(msa_fips='18140')

columbus1 = columbus.cluster(columns=['median_household_income', 
                                      'p_poverty_rate', 
                                      'p_edu_college_greater', 
                                      'p_unemployment_rate'], 
                             method='ward')

columbus1.gdf.head()

## Estimating the transition rates between neighborhood types

#### Nonspatial transition rates - Classic Markov modeling of transitions 

m = columbus1.transition(cluster_col="ward")
type(m)

m.p

sns.set()
fig, ax = plt.subplots(1,1,figsize = (5,4)) 
im=sns.heatmap(m.p, annot=True, linewidths=.5, cbar=True, vmin=0, vmax=1,
              square=True, xticklabels= m.classes, yticklabels=m.classes, ax=ax)
im.set_title("Empircal transition rates",fontsize=14) 
plt.tight_layout()

#### Spatially conditional transition rates - Spatial Markov modeling of transitions 

import numpy as np
np.random.seed(5)

sm = columbus1.transition(cluster_col="ward", w_type="queen")
type(sm)

sm.p

sm.P[0]

sm.P[0]

fig, axes = plt.subplots(3,3,figsize = (13,12)) 
ls = sm.classes
lags_all = ["Spatial Lag - "+str(l)  for l in ls]
for i in range(3):
    for j in range(3):
        ax = axes[i,j]
        if i==0 and j==0:
            p_temp = sm.p
            sns.heatmap(p_temp, annot=True, linewidths=.5, ax=ax, cbar=True, vmin=0, vmax=1,
                      square=True, xticklabels= ls, yticklabels=ls)
            ax.set_title("Global",fontsize=14) 
        # Loop over data dimensions and create text annotations.
        else:
            n = i*3+j-1
            if n>=len(sm.classes):
                ax.axis('off')
                continue
                
            p_temp = sm.P[n]
            im=sns.heatmap(p_temp, annot=True, linewidths=.5, ax=ax, cbar=True, vmin=0, vmax=1,
                          square=True, xticklabels= ls, yticklabels=ls)

            ax.set_title(lags_all[n],fontsize=14) 
plt.tight_layout()

## Whole sequence analysis

* evaluate the distance/disimilarity between every pair of neighborhood sequences based on a selected sequence method
* apply clustering algorithms to obtain a segmentation of neighborhood sequences

### (1) Comparing sequences of transitions.

transition-oriented optimal matching.

# Use the sequence method to obtain the distance matrix of neighborhood sequences
gdf_new, df_wide, seq_dis_mat = columbus1.sequence(seq_clusters=5,
                                                   dist_type="tran",
                                                   cluster_col="ward")
seq_dis_mat

df_wide.head()

df_wide.values[0]

from geosnap.visualize import indexplot_seq

indexplot_seq(df_wide, clustering="tran_5", palette="pastel")

### (2) Hamming distance

gdf_new, df_wide, seq_dis_mat = columbus1.sequence(seq_clusters=8,dist_type="hamming", cluster_col="ward")
seq_dis_mat

indexplot_seq(df_wide, clustering="hamming_8", palette="pastel")

Change the number of clusters

gdf_new, df_wide, seq_dis_mat = columbus1.sequence(seq_clusters=5,dist_type="hamming", cluster_col="ward")
seq_dis_mat

df_wide.values[0]

indexplot_seq(df_wide, clustering="hamming_5", palette="pastel")

### (3) Arbitrary distance

 substitution=0.5, indel=1

gdf_new, df_wide, seq_dis_mat = columbus1.sequence(seq_clusters=5,
                                                   dist_type="arbitrary", cluster_col="ward")
df_wide.head()

indexplot_seq(df_wide, clustering="arbitrary_5", palette="pastel")

