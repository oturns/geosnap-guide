<p align="center">
<img height=200  src="assets/images/geosnap_long.png" alt="geosnap"/>
</p>

<h1 align="center" style="margin-top:-10px">The Geospatial Neighborhood Analysis Package</h1> 


`geosnap` makes it easier to explore, model, analyze, and visualize the social and spatial dynamics
of neighborhoods.
Neighborhoods are important for a wide variety of reasons, but they’re hard to study
because of some long-standing challenges, including that

- there is no formal definition of a
  [“neighborhood”](https://www.cnu.org/publicsquare/2019/01/29/once-and-future-neighborhood) so
  identifying and modeling them is frought with uncertainty
- many different physical and social data can characterize a neighborhood (e.g. its
  proximity to the urban core, its share of residents with a high school education, or the
  median price of its apartments) so there are countless ways to model neighborhoods by
  choosing different subsets of attributes
- conceptually, neighborhoods evolve through both space and time, meaning their
  socially-construed boundaries can shift over time, as can their demographic makeup.
- geographic tabulation units change boundaries over time, meaning the raw data are
  aggregated to different areal units at differerent points in time.

To address these challenges,`geosnap` provides a suite of tools for creating socio-spatial
datasets, harmonizing those datasets into consistent set of time-static boundaries,
modeling bespoke neighborhoods and prototypical neighborhood types, and modeling
neighborhood change using classic and spatial statistical methods.
It also provides a set of static and interactive visualization tools to help you display
and understand the critical information at each step of the process.

**Batteries Included:**
`geosnap` comes packed with 30 years of census data, thanks to [quilt](https://quiltdata.com/), so you
can get started modeling neighborhoods in the U.S. immediately.
But you’re not just limited to the data provided with the package. `geosnap`
works with any data you provide, any place in the world.

<p align="center">
<img width=75% src='assets/images/Washington-Arlington-Alexandria_DC-VA-MD-WV.gif' alt='DC Transitions' style=' display: block; margin-left: auto; margin-right: auto;'/>
</p>


## Installation

The recommended method for installing geosnap is with
[anaconda](https://www.anaconda.com/download/). To get started with the development version,
clone this repository or download it manually then `cd` into the directory and run the
following commands:

```bash
conda env create -f environment.yml
conda activate geosnap 
python setup.py develop
```

This will download the appropriate dependencies and install geosnap in its own conda
environment.

## Development

geosnap development is hosted on [github](https://github.com/spatialucr/geosnap)

## Bug reports

To search for or report bugs, please see geosnap’s
[issues](http://github.com/spatialucr/geosnap/issues)

## License information

See the file “LICENSE.txt” for information on the history of this software, terms &
conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

## Citation

For a generic citation of geosnap, we recommend the following: 

```latex
@misc{Knaap2019,
author = {Knaap, Elijah and Kang, Wei and Rey, Sergio and Wolf, Levi John and Cortes, Renan Xavier and Han, Su},
doi = {10.5281/ZENODO.3526163},
title = {{geosnap: The Geospatial Neighborhood Analysis Package}},
url = {https://zenodo.org/record/3526163},
year = {2019}
}
```
If you need to cite a specific release of the package, please find the appropriate version on [Zenodo](https://zenodo.org/record/3526163)

## Funding


<img src="assets/images/nsf_logo.jpg" width=100 /> This project is supported by NSF Award #1733705,
[Neighborhoods in Space-Time Contexts](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1733705&HistoricalAwards=false)
