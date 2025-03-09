# Computational Approach to Discovering Plastic Degradation Enzymes

### Introduction

#### Purpose of the Pipeline
1) Identify possible enzymes with plastic-degrading properties.
2) Identify possible enzyme combinations with synergistic enzyme-degrading properties.
3) Identify possible species with plastic-degrading properties.

Tara Oceans data analysis used for enzyme and species identification

#### Target Outputs
1) List of enzymes with potential plastic-degrading properties
2) Suggested enzyme combinations with potential synergistic plastic degradation effects
3) List of species identified with literature supported plastic-degrading relationships

#### System Requirements
All scripts use Jupyter Notebook. To run Jupyter Notebook from your browser, click here: https://jupyter.org/try. To install, follow instructions on https://jupyter.org/install.

#### Software dependencies
	- Python 3.x
	- Python libraries:
 		- numpy
   		- pandas
		- scipy
       
### To get started
#### Using Jupyter Notebook
##### Step 1: Set up Environment
1) Download and open ‘set up’ script in Jupyter Notebook. This script is taken from https://github.com/JanZrimec/Plastic_degrading_microbiome/blob/master/scripts/3_ocean_analysis.ipynb and aggregates pollution data from Tara Ocean Study into one file (pollutionData.txt).
   	- Required input files:
		- Sunagawa_TableS1.xlsx
		- tara_assemblies_parsed.csv
		- tara-assembly-sample-mapping.txt
		- tara_env_column_names.tab
		- output_pangea_sample_identifiers.tab
		- WW Marine Datashare.xlsx
		- PlasticMarinePollutionGlobalDataset_Eriksen2014.xlsx
		- Pacific_Law_plastics.txt
		- MicroplasticNumericalandMassConcentration_Goldstein2012.csv

* All required input files for set-up script can be found at https://doi.org/10.5281/zenodo.5112372

3) Run the set up script. This will generate the pollutionData file, which is required for the analysis script.
   
##### Step 2: Run Analysis Pipeline
1) Download and open ‘analysis’ script in Jupyter Notebook.
   	- Required input files include:
		- pollutionData.txt
		- Sunagawa_TableS1.xlsx
		- TARA243.KO.profile.release
		- miTAG.taxonomic.profiles.release.tsv

* All required input files for analysis can be found at https://doi.org/10.5281/zenodo.13997003

2) Run analysis script.

#### Using Python
##### Input Files
The pipeline requires two input files in TSV format:
1) Pollution Abundance File (pollution_abundance.tsv):
   	- Contains pollution abundance data.
   	- Format:
  		- sample   abundance
   		- sample1  0.5
   	 	- sample2  0.7
   	  	- ...
   	 
2) Enzyme Abundance File (enzyme_abundance.tsv):
   	- Contains enzyme abundance data.
   	- Format:
  		- Enzyme   sample1   sample2   ...
		- enzyme1  0.1       0.3       ...
		- enzyme2  0.4       0.2       ...
		- ...
##### Output Files
The pipeline generates the following output files:
1) All Correlation Results (all_enzyme_<method>_correlations.tsv)
   	- Contains correlation coefficients, t-values, p-values, and confidence intervals for all enzymes.
   	- Example
  		- Enzyme   Correlation   t_value   p_value   conf_lower   conf_upper
		- enzyme1  0.85          5.23      0.001     0.78         0.90
		- enzyme2  0.72          4.56      0.002     0.65         0.80
		- ...
    
2) Significant Correlation Results (sig_<method>_enzymes.tsv):
   	- Contains only significant correlations.
   	- Example:
  		- Enzyme   Correlation   t_value   p_value   conf_lower   conf_upper
		- enzyme1  0.85          5.23      0.001     0.78         0.90
		- ...
3) Overlapping Enzymes (enzyme_overlap.tsv)
      	- Contains enzymes that are significant in both Pearson and Spearman correlation analyses.
   	- Example:
  		- Enzyme   Pearson_Correlation   Pearson_t_value   Pearson_p_value   Pearson_conf_lower   Pearson_conf_upper   Spearman_Correlation   Spearman_t_value   Spearman_p_value   Spearman_conf_lower   Spearman_conf_upper
		- enzyme1  0.85                  5.23              0.001             0.78                 0.90                 0.83                   5.10              0.002               0.75                   0.88
		- ...
##### Usage
##### Prepare Input Files:
1) Ensure pollution_abundance.tsv and enzyme_abundance.tsv are in the correct format and located in the working directory.
2) Run the Script:
	- Execute the script in your terminal or Python environment: python enzyme_correlation_pipeline.py

### Results
The pipeline will output two files with target results:
* results.xlsx
	* contains a list of enzymes that are significantly correlated with pollution and enzyme combinations that have the most potential to produce a synergistic effect in the degradation of plastic.
* significant_species
	* contains a list of species that are significantly correlated with pollution with their identified taxa information

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
   	* Correlation Method: Change the correlation_method variable to "pearson" or "spearman":
    	* Confidence Level: Modify the confidence_level parameter in the calculate_confidence_interval function:
     	* Input File Names: Update the pollution_file and enzyme_file variables if your input files have different names or paths:

### Additional Notes
Ensure all input files are correctly formatted and placed in the working directory before running the scripts.
