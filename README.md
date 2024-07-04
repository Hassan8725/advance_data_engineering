<div align="center">
  <h1>Interlinked Dynamics: Exploring the Correlations between Surface Temperature, Atmospheric CO2, Sea Level Rise, and Land Cover Changes</h1>
  <img src="project/final_report_latex/pictures/co2_github.jpg" width="1000" height="250" alt="Project Logo">
</div>

<div align="center">

[![Python](https://img.shields.io/badge/python-3.11.9-blue.svg)](https://www.python.org/downloads/release/python-3119/)
[![Jayvee](https://img.shields.io/badge/jayvee-0.4.0-blue.svg)](https://pypi.org/project/jayvee/0.4.0/)
[![Continuous Integration Pipeline](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/project_test.yml/badge.svg)](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/project_test.yml)
[![pre-commit](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/pre-commit.yaml)

[![Exercise Feedback](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/exercise-feedback.yml/badge.svg)](https://github.com/Hassan8725/advance_data_engineering/actions/workflows/exercise-feedback.yml)
![](https://byob.yarr.is/Hassan8725/advance_data_engineering/score_ex1) ![](https://byob.yarr.is/Hassan8725/advance_data_engineering/score_ex2) ![](https://byob.yarr.is/Hassan8725/advance_data_engineering/score_ex3) ![](https://byob.yarr.is/Hassan8725/advance_data_engineering/score_ex4) ![](https://byob.yarr.is/Hassan8725/advance_data_engineering/score_ex5)
</div>

## Project Overview
This project investigates the interrelations between climate change variables: surface temperature, atmospheric CO2 concentrations, sea level rise, and land cover changes. The main objectives are:
1. How do changes in atmospheric CO2 concentrations correlate with changes in Sea Level Rise over time?
2. Is there a correlation between rising mean surface temperatures and Land Cover Changes?

## Data Sources
The project utilizes the following datasets:
- **Annual Surface Temperature Change**: Mean surface temperature change for 1961-2021 for each country.
- **World Monthly Atmospheric CO2 Concentrations**: Global CO2 concentrations observed monthly since 1958.
- **Change in Mean Sea Levels**: Global sea level rise observed monthly since 1993.
- **Land Cover Altering Indicator**: Changes in land cover from 1992 to 2020 for each country.

## Data Pipeline
The data pipeline consists of three main modules:
1. **Extractor**: Extracts data from URLs.
2. **Transform**: Performs necessary data transformations including deletion of useless columns and standardization of date formats.
3. **Loader**: Loads transformed data into an SQLite database.

The ETL process ensures data quality, consistency, and appropriate format alignment with research questions.

## Analysis Summary
- **Correlation between Atmospheric CO2 and Sea Level Rise**: A strong positive correlation was found, suggesting that higher CO2 levels contribute to sea level rise through thermal expansion and melting ice caps.
- **Correlation between Surface Temperature and Land Cover Changes**: No significant correlation was observed, indicating other factors might influence land cover changes.

## Conclusion
The study highlights the impact of atmospheric CO2 on sea level rise and the complex nature of land cover changes, underscoring the need for effective climate policies.

## Repository Structure
- `.github/workflows`: GitHub Actions workflows.
- `data/`: Raw and processed data files.
- `examples/`: Scripts and notebooks for running and trying out examples.
- `exercises/`: Jayvee exercises.
- `project/`: Main project folder containing modules, tests, and reports along with files for shell pipelines.
	- `etl_pipeline/`: Modules for data extraction, transformation, and loading.
	- `data_exploratory/`: Modules for all data analysis.
	- `data_report_latex/`: LaTeX code for data report.
	- `final_report_latex/`: LaTeX code for final analysis report.
	- `tests/`: Modular pytest scripts.
	- `data-report.pdf`: Data report PDF.
	- `analysis-report.pdf`: Analysis report PDF.
	- `pipeline.py`: Main script for running the data pipeline.
	- `pipeline.sh`: Shell script for running the data pipeline.
	- `test.sh`: Shell script for running tests.
	- `project-plan.md`: Project plan document.

- `.gitignore`: Specifies files and directories to be ignored by git.
- `requirements.txt`: Lists the dependencies required for the project.
- `README.md`: Project overview and instructions.

## License

The content of this project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. For more information, visit [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).

For further information and detailed data source licenses, visit [IMF Climate Data](https://climatedata.imf.org/).

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Hassan8725/advance_data_engineering.git
   ```
2. Navigate to the project directory:

   ```bash
   cd AI-FAPS_Hassan_Ahmed
   ```
3. Create and activate a virtual environment:

   ```bash
    # For Windows:
    python -m venv .venv
    venv\Scripts\activate

    # For macOS and Linux:
    python3 -m venv .venv
    source venv/bin/activate
   ```
4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Verify installation:

   ```bash
   pip list
   ```
6. Deactivate the virtual environment (optional):

   ```bash
   deactivate
   ```

## Version Control Steps:

Before Pushing into your branch update **requirements.txt** file and then commit and push using following commands.

```
pip freeze > requirements.txt

git add .
git commit -m "commit message"
git push origin branch_name

```
