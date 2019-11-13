<p align="center">
<img height=200  src="assets/images/geosnap_long.svg" alt="geosnap"/>
</p>
<h2 align="center" style="margin-top:-10px">The Geospatial Neighborhood Analysis Package</h2> 

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


## Architecture

Most interaction in geosnap happens with a `Community`, and almost all of geosnap's functionality is available as a method on a `Community` object. But when you need to use other fetures, like access data or launch an interactive visuzalization, you may need to access functions in one of geosnap's submodules.

### `geosnap` has five modules:

- **`datasets`**:   Access built-in datasets, including 30 years of census data for the USA,  and databases stored with functions from the `io` module

- **`io`**:  Ingest, create, and manipulate space-time datasets

- **`analyze`**:  Analyze and model neighborhood boundaries and spatio-temporal dynamics

- **`harmonize`**:  Harmonize neighborhood boundaries into consistent, stable units using spatial statistical
methods

- **`visualize`**:  Visualize neighborhood dynamics


## Installation

The recommended method for installing geosnap is with
[anaconda](https://www.anaconda.com/download/). 

```bash
conda install geosnap
```

## Funding

<img src="assets/images/nsf_logo.jpg" width=100 /> This project is supported by NSF Award #1733705,
[Neighborhoods in Space-Time Contexts](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1733705&HistoricalAwards=false)
