# Computational Approach to Discovering Plastic Degradation Enzymes

## The repository contains scripts used to produce the results and figures. All files used in the scripts are available at 
### Introduction
#### Purpose of the Pipeline
1) Identify possible enzymes with plastic-degrading properties.
2) Identify possible enzyme combinations with synergistic enzyme-degrading properties.
3) Identify possible species with plastic-degrading properties.

Tara Oceans data analysis used for enzyme and species identification

Target Outputs
1) List of enzymes with potential plastic-degrading properties
2) Suggested enzyme combinations with potential synergistic plastic degradation effects
3) List of species identified with literature supported plastic-degrading relationships

### System Requirements
All scripts use Jupyter Notebook. To run Jupyter Notebook from your browser, click here: from browser. To install, follow instructions on How to Install.
Software dependencies?

### To get started
Download and open ‘set up’ script in Jupyter Notebook. This script follows Zrimec et. al 2021 and collects data from Tara Ocean Study. Required input files include:
Sunagawa_TableS1.xlsx
Tara_assemblies_parsed.csv

	* All files can be found through Zenodo: LINK
Download and open ‘analysis’ script in Jupyter Notebook. Required input files include:
pollutionData.txt
Run ‘analysis’ script.

### Results
Output Data Format will be a ‘.xlsx’
The pipeline will output the following files:
Each file will contain:
Enzyme suggestions
Combination effectiveness ratings
Species identification details

### Understanding the Results
How to interpret enzyme properties
Insights on synergistic effects between enzymes
Evaluation criteria for species viability

### Parameters
Change the range of accepted pollution values for the distance from the closest pollution location.
Change degrees of freedom when calculating t-distribution
Change n parameter from n=10 to desired number of matching positive values in samples

### More Resources
Research papers on plastic degradation
Relevant online forums and communities
Additional tools for enzyme analysis
