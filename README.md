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

### System Requirements
All scripts use Jupyter Notebook. To run Jupyter Notebook from your browser, click here: from browser. To install, follow instructions on How to Install.
Software dependencies?

### To get started
1) Download and open ‘set up’ script in Jupyter Notebook. This script is taken from https://github.com/JanZrimec/Plastic_degrading_microbiome/blob/master/scripts/3_ocean_analysis.ipynb and aggregates pollution data from Tara Ocean Study into one file (pollutionData.txt). Upload required input files to notebook:
	- Sunagawa_TableS1.xlsx
	- tara_assemblies_parsed.csv
	- tara-assembly-sample-mapping.txt
	- tara_env_column_names.tab
	- output_pangea_sample_identifiers.tab
	- WW Marine Datashare.xlsx
	- PlasticMarinePollutionGlobalDataset_Eriksen2014.xlsx
	- Pacific_Law_plastics.txt
	- MicroplasticNumericalandMassConcentration_Goldstein2012.csv

		* All required input files for set up can be found at https://doi.org/10.5281/zenodo.5112372

2) Run the set up script.

3) Download and open ‘analysis’ script in Jupyter Notebook. Required input files include:
	- pollutionData.txt
	- Sunagawa_TableS1.xlsx
	- TARA243.KO.profile.release
	- miTAG.taxonomic.profiles.release.tsv

   		* All required input files for analysis can be found at https://doi.org/10.5281/zenodo.13997003

5) Run the analysis script.

### Results
The pipeline will output two files with target results:
* results.xlsx
	* contains a list of enzymes that are significantly correlated with pollution and enzyme combinations that have the most potential to produce a synergistic effect in the degradation of plastic.
* significant_species
	* contains a list of species that are significantly correlated with pollution with their identified taxa information

### Understanding the Results
#### How to interpret the list of enzymes

Input each enzyme from list into GenomeNet's KO Databse (https://www.genome.jp/kegg/ko.html) to view the enzyme's name. Then, check literature to see if the enzyme's involvement in plastic degradation is supported

#### Insights on synergistic effects between enzymes

Input combinations of enzymes into GenomeNet's KEGG Mapper (https://www.genome.jp/kegg/mapper/color.html) to view shared pathways. If enzymes in a combination are on the same pathway, they are more likely to be able to work together and have synergy.

#### Evaluation criteria for species viability

Check literature to see if species' family involvement in plastic degradation is supported. We do not consider the species without family level information, such as "Bacteria, Deferribacteres, Deferribacteres, Deferribacterales, SAR406 clade(Marine group A), nan, GQ337094.1.1520". Here, we consider "SAR406 clade(Marine group A)" as na, since it is not some formal name of family. The same for surface 1, 2, etc.

### Parameters that can be changed

	* Change the range of accepted pollution values for the distance from the closest pollution location.
	* Change degrees of freedom when calculating t-distribution
	* Change n parameter from n=10 to desired number of matching positive values in samples
