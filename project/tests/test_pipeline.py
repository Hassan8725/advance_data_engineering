import pytest
import pandas as pd
from pathlib import Path
from etl_pipeline.extractor import extract_csv
from etl_pipeline.transform import delete_columns, standardize_date_column, rename_year_columns
from etl_pipeline.loader import load_df_to_sqlite

# Mock data for testing
mock_data = {
    "Annual_Surface_Temperature_Change": {
        "url": "https://opendata.arcgis.com/datasets/4063314923d74187be9596f10d034914_0.csv",
        "columns_to_delete": [
            "ObjectId", "ISO2", "Indicator", "Unit", "Source", "CTS_Code", "CTS_Name", 
            "CTS_Full_Descriptor", "F1961", "F1962", "F1963", "F1964", "F1965", 
            "F1966", "F1967", "F1968", "F1969", "F1970", "F1971", "F1972", "F1973", 
            "F1974", "F1975", "F1976", "F1977", "F1978", "F1979", "F1980", "F1981", 
            "F1982", "F1983", "F1984", "F1985", "F1986", "F1987", "F1988", "F1989", 
            "F1990", "F1991", "F2021", "F2022"
        ],
        "rename_year_columns": True,
    },
    "World_Monthly_CO2_Concentrations": {
        "url": "https://opendata.arcgis.com/datasets/9c3764c0efcc4c71934ab3988f219e0e_0.csv",
        "columns_to_delete": [
            "ObjectId", "ISO2", "ISO3", "Indicator", "Source", "CTS_Code", "CTS_Name", "CTS_Full_Descriptor"
        ],
        "date_column": "Date",
    },
    "Change_in_Mean_Sea_Levels": {
        "url": "https://opendata.arcgis.com/datasets/b84a7e25159b4c65ba62d3f82c605855_0.csv",
        "columns_to_delete": [
            "ObjectId", "ISO2", "ISO3", "Indicator", "Unit", "Source", "CTS_Code", "CTS_Name", "CTS_Full_Descriptor"
        ],
        "date_column": "Date",
    },
    "Land_Cover_Alteration": {
        "url": "https://opendata.arcgis.com/datasets/b1e6c0ea281f47b285addae0cbb28f4b_0.csv",
        "columns_to_delete": [
            "ObjectId", "ISO2", "Source", "CTS_Code", "CTS_Name", "CTS_Full_Descriptor"
        ],
        "rename_year_columns": True,
    },
}

@pytest.fixture
def mock_df() -> pd.DataFrame:
    """Fixture for creating a mock DataFrame for testing.

    Returns:
        pd.DataFrame: A mock DataFrame.
    """
    data = {
        "ObjectId": [1, 2, 3],
        "ISO2": ["US", "CA", "MX"],
        "Indicator": ["Temp Change", "Temp Change", "Temp Change"],
        "Date": ["2020-01-01", "2020-02-01", "2020-03-01"],
        "F1961": [0.1, 0.2, 0.3],
        "F2020": [1.1, 1.2, 1.3]
    }
    return pd.DataFrame(data)

def test_extract_csv(monkeypatch, mock_df):
    """Test the extract_csv function with a mock CSV URL.

    Args:
        monkeypatch (pytest.MonkeyPatch): Pytest's monkeypatch fixture.
        mock_df (pd.DataFrame): Mock DataFrame fixture.
    """
    def mock_extract_csv(url: str) -> pd.DataFrame:
        return mock_df

    monkeypatch.setattr("etl_pipeline.extractor.extract_csv", mock_extract_csv)
    df = extract_csv(mock_data["Annual_Surface_Temperature_Change"]["url"])
    assert not df.empty

def test_delete_columns(mock_df: pd.DataFrame):
    """Test the delete_columns function with a mock DataFrame.

    Args:
        mock_df (pd.DataFrame): Mock DataFrame fixture.
    """
    df = delete_columns(mock_df, mock_data["Annual_Surface_Temperature_Change"]["columns_to_delete"])
    assert "ObjectId" not in df.columns
    assert "ISO2" not in df.columns

def test_standardize_date_column(mock_df: pd.DataFrame):
    """Test the standardize_date_column function with a mock DataFrame.

    Args:
        mock_df (pd.DataFrame): Mock DataFrame fixture.
    """
    df = standardize_date_column(mock_df, "Date")
    assert pd.api.types.is_datetime64_any_dtype(df["Date"])

def test_rename_year_columns(mock_df: pd.DataFrame):
    """Test the rename_year_columns function with a mock DataFrame.

    Args:
        mock_df (pd.DataFrame): Mock DataFrame fixture.
    """
    df = rename_year_columns(mock_df)
    assert "1961" in df.columns
    assert "2020" in df.columns
    assert "F1961" not in df.columns
    assert "F2020" not in df.columns

def test_load_df_to_sqlite(monkeypatch, tmp_path, mock_df):
    """Test the load_df_to_sqlite function with a mock DataFrame and temporary database path.

    Args:
        monkeypatch (pytest.MonkeyPatch): Pytest's monkeypatch fixture.
        tmp_path (pathlib.Path): Temporary path fixture.
        mock_df (pd.DataFrame): Mock DataFrame fixture.
    """
    db_path = tmp_path / "test.db"

    def mock_load_df_to_sqlite(db_name: Path, table_name: str, df: pd.DataFrame):
        assert db_name == db_path
        assert table_name == "Annual_Surface_Temperature_Change"
        assert not df.empty

    monkeypatch.setattr("etl_pipeline.loader.load_df_to_sqlite", mock_load_df_to_sqlite)
    load_df_to_sqlite(db_path, "Annual_Surface_Temperature_Change", mock_df)
