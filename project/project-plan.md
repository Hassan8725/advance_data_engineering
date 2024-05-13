# Project Plan

## Title

Interlinked Dynamics: Exploring the Correlations between Surface Temperature, Atmospheric CO2, Sea Level Rise, and Land Cover Changes

## Main Questions

1. How do changes in atmospheric CO2 concentrations correlate with changes in mean surface temperature globally and regionally over the decades?
2. Can we model the predictive relationship between CO2 concentration increases and subsequent increases in surface temperature in different climatic zones?
3. What are the lag effects, if any, between spikes in CO2 levels and observable increases in average surface temperatures?
4. Is there a correlation between rising mean surface temperatures and accelerated sea level rise in specific global regions?
5. Can variations in temperature changes predict anomalies in sea level changes across different time periods?
6. What patterns emerge from mapping CO2 concentration changes and sea level changes simultaneously on a global scale?
7. Can we predict future sea level rises based on current trends in atmospheric CO2 concentrations?
8. How do changes in land cover, particularly in coastal areas, impact the local sea level changes?
9. What is the cumulative effect of land cover change and increasing atmospheric CO2 levels on regional temperature changes?
10. How do different regions adapt their land cover management to mitigate the effects of rising temperatures and CO2 levels?

## Description


This data science project aims to comprehensively analyze the interrelationships between climate change metrics—namely annual surface temperature changes, atmospheric CO2 concentrations, sea level rise, and alterations in land cover—to understand their collective impact on the global climate. Utilizing datasets spanning several decades, the project seeks to identify trends and correlations that can help predict future environmental conditions and inform policy decisions. [^r1]

The approach involves merging data from four distinct yet interconnected datasets. By examining the relationships between rising CO2 levels and surface temperatures, analyzing how these factors influence sea level changes, and assessing the impact of land cover transformations, the project aims to create a holistic view of climate dynamics. Advanced statistical models and machine learning techniques will be employed to identify patterns and predict future trends. This project not only contributes to our understanding of how different climate-related factors are interlinked but also supports the development of targeted climate resilience and mitigation strategies. [^r1]

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Annual Surface Temperature Change
* Metadata URL: https://climatedata.imf.org/datasets/4063314923d74187be9596f10d034914_0/about
* Data URL: https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv
* Data Type: CSV

This indicator presents the mean surface temperature change during the period 1961-2021, using temperatures between 1951 and 1980 as a baseline.
This data is provided by the Food and Agriculture Organization Corporate Statistical Database (FAOSTAT) and is based on publicly available GISTEMP data from the National Aeronautics and Space Administration Goddard Institute for Space Studies (NASA GISS). Annual estimates of mean surface temperature change measured with respect to a baseline climatology, corresponding to the period 1951-1980. Estimates of changes in the mean surface temperature are presented, in Degree Celsius, for the years 1961-2021 by country and for World. [^r1]

### Datasource 2: World Monthly Atmospheric Carbon Dioxide Concentrations
* Metadata URL: https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/about
* Data URL: https://opendata.arcgis.com/datasets/9c3764c0efcc4c71934ab3988f219e0e_0.csv
* Data Type: CSV

This indicator presents the concentration of carbon dioxide in the atmosphere, on a monthly and yearly basis, dating back to 1958. Levels of CO₂ concentrations are presented at the World Level. Data are reported as a dry air mole fraction defined as the number of molecules of carbon dioxide divided by the number of all molecules in air, including CO₂ itself, after water vapor has been removed. The mole fraction is expressed as parts per million (ppm). [^r1]

### Datasource 3: Change in Mean Sea Levels
* Metadata URL: https://climatedata.imf.org/datasets/b84a7e25159b4c65ba62d3f82c605855/about
* Data URL: https://opendata.arcgis.com/datasets/b84a7e25159b4c65ba62d3f82c605855_0.csv
* Data Type: CSV

This indicator gives estimates of the rise of global sea levels, based on measurements from satellite radar altimeters. These are produced by measuring the time it takes a radar pulse to make a round-trip from the satellite to the sea surface and back again. 
Change in mean sea levels, in millimeters, are estimated based on measurements of sea level from satellite radar altimeters. Time-series information is presented from 1992-12-17 to 2022-08-10, with 3/4 data points for every month. The estimates are provided for 24 regions across the world, along with a global estimate. [^r1]


### Datasource 4: Land Cover and Land Cover Altering Indicator
* Metadata URL: https://climatedata.imf.org/datasets/b1e6c0ea281f47b285addae0cbb28f4b/about
* Data URL: https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv
* Data Type: CSV

Land cover has important linkages to climate regulation. Land’s ability to sequester carbon or store (retain) carbon impacts that amount of CO2 in the atmosphere. These indicators look at changes in land cover over time, grouping land cover into those types that have climate influencing, climate regulating and climate neutral impacts.
Changes in land cover over time, grouping land cover into those types that have climate influencing, climate regulating and climate neutral impacts.
Annual estimates of land cover and Climate Altering Land Cover Index are presented at country and regional levels for the years, 1992-2020. 
Estimates of land cover are presented in thousand hectares and the Climate Altering Land Cover Index is unitless. [^r1]


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

This project is structured into six work packages, represented as [milestones in the GitHub repository]().
Each work package contains at least one issue. 

1. **Objective Definition and Data Source Selection** [[WP1]()]
    1. Define the research question [[issue]()]
    2. Locate potential data sources [[issue]()]
    3. Evaluate the identified data sources [[issue]()]
2. **Data Acquisition and Pipeline** [[WP2]()]
    1. Determine the best data storage format [[issue]()]
    2. Convert data into the chosen format [[issue]()]
    3. Data Pipeline [[issue]()]
3. **Data Exploration, Analytics and Report** [[WP3]()]
    1. Conduct exploratory data analysis and preliminary visualization [[issue]()]
    2. Create Modules: DataLoader, Pipeline, Visualizations, Models, etc [[issue]()]
    3. Perform data analysis and modeling (where necessary) [[issue]()]
    4. Address all the research questions [[issue]()]
    5. Draw conclusions form the analysis [[issue]()]
4. **Tests** [[WP4]()]
    1. Create Tests for each module [[issue]()]
5. **Continuous integration** [[WP5]()]
    1. Develop CI for Tests [[issue]()]
    2. Develop CI for Pre-Commit [[issue]()]
6. **Reporting Results** [[WP6]()]
    1. Develop visual representations [[issue]()]
    2. Enhance the repository's presentation [[issue]()]
    3. Prepare the final presentation [[issue]()]


Work packages must be completed sequentially as each one depends on the completion of all preceding ones. Dependencies within a work package are specified in the corresponding issues.
Since issues can change, the issue-ID should not be used to identify dependencies. Instead, refer to the dependency list provided in each issue.

## References and footnotes

[^r1]: [IMF:Climate_Change_Dashboard](https://climatedata.imf.org/)