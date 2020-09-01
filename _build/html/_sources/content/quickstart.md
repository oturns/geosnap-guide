# Quickstart


the `Community` class is geosnap’s central data construct that holds space-time neighborhood data.  
You can create a `Community` from geosnap’s built-in data by passing a set of fips codes to a
constructor method

```python
from geosnap.data import Community
dc = Community.from_census(state_fips='11')
```

Using the `.from_census` constructor, you’ll get 30 years of census tract data in their original
boundaries with over a hundred commonly used demographic and socioeconomic variables.
Data are stored as a long-form geodataframe under the `gdf` attribute

```python
dc.gdf.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geoid</th>
      <th>geometry</th>
      <th>median_contract_rent</th>
      <th>median_home_value</th>
      <th>median_household_income</th>
      <th>median_income_asianhh</th>
      <th>median_income_blackhh</th>
      <th>median_income_hispanichh</th>
      <th>median_income_whitehh</th>
      <th>n_age_5_older</th>
      <th>...</th>
      <th>p_unemployment_rate</th>
      <th>p_vacant_housing_units</th>
      <th>p_veterans</th>
      <th>p_vietnamese_persons</th>
      <th>p_white_over_60</th>
      <th>p_white_over_65</th>
      <th>p_white_under_15</th>
      <th>p_widowed_divorced</th>
      <th>per_capita_income</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>53214</th>
      <td>11001001600</td>
      <td>POLYGON ((-77.02680206298828 38.98410034179688...</td>
      <td>477.0</td>
      <td>285100.0</td>
      <td>75252.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.742191e+70</td>
      <td>...</td>
      <td>0.0</td>
      <td>2.58</td>
      <td>1.028308e+08</td>
      <td>0.00</td>
      <td>3.159920e+25</td>
      <td>4.999423e+17</td>
      <td>1.378187e+24</td>
      <td>0.0</td>
      <td>32166.0</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>53215</th>
      <td>11001001500</td>
      <td>POLYGON ((-77.05280303955078 38.98649978637695...</td>
      <td>1001.0</td>
      <td>366000.0</td>
      <td>79681.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.025723e+72</td>
      <td>...</td>
      <td>0.0</td>
      <td>3.38</td>
      <td>7.095389e+07</td>
      <td>0.23</td>
      <td>6.529311e+30</td>
      <td>1.483617e+23</td>
      <td>6.816417e+33</td>
      <td>0.0</td>
      <td>36452.0</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>53216</th>
      <td>11001001701</td>
      <td>POLYGON ((-77.02660369873047 38.97769927978516...</td>
      <td>429.0</td>
      <td>135600.0</td>
      <td>34420.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.918716e+64</td>
      <td>...</td>
      <td>0.0</td>
      <td>3.89</td>
      <td>8.990532e+05</td>
      <td>0.10</td>
      <td>1.184601e+14</td>
      <td>1.285720e+10</td>
      <td>8.476736e+15</td>
      <td>0.0</td>
      <td>17782.0</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>53217</th>
      <td>11001001801</td>
      <td>POLYGON ((-77.02660369873047 38.97769927978516...</td>
      <td>1001.0</td>
      <td>0.0</td>
      <td>77197.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.084115e+31</td>
      <td>...</td>
      <td>0.0</td>
      <td>10.00</td>
      <td>5.229000e+01</td>
      <td>0.00</td>
      <td>1.450982e+11</td>
      <td>1.437909e+08</td>
      <td>1.321830e+14</td>
      <td>0.0</td>
      <td>14679.0</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>53218</th>
      <td>11001001702</td>
      <td>POLYGON ((-77.00859832763672 38.97000122070312...</td>
      <td>514.0</td>
      <td>129300.0</td>
      <td>42661.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.210494e+62</td>
      <td>...</td>
      <td>0.0</td>
      <td>3.96</td>
      <td>7.219278e+04</td>
      <td>0.04</td>
      <td>4.438992e+13</td>
      <td>2.147213e+10</td>
      <td>2.352939e+17</td>
      <td>0.0</td>
      <td>20468.0</td>
      <td>1990</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 195 columns</p>
</div>

you can create a [geodemographic typology](https://en.wikipedia.org/wiki/Geodemography) using
classic clustering methods on the `Community`

```python
dc = dc.cluster(method='kmeans', n_clusters=6, columns=['p_unemployment_rate', 'per_capita_income'] )
dc.gdf[dc.gdf.year==2000].plot(column='kmeans')
```

<p align="center">
<img height=250 src="assets/images/output_6_1.png"/>
</p>

you can create a
[regionalization](https://www.sciencedirect.com/science/article/pii/0038012181900409) using
spatially-constrained clustering methods on the `Community`

```python
dc = dc.cluster_spatial(method='spenc', n_clusters=6, columns=['p_unemployment_rate', 'per_capita_income'] )
dc.gdf[dc.gdf.year==2000].plot('spenc')
```

<p align="center">
<img height=250 src="assets/images/output_9_1.png"/>
</p>

You can also [harmonize](https://github.com/spatialucr/tobler) `Community` boundaries so that they’re
consistent over time. For example 

```python
 dc = dc.harmonize(2010, extensive_variables=["population"])
```
will create a new `Community` with population in 1990 and 2000 modeled as 2010 tract boundaries (2010 will remain unchanged). Thanks to [`tobler`](http://github.com/pysal/tobler), geosnap provides several methods for harmonization, from simple areal interpolation to model-based approaches using auxiliary data. See the [harmonization example](https://spatialucr.github.io/geosnap-guide/notebooks/03_harmonizing_community_boundaries.html) for more code samples

You can explore datasets using a prototype interactive dashboard using

```python
from geosnap.vizualize import explore
explore()
```

![](assets/images/commviz.png)

By default, the dashboard will launch with built-in census data, but if you've stored other databases, then you can exlore those as well. 

Many more visualization features coming soon
