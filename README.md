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
- `Get_danish_data.ipynb` - Downloads Danish voting data through an API and processes them
- `data_prep_US.ipynb` - Merges and processes US voting data
- `dataset_stats.ipynb` - Generates statistics and analysis of the datasets
- `RC_create_sparmatrix.ipynb` - Creates sparse matrices for analysis

### Analysis Files
- `avg_of_avg_newtork.ipynb` - Creates networks using inter- party average
- `intra_inter_party.ipynb` - Creates networks using intra- and inter- party agreement
- `Network_statistics.ipynb` - Computes statistic on networks (number of all edges, intra-edges and inter-edges)
- `Polarization_Calculation.ipynb` - Calculates Polarization scores
- `heat_maps_party_agreement.ipynb` - Generates heat maps for party agreement
- `Danish_opinion.ipynb` - Creates plots of danish ideology (MDS, PCA, UMAP)
- `US_opinion_plot.ipynb` - Creates plots of US ideology (MDS, PCA, UMAP)

### Data Organization
- `data/Denmark/` - Contains Danish data
- `data/USA/` - Contains US data

### Images

## Results

Results are stored in the respective `results/` directories within each country's data folder.  
