from mylib.lib import load_dataset, calculate_statistics, generate_visualizations

file_url = "https://raw.githubusercontent.com/nogibjj/yijia_ids706_miniProj3/main/rdu-weather-history.csv"


if __name__ == "__main__":
    load_dataset(file_url)
    calculate_statistics(file_url)
    generate_visualizations(file_url)
