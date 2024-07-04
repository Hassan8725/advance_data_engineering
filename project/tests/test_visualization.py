import pytest
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from unittest.mock import patch
from data_exploration.visualization import (
    plot_average_value_map,
    plot_column_over_time,
    plot_average_change,
    plot_scatter,
)


@pytest.fixture
def mock_gdf() -> gpd.GeoDataFrame:
    """Fixture for creating a mock GeoDataFrame."""
    data = {
        "ISO3": ["USA", "CAN", "MEX"],
        "Average_Value": [0.1, 0.4, 0.7],
        "geometry": [
            Point(-99.1332, 19.4326),
            Point(-106.3468, 56.1304),
            Point(-102.5528, 23.6345),
        ],
    }
    return gpd.GeoDataFrame(data, crs="EPSG:4326")


@pytest.fixture
def mock_df() -> pd.DataFrame:
    """Fixture for creating a mock DataFrame."""
    data = {
        "Date": pd.date_range(start="1/1/2020", periods=6, freq="M"),
        "Value": [1, 2, 3, 4, 5, 6],
    }
    return pd.DataFrame(data)


@pytest.fixture
def mock_avg_change() -> pd.Series:
    """Fixture for creating a mock Series for average change."""
    data = [0.1, 0.2, 0.3, 0.4, 0.5]
    index = pd.Index([1961, 1962, 1963, 1964, 1965], name="Year")
    return pd.Series(data, index=index)


@patch("data_exploration.visualization.plt.show")
def test_plot_average_value_map(mock_show, mock_gdf):
    """Test the plot_average_value_map function."""
    plot_average_value_map(mock_gdf, "Average Temperature (°C)")
    mock_show.assert_called_once()


@patch("data_exploration.visualization.plt.show")
def test_plot_column_over_time(mock_show, mock_df):
    """Test the plot_column_over_time function."""
    plot_column_over_time(mock_df, "Date", "Value", "Temperature")
    mock_show.assert_called_once()


@patch("data_exploration.visualization.plt.show")
def test_plot_average_change(mock_show, mock_avg_change):
    """Test the plot_average_change function."""
    plot_average_change(mock_avg_change, "Temperature")
    mock_show.assert_called_once()


@patch("data_exploration.visualization.plt.show")
def test_plot_scatter(mock_show):
    """Test the plot_scatter function."""
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    plot_scatter(x, y, "X Label", "Y Label", "Title")
    mock_show.assert_called_once()
