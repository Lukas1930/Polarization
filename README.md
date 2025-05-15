# Political Polarization Analysis

This project analyzes political polarization using voting data from Denmark and the USA.

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

### Data Collection and Preparation
- Get_danish_data.ipynb - Downloads Danish voting data through an API and processes them
- data_prep_US.ipynb - Merges and processes US voting data
- dataset_stats.ipynb - Generates statistics and analysis of the datasets
- RC_create_sparmatrix.ipynb - Creates sparse matrices for analysis

### Analysis Files
- avg_of_avg_newtork.ipynb - Creates networks using inter- party average
- intra_inter_party.ipynb - Creates networks using intra- and inter- party agreement
- Network_statistics.ipynb - Computes statistic on networks (number of all edges, intra-edges and inter-edges)
- Polarization_Calculation.ipynb - Calculates Polarization scores
- heat_maps_party_agreement.ipynb - Generates heat maps for party agreement
- Danish_opinion.ipynb - Creates plots of danish ideology (MDS, PCA, UMAP)
- US_opinion_plot.ipynb - Creates plots of US ideology (MDS, PCA, UMAP)
- Modules - polarization calculation code from Hoffman et al.
### Data Organization
data/
└── Denmark/
│    ├── Raw - Contains prepared Danish data
│    ├── avg_party - contains edgelists for Danish networks created using inter- party average
│        ├── results - contains the dimensionality reduction scores and polarization scores for that method
│    ├── intra_inter_part - contains edgelists for Danish networks created using inter- and intra-party agreement
│        ├── results - contains the dimensionality reduction scores and polarization scores for that method
│    └── other files containing raw information on the politicians and so on
└── USA/
    ├── Raw - Contains raw voting and member USA data
    ├── Filtered - Containes merged and prepared USA data
    ├── avg_party - contains edgelists for USA networks created using inter- party average
        ├── results - contains the dimensionality reduction scores and polarization scores for that method
    ├── intra_inter_part - contains edgelists for USA networks created using inter- and intra-party agreement
        ├── results - contains the dimensionality reduction scores and polarization scores for that method
    ├── Dwnominate - contains results of our Dwnominate attempts
    └── Sparsematrix - sparse matrices for the USA congrasses which were used in the Dwnominate attemps
  
### Images
- Images - file containing all images of networks and plots which we used in our analysis
  

