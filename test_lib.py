import os
import pandas as pd
from lib import (
    load_dataset,
    calculate_statistics,
    create_histogram,
    generate_visualizations,
)

# Define test file url
file_url = "https://raw.githubusercontent.com/nogibjj/yijia_ids706_miniProj3/main/rdu-weather-history.csv"


def test_load_data():
    """Function to test the load_data function."""
    data = load_dataset(file_url)
    assert not data.empty, "Loaded data should not be empty"
    assert isinstance(data, pd.DataFrame), "Loaded data should be a DataFrame"
    assert (
        "Temperature Minimum" in data.columns
    ), "Expected column 'Temperature Minimum' not found"


def test_calculate_statistics():
    """Function to test the calculate_statistics function."""
    data = load_dataset(file_url)
    stats = calculate_statistics(data)

    # Assert statements to check the calculated values against the expected values
    assert (
        abs(stats.at["mean", "Temperature Minimum"] - 44.225166) < 1e-6
    ), "Mean of Temperature Minimum is incorrect"
    assert (
        abs(stats.at["median", "Temperature Minimum"] - 45.000000) < 1e-6
    ), "Median of Temperature Minimum is incorrect"
    assert (
        abs(stats.at["std_dev", "Temperature Minimum"] - 14.538763) < 1e-6
    ), "Standard deviation of Temperature Minimum is incorrect"

    assert (
        abs(stats.at["mean", "Temperature Maximum"] - 66.966887) < 1e-6
    ), "Mean of Temperature Maximum is incorrect"
    assert (
        abs(stats.at["median", "Temperature Maximum"] - 70.000000) < 1e-6
    ), "Median of Temperature Maximum is incorrect"
    assert (
        abs(stats.at["std_dev", "Temperature Maximum"] - 14.719337) < 1e-6
    ), "Standard deviation of Temperature Maximum is incorrect"

    assert (
        abs(stats.at["mean", "Precipitation"] - 0.127020) < 1e-6
    ), "Mean of Precipitation is incorrect"
    assert (
        abs(stats.at["median", "Precipitation"] - 0.000000) < 1e-6
    ), "Median of Precipitation is incorrect"
    assert (
        abs(stats.at["std_dev", "Precipitation"] - 0.327184) < 1e-6
    ), "Standard deviation of Precipitation is incorrect"


def test_create_histogram():
    """Function to test the create_histogram function."""
    data = load_dataset(file_url)
    histogram_path = "temperature_minimum_distribution.png"
    create_histogram(data, "Temperature Minimum", histogram_path)
    assert os.path.isfile(histogram_path), "Histogram file should be created"
    os.remove(histogram_path)  # Cleanup after test


def test_generate_visualizations():
    """Test the generate_visualizations function."""
    image_paths = generate_visualizations(file_url)
    for path in image_paths:
        assert os.path.isfile(path), f"Visualization file {path} should be created"
        os.remove(path)  # Cleanup after test


if __name__ == "__main__":
    test_load_data()
    test_calculate_statistics()
    test_create_histogram()
    test_generate_visualizations()
    print("All tests passed.")
