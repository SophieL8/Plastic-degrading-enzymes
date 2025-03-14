# -*- coding: utf-8 -*-
"""Enzyme Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16EeTfQeBKhoOl_iZVht0OqPYgWtQENMj

# Significant enzymes
"""

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr, t
from scipy import stats
import csv

# Helper functions
def calculate_correlation(x_values, y_values, method="pearson"):
    """Calculate Pearson or Spearman correlation coefficient."""
    if method == "pearson":
        correlation_coefficient, _ = pearsonr(x_values, y_values)
    elif method == "spearman":
        correlation_coefficient, _ = spearmanr(x_values, y_values)
    else:
        raise ValueError("Method must be either 'pearson' or 'spearman'")
    return correlation_coefficient

def calculate_t_value_distribution(correlation_coefficient, degrees_of_freedom):
    """Calculate t-value and p-value for the correlation."""
    t_value = correlation_coefficient * np.sqrt(degrees_of_freedom) / np.sqrt(1 - correlation_coefficient**2)
    p_value = 2 * (1 - t.cdf(np.abs(t_value), degrees_of_freedom))  # Two-tailed test
    return t_value, p_value

def calculate_confidence_interval(correlation_coefficient, total_samples, confidence_level=0.95):
    """Calculate the confidence interval for the correlation coefficient."""
    # Fisher transformation
    z = 0.5 * np.log((1 + correlation_coefficient) / (1 - correlation_coefficient))
    standard_error = 1 / np.sqrt(total_samples - 3)

    # Critical value from normal distribution (1.96 for 95% CI)
    z_critical = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    # Confidence interval in Fisher z-space
    z_lower = z - z_critical * standard_error
    z_upper = z + z_critical * standard_error

    # Convert back to correlation coefficient using the inverse Fisher transformation
    r_lower = (np.exp(2 * z_lower) - 1) / (np.exp(2 * z_lower) + 1)
    r_upper = (np.exp(2 * z_upper) - 1) / (np.exp(2 * z_upper) + 1)

    return r_lower, r_upper

# User-defined input files
pollution_file = "pollution_abundance.tsv"
enzyme_file = "enzyme_abundance.tsv"
correlation_method = "spearman"  # Change this to "spearman" for Spearman correlation

# Load pollution abundance data
pollution_df = pd.read_csv(pollution_file, sep='\t')

# Extract x_values (pollution abundance)
x_values = pollution_df["abundance"].values
total_samples = len(x_values)

# Load enzyme abundance data, skipping first two rows
enzyme_df = pd.read_csv(enzyme_file, sep='\t', skiprows=2)

# Dictionary to store correlation coefficients
correlation_results = []

# Iterate over each row of the enzyme abundance data
for _, row in enzyme_df.iterrows():
    enzyme_name = row.iloc[0]  # First column is enzyme name
    y_values = row.iloc[1:].values  # Enzyme abundance values

    # Calculate correlation coefficient
    correlation_coefficient = calculate_correlation(x_values, y_values, method=correlation_method)
    correlation_results.append((enzyme_name, correlation_coefficient))

# Convert to DataFrame and sort by correlation in descending order
df = pd.DataFrame(correlation_results, columns=["Enzyme", "Correlation"])
df = df.sort_values(by="Correlation", ascending=False)

# Calculate t-values, p-values, and confidence intervals
degrees_of_freedom = total_samples - 2
df[['t_value', 'p_value']] = df.apply(lambda row: calculate_t_value_distribution(row['Correlation'], degrees_of_freedom), axis=1, result_type='expand')
df[['conf_lower', 'conf_upper']] = df.apply(lambda row: calculate_confidence_interval(row['Correlation'], total_samples), axis=1, result_type='expand')

# Save the results to a TSV file
output_file = f"all_enzyme_{correlation_method}_correlations.tsv"
df.to_csv(output_file, sep='\t', index=False)
print(f"{correlation_method.capitalize()} correlation results saved to {output_file}")

# Identify significant rows using Benjamini-Hochberg procedure
significant_rows = []
total_probability = 0

for _, row in df.iterrows():
    enzyme_name = row["Enzyme"]
    correlation_coefficient = row["Correlation"]
    t_value = row["t_value"]
    p_value = row["p_value"]

    if total_probability + p_value <= 1:
        significant_rows.append((enzyme_name, correlation_coefficient, t_value, p_value, row["conf_lower"], row["conf_upper"]))
        total_probability += p_value
    else:
        break

# Save significant results to a new TSV file including confidence intervals
sig_output_file = f"sig_{correlation_method}_enzymes.tsv"
sig_df = pd.DataFrame(significant_rows, columns=["Enzyme", "Correlation", "t_value", "p_value", "conf_lower", "conf_upper"])
sig_df.to_csv(sig_output_file, sep='\t', index=False)
print(f"Significant {correlation_method.capitalize()} results saved to {sig_output_file}")

# Step 1: Read the sig_pearson_enzymes.tsv file into a dictionary with additional columns
pearson_data = {}
with open('sig_pearson_enzymes.tsv', 'r') as pearson_file:
    reader = csv.reader(pearson_file, delimiter='\t')
    next(reader)  # Skip the header
    for row in reader:
        enzyme = row[0]
        correlation = float(row[1])
        t_value = float(row[2])
        p_value = float(row[3])
        conf_lower = float(row[4])
        conf_upper = float(row[5])
        # Store the additional data in the dictionary
        pearson_data[enzyme] = {
            'correlation': correlation,
            't_value': t_value,
            'p_value': p_value,
            'conf_lower': conf_lower,
            'conf_upper': conf_upper
        }

# Step 2: Read the sig_spearman_enzymes.tsv file and find overlapping enzymes
overlap_data = []
with open('sig_spearman_enzymes.tsv', 'r') as spearman_file:
    reader = csv.reader(spearman_file, delimiter='\t')
    next(reader)  # Skip the header
    for row in reader:
        enzyme = row[0]
        spearman_correlation = float(row[1])
        spearman_t_value = float(row[2])
        spearman_p_value = float(row[3])
        spearman_conf_lower = float(row[4])
        spearman_conf_upper = float(row[5])

        # Step 3: Check if the enzyme is in both Pearson and Spearman data
        if enzyme in pearson_data:
            # Retrieve Pearson data for the overlapping enzyme
            pearson_info = pearson_data[enzyme]
            pearson_correlation = pearson_info['correlation']
            pearson_t_value = pearson_info['t_value']
            pearson_p_value = pearson_info['p_value']
            pearson_conf_lower = pearson_info['conf_lower']
            pearson_conf_upper = pearson_info['conf_upper']

            # Step 4: Store the overlapping enzyme and all correlation-related values
            overlap_data.append([
                enzyme,
                pearson_correlation, pearson_t_value, pearson_p_value, pearson_conf_lower, pearson_conf_upper,
                spearman_correlation, spearman_t_value, spearman_p_value, spearman_conf_lower, spearman_conf_upper
            ])

# Step 5: Write the overlapping enzymes and their correlation values to a new TSV file
with open('enzyme_overlap.tsv', 'w', newline='') as overlap_file:
    writer = csv.writer(overlap_file, delimiter='\t')
    writer.writerow([
        'Enzyme',
        'Pearson_Correlation', 'Pearson_t_value', 'Pearson_p_value', 'Pearson_conf_lower', 'Pearson_conf_upper',
        'Spearman_Correlation', 'Spearman_t_value', 'Spearman_p_value', 'Spearman_conf_lower', 'Spearman_conf_upper'
    ])
    for row in overlap_data:
        writer.writerow(row)

print("Overlapping enzymes saved to 'enzyme_overlap.tsv'")