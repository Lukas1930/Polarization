# Political Polarization Analysis

This project analyzes political polarization by examining voting data from Denmark and the United States.

---

## Setup

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

### Data Collection & Preparation

| File | Description |
|------|-------------|
| `Get_danish_data.ipynb` | Downloads and processes Danish voting data via API |
| `data_prep_US.ipynb` | Merges and prepares US voting data |
| `dataset_stats.ipynb` | Generates descriptive statistics and data overview |
| `RC_create_sparmatrix.ipynb` | Creates sparse matrices for network analysis |

---

### 📊 Analysis Notebooks

| File | Description |
|------|-------------|
| `avg_of_avg_newtork.ipynb` | Builds party networks using inter-party averages |
| `intra_inter_party.ipynb` | Builds networks based on intra/inter-party agreement |
| `Network_statistics.ipynb` | Computes network statistics (edge counts, intra/inter-edge ratios) |
| `Polarization_Calculation.ipynb` | Calculates polarization scores using various methods |
| `heat_maps_party_agreement.ipynb` | Visualizes party agreement via heat maps |
| `Danish_opinion.ipynb` | Visualizes Danish ideology (MDS, PCA, UMAP) |
| `US_opinion_plot.ipynb` | Visualizes US ideology (MDS, PCA, UMAP) |
| `Modules/` | Contains polarization calculation logic (from Hoffman et al.) |

---

### Data Directory

```
data/
├── Denmark/
│   ├── Raw/                     # Prepared Danish voting and member data
│   ├── avg_party/               # Networks using inter-party average
│   │   └── results/             # Dimensionality reduction and polarization scores
│   ├── intra_inter_part/       # Networks using intra/inter-party agreement
│   │   └── results/             # Dimensionality reduction and polarization scores
│   └── ...                      # Additional politician and voting metadata
│
├── USA/
│   ├── Raw/                     # Raw US voting/member data
│   ├── Filtered/                # Cleaned and merged datasets
│   ├── avg_party/               # Inter-party average network data
│   │   └── results/             # Dimensionality reduction and polarization scores
│   ├── intra_inter_part/       # Intra/inter-party agreement networks
│   │   └── results/             # Dimensionality reduction and polarization scores
│   ├── Dwnominate/              # Dwnominate model output and results
│   └── Sparsematrix/            # Sparse matrices used in Dwnominate analysis
```

---

### Visuals

- `Images/` – Contains all generated network diagrams, ideological plots, and heat maps used in the analysis.
