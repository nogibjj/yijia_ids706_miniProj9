import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(filepath):
    data = pd.read_csv(filepath)
    return data


def calculate_statistics(data):
    """Calculate mean, median, and standard deviation for selected columns."""
    selected_columns = [
        "Temperature Minimum",
        "Temperature Maximum",
        "Precipitation",
        "Snowfall",
        "Snow Depth",
        "Avgerage Wind Speed",
    ]

    data = data[selected_columns]

    stats = {
        "mean": data.mean(),
        "median": data.median(),
        "std_dev": data.std(),
    }
    return pd.DataFrame(stats).T


def create_histogram(data, column, filepath):
    """Generate a histogram for the specified column and save it."""
    plt.figure(figsize=(10, 5))
    plt.hist(data[column], bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(filepath)
    plt.close()


def generate_visualizations(filepath):
    """Generate visualizations for specific columns and save them as PNG files."""
    data = load_dataset(filepath)

    # Create and save histograms for selected columns
    columns = ["Temperature Maximum", "Temperature Minimum", "Precipitation"]
    image_paths = []
    for column in columns:
        image_path = f"{column.lower().replace(' ', '_')}_distribution.png"
        create_histogram(data, column, image_path)
        image_paths.append(image_path)

    return image_paths
