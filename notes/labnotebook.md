# Lab Notebook 

Store ongoing thoughts and observations here in reverse chronological order. 


### 11/05/21

First few questions from grad project, 
for the `daily_reports` dataset: 
* Data Sampling and Collection
    * How were the data collected?
    * Was there any potential bias introduced in the sampling process?

Lots of data is self reported by the states/counties themselves. Different locations may start/stop reporting different metrics (e.g. recovered, active cases). Early reporting states may have had higher case numbers or taken the pandemic more seriously early on. 

* Data Cleaning
    * What type of data are you currently exploring?
    * What is the granularity of the data?
    * What does the distribution of the data look like? Are there any outliers? Are there any missing or invalid entries?

For province_state values, there are 9 non-states. Several territories but also the cruise ships Diamon Princess and Grand Princess are reported separately. Their data looks uniform in time so likely not useful as a timeseries. Similarly the Grand Princess has 1-2 unique values per (non-date) column. There is also a 'Recovered' Province_State value with its own unique UID but unclear what it belongs to/refers to.  

Granularity: Data is reported per state/province and typically once per day, with varied start times. 

* Exploratory Data Analysis
    * Is there any correlation between the variables you are interested in exploring?
    * How would you cleanly and accurately visualize the relationship among variables?

### 11/03/21 

Goals: initial exploration of COVID datasets 1 and 2. maybe decide on some which to explore and some preliminary questions to ask. 

Converted cumulative death data for CA covid daily cases into delta (daily counts) and then applied a rolling average to plot the smoothed daily death counts for CA. Created method for making future rolling averages 

Questions: 

Create a model to predict covid cases (by...state? zip? what level of detail?)

explore other datasets and look at causes of death. Maybe make a model for predicting death or type of death based on features? 