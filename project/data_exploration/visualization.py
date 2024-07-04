import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

def plot_average_value_map(
    merged: gpd.GeoDataFrame, label_and_unit: str, column: str = "Average_Value"
) -> None:
    """
    Create a map visualization of all countries
    with the average value of a specified column.

    :param merged: gpd.GeoDataFrame
        GeoDataFrame containing the merged world map and data.
    :param label_and_unit: str
        A string containing the label and unit for the legend and title.
    :param column: str, optional
        The name of the column to plot, default is "Average_Value".
    """
    label, unit = label_and_unit.split(" (")
    unit = unit.rstrip(")")

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged.plot(
        column=column,
        ax=ax,
        legend=True,
        legend_kwds={
            "label": f"{label} ({unit})",
            "orientation": "horizontal",
        },
        cmap="viridis",
        missing_kwds={"color": "lightgrey"},
    )
    plt.title(f"{label} by Country")
    plt.show()


def plot_column_over_time(
    df: pd.DataFrame, date_col: str, value_col: str, label: str, frequency: str = 'M'
) -> None:
    """
    Plot the specified column aggregated by the specified frequency.

    :param df: pd.DataFrame
        DataFrame containing the data.
    :param date_col: str
        The name of the column containing date information.
    :param value_col: str
        The name of the column containing the values to be plotted.
    :param label: str
        The label for the data to be used in the plot title and ylabel.
    :param frequency: str, optional
        The frequency for resampling the data (e.g., 'M' for monthly, 'Y' for yearly). Defaults to 'M'.
    """

    df_copy = df.copy()

    df_copy[date_col] = pd.to_datetime(df_copy[date_col])

    df_copy.set_index(date_col, inplace=True)

    resampled_data = df_copy[value_col].resample(frequency).mean()
    
    plt.figure(figsize=(10, 6))
    resampled_data.plot()
    plt.title(f"{label} Over Time")
    plt.xlabel("Date")
    plt.ylabel(f"Average {label}")
    plt.grid(True)
    plt.show()



def plot_average_change(avg_change: pd.Series, label: str) -> None:
    """
    Plot the average change over the years.

    :param avg_change: pd.Series
        Series containing the average change for each year.
    :param label: str
        The label for the data to be used in the plot title and ylabel.
    """
    plt.figure(figsize=(10, 6))
    avg_change.plot()
    plt.title(f"Average Worldwide {label} Change Over Years")
    plt.xlabel("Year")
    plt.ylabel(f"Average {label} Change")
    plt.grid(True)
    plt.show()


def plot_scatter(x, y, x_label, y_label, title, alpha=0.5, figsize=(10, 6), grid=True):
    """
    Create a scatter plot with the given data and annotations.

    :param x: array-like
        Data for the x-axis.
    :param y: array-like
        Data for the y-axis.
    :param x_label: str
        Label for the x-axis.
    :param y_label: str
        Label for the y-axis.
    :param title: str
        Title of the plot.
    :param alpha: float, optional (default=0.5)
        Transparency level of the points.
    :param figsize: tuple, optional (default=(10, 6))
        Size of the figure.
    :param grid: bool, optional (default=True)
        Whether to display grid lines.
    """
    plt.figure(figsize=figsize)
    plt.scatter(x, y, alpha=alpha)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if grid:
        plt.grid(True)
    plt.show()