# Computational Approach to Discovering Plastic Degradation Enzymes

## Overview

This repository provides a computational pipeline designed to identify enzymes with plastic-degrading properties, potential synergistic enzyme combinations, and species associated with plastic degradation. The pipeline utilizes data from the Tara Oceans study to perform enzyme and species identification.

There are two main types of scripts in this repository:
1) Jupyter Notebook Scripts: specific to using Tara Oceans and Global Topsoil data for plastic degradation enzyme and specie identification.
2) Python Scripts: more generalized to be used with different datasets in the same format.

---

## Purpose of the Pipeline

The main objectives of the pipeline are to:
1. Identify enzymes with potential plastic-degrading properties.
2. Discover possible enzyme combinations that may exhibit synergistic plastic degradation effects.
3. Identify species known for their plastic-degrading properties based on available literature.

The pipeline leverages **Tara Oceans** data for enzyme and species identification.

---

## Target Outputs

The pipeline will generate the following outputs:
1. **Enzyme List**: A list of enzymes with potential plastic-degrading properties.
2. **Synergistic Enzyme Combinations**: Suggested combinations of enzymes with potential synergistic plastic degradation effects.
3. **Species List**: A list of species identified based on literature-supported plastic-degrading relationships.

---

## System Requirements

The scripts are developed to run in **Jupyter Notebook**. You can use the Jupyter Notebook environment directly from your browser: [Jupyter Online](https://jupyter.org/try). For installation, follow the instructions on the official site: [Jupyter Installation Guide](https://jupyter.org/install).

### Dependencies
- **Python 3.x**
- Required Python Libraries:
  - `numpy`
  - `pandas`
  - `scipy`
  - `csv`

---

## Getting Started

### 1. Using Jupyter Notebook scripts
### Ocean Analysis
#### Step 1: Set up the Environment
1. **Download and open the ocean setup script** in Jupyter Notebook. This script aggregates pollution measurements from the Tara Oceans study into a single file called `pollutionData.txt`.  

   #### Required Input Files:
   - `Sunagawa_TableS1.xlsx`
   - `tara_assemblies_parsed.csv`
   - `tara-assembly-sample-mapping.txt`
   - `tara_env_column_names.tab`
   - `output_pangea_sample_identifiers.tab`
   - `WW Marine Datashare.xlsx`
   - `PlasticMarinePollutionGlobalDataset_Eriksen2014.xlsx`
   - `Pacific_Law_plastics.txt`
   - `MicroplasticNumericalandMassConcentration_Goldstein2012.csv`

   All required input files can be found at: [Zenodo DOI 5112372](https://doi.org/10.5281/zenodo.5112372)

2. **Run the setup script**: This will generate the `pollutionData.txt` file, which is required for the analysis.

#### Step 2: Run the Analysis
1. **Download and open the ocean analysis script** in Jupyter Notebook. This script will perform the core analysis.
   
   #### Required Input Files for Analysis:
   - `pollutionData.txt`
   - `Sunagawa_TableS1.xlsx`
   - `TARA243.KO.profile.release`
   - `miTAG.taxonomic.profiles.release.tsv`

   All required input files can be found at: [Zenodo DOI 13997003](https://doi.org/10.5281/zenodo.13997003)

2. **Run the analysis script**. This will create files with identified significant enzymes, combinations, and species.

---

### 2. Using Python

#### Input Files

Both the enzyme and species pipeline require two input files in **TSV** format:

1. **Pollution Abundance File** (`pollution_abundance.tsv`):
   - Contains pollution abundance data.
   - **Format**:
     ```
     sample   abundance
     sample1  0.5
     sample2  0.7
     ```

2. **Enzyme Abundance File** (`enzyme_abundance.tsv`):
   - Contains enzyme abundance data.
   - **Format**:
     ```
     Enzyme   sample1   sample2   ...
     enzyme1  0.1       0.3       ...
     enzyme2  0.4       0.2       ...
     ```

#### Output Files

Both the enzyme and species pipeline generate the following output files:

1. **All Correlation Results** (`all_enzyme_<method>_correlations.tsv`): Contains correlation coefficients, t-values, p-values, and confidence intervals for all enzymes.
   - **Example Format**:
     ```
     Enzyme   Correlation   t_value   p_value   conf_lower   conf_upper
     enzyme1  0.85          5.23      0.001     0.78         0.90
     ```

2. **Significant Correlation Results** (`sig_<method>_enzymes.tsv`): Contains only significant correlations.
   - **Example Format**:
     ```
     Enzyme   Correlation   t_value   p_value   conf_lower   conf_upper
     enzyme1  0.85          5.23      0.001     0.78         0.90
     ```

3. **Overlapping Enzymes** (`enzyme_overlap.tsv`): Contains enzymes that are significant in both Pearson and Spearman correlation analyses.
   - **Example Format**:
     ```
     Enzyme   Pearson_Correlation   Pearson_t_value   Pearson_p_value   Pearson_conf_lower   Pearson_conf_upper   Spearman_Correlation   Spearman_t_value   Spearman_p_value   Spearman_conf_lower   Spearman_conf_upper
     enzyme1  0.85                  5.23              0.001             0.78                 0.90                 0.83                   5.10              0.002               0.75                   0.88
     ```

### Usage
##### Prepare Input Files:
1) Ensure pollution_abundance.tsv and enzyme_abundance.tsv are in the correct format and located in the working directory.
2) Run the Script:
	- Execute the script in your terminal or Python environment:
 		- For Enzyme Analysis script: python enzyme_analysis.py
   		- For Combination Analysis script: python combination_analysis.py
		- For Species Analysis script: python species_analysis.py 

### Results
The jupyter notebook scripts will output the following files:
* results.xlsx
	* contains a list of enzymes that are significantly correlated with pollution and enzyme combinations that have the most potential to produce a synergistic effect in the degradation of plastic.
* significant_species
	* contains a list of species that are significantly correlated with pollution with their identified taxa information

The python scripts will output the following files:
* All Correlation Results (all_enzyme_<method>_correlations.tsv):
	* Contains correlation coefficients, t-values, p-values, and confidence intervals for all enzyme-pollution pairings.
* Significant Correlation Results (sig_<method>_enzymes.tsv):
	* Contains only significant correlations based on the Benjamini-Hochberg procedure.
* Overlapping Enzymes (enzyme_overlap.tsv):
	* Contains enzymes that are significant in both Pearson and Spearman correlation analyses.

### Understanding the Results
#### Interpreting List of Enzymes

Input each enzyme from list into GenomeNet's KO Databse (https://www.genome.jp/kegg/ko.html) to view the enzyme's name. Then, check literature to see if the enzyme's involvement in plastic degradation is supported

#### Insights on synergistic effects between enzymes

Input combinations of enzymes into GenomeNet's KEGG Mapper (https://www.genome.jp/kegg/mapper/color.html) to view shared pathways. If enzymes in a combination are on the same pathway, they are more likely to be able to work together and have synergy.

#### Evaluation criteria for species viability

Check literature to see if species' family involvement in plastic degradation is supported. We do not consider the species without family level information, such as "Bacteria, Deferribacteres, Deferribacteres, Deferribacterales, SAR406 clade(Marine group A), nan, GQ337094.1.1520". Here, we consider "SAR406 clade(Marine group A)" as na, since it is not some formal name of family. The same for surface 1, 2, etc.

### Customization
You can customize the following parameters in the script:
	
	* Change the range of accepted pollution values for the distance from the closest pollution location.
 	* Change degrees of freedom when calculating t-distribution
  	* Change n parameter from n=10 to desired number of matching positive values in samples
   	* Correlation Method: Change the correlation_method variable to "pearson" or "spearman"
	* Confidence Level: Modify the confidence_level parameter in the calculate_confidence_interval function
	* Input File Names: Update the pollution_file and enzyme_file variables if your input files have different names or paths

### Additional Notes
Ensure all input files are correctly formatted and placed in the working directory before running the scripts.
