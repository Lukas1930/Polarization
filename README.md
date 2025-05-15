# Political Polarization Analysis

This project analyzes political polarization using voting data from Denmark and the USA.

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- pandas >= 2.0.0
- networkx >= 3.1
- numpy >= 1.24.0
- scipy >= 1.10.0
- umap-learn >= 0.5.3
- matplotlib >= 3.8.0
- seaborn >= 0.13.0
- scikit-learn >= 1.4.0

## Project Structure

### Data Collection and Preparation
- `Get_danish_data.ipynb` - Downloads Danish voting data through an API
- `data_prep.ipynb` - Merges and processes US voting data
- `dataset_stats.ipynb` - Generates statistics and analysis of the datasets

### Analysis Files
- `avg_of_network.ipynb` - Calculates average network metrics and properties
- `network_statistics.ipynb` - Computes various network statistics and measures
- `polarization_calculation.ipynb` - Performs polarization analysis and calculations

### Data Organization
- `data/Denmark/` - Contains Danish voting data and analysis
- `data/USA/` - Contains US voting data and analysis

## Analysis

The project includes various analyses of political polarization:
- Intra-party and inter-party analysis
- Average party positions
- Network analysis of voting patterns
- Dimensionality reduction using UMAP

## Results

Results are stored in the respective `results/` directories within each country's data folder.  