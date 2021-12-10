# COVID_project

This repo contains the files for the Grduate Project for DATA 200 at Berkeley. 

* `/analysis` contains all jupyter notebooks used for data processing, modeling, and analysis. 
    * files named `initial_*` are uncleaned initial data exploration
    * a subfolder `/analysis_figures` contains any photos included in the analysis notebooks 
* `/data` contains all initial and processed data 
* `/figures` contains all figures created in the analysis notebooks that were saved for the report (`plt.savefig` was used to save them)
* `/narrative` contains the `.tex` files used to compile the report, along with `report.pdf` which is the final write up


Since some notebooks process data and then save the output to be used in other notebooks, the data processing pipeline is included below to enable replicaton: 

1. `covid_data_processing.ipynb`, `vaccine_data_processing.ipynb`, and `weather_data_processing.ipynb` read and process the initial data 
2. `data_merge_and_eda.ipynb` combines the data _outputed_ from the above and performs some exploratory data analaysis 
3. `baseline_modeling.ipynb`, `weather_modeling.ipynb` and `death_rate_models.ipynb` perform the data analysis describe in the report using the aggregated data from the previous step 
