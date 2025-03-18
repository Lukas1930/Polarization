import pandas as pd
import networkx as nx
import numpy as np
import utils
import os
from modules import ps

## Code to clean and prepare the USA congress data
def clean_and_prepare_congress_data(congress, data_path="data/USA/", output_path="data/USA/"):
        # Define file names
        members_file = f"{data_path}H{congress}_members.csv"
        votes_file = f"{data_path}H{congress}_votes.csv"
        output_file = f"{output_path}H{congress}_filtered_USA_votes.csv"

        # Load datasets
        members = pd.read_csv(members_file)
        votes = pd.read_csv(votes_file)

        # Ensure icpsr is treated as an integer
        members["icpsr"] = members["icpsr"].astype("Int64")
        votes["icpsr"] = votes["icpsr"].astype("Int64")

        # Merge datasets on icpsr
        merged = votes.merge(members, on="icpsr")

        # Select relevant columns
        merged = merged[["icpsr", "state_abbrev", "party_code", "cast_code", 
                         "rollnumber", "nominate_dim1", "nominate_dim2"]]

        # Normalize `cast_code`
        merged["cast_code"] = merged["cast_code"].apply(
            lambda x: 1 if 1 <= x <= 3 else (2 if 4 <= x <= 6 else x)
        )

        # Remove invalid votes
        merged = merged[~merged["cast_code"].isin([7, 9])]

        # Save the cleaned dataset
        merged.to_csv(output_file, index=False)

        return f"✅ Successfully processed Congress {congress} and saved to {output_file}"


## Code to construct the network
def construct_congress_network(congress, data_path="data/USA/"):
    # Define file paths
    input_file = f"{data_path}H{congress}_filtered_USA_votes.csv"
    output_file = f"{data_path}H{congress}_USA_edgelist.csv"

    # Load filtered voting data
    USA_data = pd.read_csv(input_file)

    # Create necessary dictionaries
    US_PA, US_PAV, US_PAVP, US_PP = utils.dict_create(USA_data, 'icpsr', 'party_code', 'rollnumber', 'cast_code')

    # Calculate threshold and interaction edges
    U_thres = np.average(utils.calc_thres(US_PP, US_PA, US_PAV))
    USA_inter = utils.calc_inter_edges(US_PP, US_PA, US_PAV)

    # Calculate edge list
    U_edgelist = utils.edgelist_calc(US_PA, US_PAV, U_thres)
    U_edgelist = U_edgelist + USA_inter

    # Create network graph
    G = nx.Graph()
    G.add_edges_from(U_edgelist)

    # Ensure the network is fully connected
    while nx.number_connected_components(G) > 1:
        components = list(nx.connected_components(G))  # Get all components
        largest_component = max(components, key=len)  # Get the largest component
        second_largest_component = max([c for c in components if c != largest_component], key=len)

        # Find best node from each component (highest agreement)
        best_node_1 = max(largest_component, key=lambda node: len(set(US_PAV.get(node, []))))
        best_node_2 = max(second_largest_component, key=lambda node: len(set(US_PAV.get(node, []))))

        # Connect the two nodes with highest agreement
        G.add_edge(best_node_1, best_node_2)
        U_edgelist.append((best_node_1, best_node_2))

    # Save edge list to CSV
    edge_df = pd.DataFrame(U_edgelist, columns=["Source", "Target"])
    edge_df.to_csv(output_file, index=False)

    return G, f"✅ Successfully created *single* connected network for Congress {congress} and saved edge list to {output_file}"

## Code to calculate the polarization scores
def calc_pol(congress, data_path="data/USA/", edge_list_path="USA_edgelist.csv"):
    edge_df = pd.read_csv(f"{data_path}H{congress}_{edge_list_path}", delimiter=",")
    
    # Remove any rows with non-numeric values in 'Source' or 'Target' columns
    edge_df = edge_df[pd.to_numeric(edge_df['Source'], errors='coerce').notna()]
    edge_df = edge_df[pd.to_numeric(edge_df['Target'], errors='coerce').notna()]
    
    # Create the graph using the cleaned edge list
    G = nx.from_pandas_edgelist(edge_df, 'Source', 'Target')
    
    # Convert nodes to integers (if they are not already)
    G = nx.relabel_nodes(G, lambda x: int(x))  # Convert nodes to integers
    # Load the members' data
    members_df = pd.read_csv(f"{data_path}H{congress}_members.csv")

    # Drop rows where nominate_dim1 is missing (NaN)
    members_df = members_df.dropna(subset=["nominate_dim1"])

    # Convert ICPSR to integer
    members_df["icpsr"] = members_df["icpsr"].astype(int)

    # Create a dictionary of opinions {icpsr: nominate_dim1}
    opinions_x = dict(zip(members_df["icpsr"], members_df["nominate_dim1"]))

    # Filter the opinions dictionary to ensure it only contains nodes in the graph
    opinions = {node: opinions_x[node] for node in G.nodes if node in opinions_x}

    # Normalize opinions between -1 and 1 using Min-Max Scaling
    min_opinion = min(opinions.values())
    max_opinion = max(opinions.values())
    
    opinions = {
        k: 2 * (v - min_opinion) / (max_opinion - min_opinion) - 1
        for k, v in opinions.items()
    }

    # Now calculate polarization using the 'ps.ge()' function
    pol_score = ps.ge(opinions, {}, G)
    
    return pol_score
    