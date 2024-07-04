import pytest
import sqlite3
import pandas as pd
import geopandas as gpd
from data_exploration.helper import (
    fetch_table,
    prepare_data_for_maps,
    reshape_land_cover_data,
    aggregate_average_change,
)


@pytest.fixture
def mock_conn() -> sqlite3.Connection:
    """Fixture to create a mock SQLite connection for testing.

    :return: sqlite3.Connection
        Mock SQLite connection.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE test_table (ï»¿ObjectId INTEGER, ISO3 TEXT, Country TEXT,
        Climate_Influence TEXT, Unit TEXT, Indicator
        TEXT, F1961 REAL, F1962 REAL, F1963 REAL);"""
    )
    cursor.executemany(
        "INSERT INTO test_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
        [
            (
                1,
                "USA",
                "United States",
                "Influence1",
                "Unit1",
                "Indicator1",
                0.1,
                0.2,
                0.3,
            ),
            (2, "CAN", "Canada", "Influence2", "Unit1", "Indicator1", 0.4, 0.5, 0.6),
            (3, "MEX", "Mexico", "Influence3", "Unit1", "Indicator1", 0.7, 0.8, 0.9),
        ],
    )
    conn.commit()
    return conn


@pytest.fixture
def mock_df() -> pd.DataFrame:
    """Fixture to create a mock DataFrame for testing.

    :return: pd.DataFrame
        Mock DataFrame.
    """
    data = {
        "ISO3": ["USA", "CAN", "MEX", "TCA", "ARE"],
        "Country": [
            "United States",
            "Canada",
            "Mexico",
            "Turks and Caicos",
            "United Arab Emirates",
        ],
        "Climate_Influence": [
            "Influence1",
            "Influence2",
            "Influence3",
            "Influence1",
            "Influence2",
        ],
        "F1961": [0.1, 0.4, 0.7, 0.1, 0.4],
        "F1962": [0.2, 0.5, 0.8, 0.2, 0.5],
        "F1963": [0.3, 0.6, 0.9, 0.3, 0.6],
        "Unit": ["Unit1", "Unit1", "Unit1", "Unit1", "Unit1"],
        "Indicator": [
            "Indicator1",
            "Indicator1",
            "Indicator1",
            "Indicator1",
            "Indicator1",
        ],
    }
    return pd.DataFrame(data)


def test_fetch_table(mock_conn):
    """Test the fetch_table function with a mock SQLite connection.

    :param mock_conn: sqlite3.Connection
        Mock SQLite connection.
    """
    df = fetch_table(mock_conn, "test_table")
    expected_columns = [
        "ISO3",
        "Country",
        "Climate_Influence",
        "Unit",
        "Indicator",
        "F1961",
        "F1962",
        "F1963",
    ]
    assert list(df.columns) == expected_columns
    assert df.shape == (3, 8)


def test_prepare_data_for_maps(mock_df):
    """Test the prepare_data_for_maps function with a mock DataFrame.

    :param mock_df: pd.DataFrame
        Mock DataFrame fixture.
    """
    # Ensure numeric only columns are included in the calculation
    mock_df_numeric = mock_df.drop(columns=["Unit", "Indicator"])
    gdf = prepare_data_for_maps(mock_df_numeric, 3)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert "geometry" in gdf.columns
    assert "Average_Value" in gdf.columns


def test_reshape_land_cover_data(mock_df):
    """Test the reshape_land_cover_data function with a mock DataFrame.

    :param mock_df: pd.DataFrame
        Mock DataFrame fixture.
    """
    reshaped_df = reshape_land_cover_data(mock_df)
    expected_columns = ["ISO3", "Country", "F1961", "F1962", "F1963"]
    assert all(col in reshaped_df.columns for col in expected_columns)
    assert reshaped_df.shape[1] == 6  # Expected 6 due to the pivot operation


def test_aggregate_average_change(mock_df):
    """Test the aggregate_average_change function with a mock DataFrame.

    :param mock_df: pd.DataFrame
        Mock DataFrame fixture.
    """
    # Ensure numeric only columns are included in the calculation
    mock_df_numeric = mock_df.drop(columns=["Unit", "Indicator"])
    avg_change = aggregate_average_change(mock_df_numeric, 3)
    expected_avg = mock_df_numeric[["F1961", "F1962", "F1963"]].mean()
    pd.testing.assert_series_equal(avg_change, expected_avg)
