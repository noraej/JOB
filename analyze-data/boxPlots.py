import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['results'][0]['mean'], data['results'][0]['stddev']

def collect_data(folder_path):
    data = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                mean, stddev = parse_json(file_path)
                data.append((mean, stddev))
    return data

def calculate_relative_stats(original_data):
    original_means = [x[0] for x in original_data]
    original_stddevs = [x[1] for x in original_data]
    
    # relative_means = np.mean(original_means)
    # relative_stddevs = np.mean(original_stddevs)
    
    # return relative_means, relative_stddevs
    total_mean = sum(original_means)
    total_stddev = np.sqrt(sum(stddev**2 for stddev in original_stddevs))
    return total_mean, total_stddev

def plot_box_plot(original_data, compare_data):
    plt.boxplot([original_data, compare_data], labels=["Original", "Other"])
    plt.title('Execution Time Distribution Comparison')
    plt.xlabel('Implementation')
    plt.ylabel('Execution Time (s)')

    plt.tight_layout()
    plt.show()

def extract_execution_times(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['results'][0]['times']

def create_box_plots(json_folders):
    #labels = ['Original', 'Naive 1%', 'Naive 5%']
    #labels = ['Original', 'UpperBound01', 'Upperbound015', 'UpperBound02']
    # labels = ['Original', 'G1BoundingBox01', 'G1BoundingBox015', 'G1BoundingBox02']
    labels = ['Original', 'G2BoundingBox01', 'G2BoundingBox015', 'G2BoundingBox02']
    #labels = ['Original', 'Bounding Box alpha=0.5 \nbeta=0.4 gamma=0.1 \nincr=0.2 decr=0.1', 'Bounding Box alpha=0.5 \nbeta=0.4 gamma=0.1 \nincr=0.15 decr=0.075', 'Bounding Box alpha=0.5 \nbeta=0.4 gamma=0.1 \nincr=0.1 decr=0.05']
    #labels = ['Original', 'Bounding Box \nincr=0.2 decr=0.1', 'Bounding Box \nincr=0.15 decr=0.075', 'Bounding Box \nincr=0.1 decr=0.05']
    #labels = ['UpperBound015', 'G1BoundingBox02']
    execution_times_combined = []
    execution_times = []
    positions = []

    for i, json_folder in enumerate(json_folders, 1):
        for root, dirs, files in os.walk(json_folder):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    execution_times.extend(extract_execution_times(file_path))
        execution_times_combined.append(execution_times)
        positions.append(i)
        execution_times = []

    plt.boxplot(execution_times_combined, positions=positions)
    plt.title('Execution Time Distribution with Histograms')
    plt.xlabel('Implementation', labelpad=20)
    plt.ylabel('Execution Time (s)')
    plt.xticks(positions, [labels[i] for i in range(0, len(json_folders))])
    plt.grid(True)
    #plt.legend(title="alpha=0.5 beta=0.4 gamma=0.1")
    #plt.legend(title="alpha=0.7 beta=0.2 gamma=0.1")
    plt.show()



if __name__ == "__main__":
    matplotlib.rcParams.update({'font.size': 22})
    original_folder = "test-results/original"
    #original_folder = "test-results/upper_bound_4_levels_incremental_0_15"
    #compare_folder = "test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_2_dec_0_1"
    #compare_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1"
    #compare_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075"
    subfolders = ["histograms_and_indexes", "indexes"]

    original_path_indexes = os.path.join(original_folder, subfolders[1])
    original_path_histograms = os.path.join(original_folder, subfolders[0])

    # compare_folder = "test-results/naiv_1_percent"
    # compare_folder2 = "test-results/naiv_5_percent"
    
    # compare_folder = "test-results/upper_bound_4_levels_incremental_0_1"
    # compare_folder2 = "test-results/upper_bound_4_levels_incremental_0_15"
    # compare_folder3 = "test-results/upper_bound_4_levels_incremental_0_2"

    # compare_folder = "test-results/upper_bound_fixed_0_1"
    # compare_folder2 = "test-results/upper_bound_fixed_0_15"
    # compare_folder3 = "test-results/upper_bound_fixed_0_2"


    # compare_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05"
    # compare_folder2 = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075"
    # compare_folder3 = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1"

    # compare_folder = "test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_1_dec_0_05"
    # compare_folder2 = "test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_15_dec_0_075"
    # compare_folder3 = "test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_2_dec_0_1"



    # compare_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05"
    # compare_folder2 = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075"
    # compare_folder3 = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1"

    compare_folder = "test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_1_dec_0_05"
    compare_folder2 = "test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_15_dec_0_075"
    compare_folder3 = "test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_2_dec_0_1"


    compare_path_indexes = os.path.join(compare_folder, subfolders[1])
    compare_path_histograms = os.path.join(compare_folder, subfolders[0])

    compare_path_indexes2 = os.path.join(compare_folder2, subfolders[1])
    compare_path_histograms2 = os.path.join(compare_folder2, subfolders[0])

    compare_path_indexes3 = os.path.join(compare_folder3, subfolders[1])
    compare_path_histograms3 = os.path.join(compare_folder3, subfolders[0])

    original_path_indexes_data = collect_data(original_path_indexes)
    original_path_histograms_data = collect_data(original_path_histograms)

    compare_path_indexes_data = collect_data(compare_path_indexes)
    compare_path_histograms_data = collect_data(compare_path_histograms)

    original_path_indexes_relative_mean, original_path_indexes_relative_stddev = calculate_relative_stats(original_path_indexes_data)
    original_path_histograms_relative_mean, original_path_histograms_relative_stddev = calculate_relative_stats(original_path_histograms_data)

    compare_path_indexes_relative_mean, compare_path_indexes_relative_stddev = calculate_relative_stats(compare_path_indexes_data)
    compare_path_histograms_relative_mean, compare_path_histograms_relative_stddev = calculate_relative_stats(compare_path_histograms_data)
        
    # plot_normal_distribution(original_path_indexes_relative_mean, original_path_indexes_relative_stddev, compare_path_indexes_relative_mean, compare_path_indexes_relative_stddev, f'Normal Distribution - {compare_path_indexes}')
    # plot_normal_distribution(original_path_histograms_relative_mean, original_path_histograms_relative_stddev, compare_path_histograms_relative_mean, compare_path_histograms_relative_stddev, f'Normal Distribution - {compare_path_histograms}')

    original_indexes_means = [x[0] for x in original_path_indexes_data]
    original_histograms_means = [x[0] for x in original_path_histograms_data]

    compare_indexes_means = [x[0] for x in compare_path_indexes_data]
    compare_histograms_means = [x[0] for x in compare_path_histograms_data]

    # plot_box_plot(original_indexes_means, compare_indexes_means)
    # plot_box_plot(original_histograms_means, compare_histograms_means)

    # indexed_folders = [original_path_indexes, compare_path_indexes]
    # indexed_folders = [original_path_indexes, compare_path_indexes, compare_path_indexes2]
    # indexed_folders = [original_path_indexes, compare_path_indexes, compare_path_indexes2, compare_path_indexes3]
    # create_box_plots(indexed_folders)

    # histogram_folders = [original_path_histograms, compare_path_histograms]
    # histogram_folders = [original_path_histograms, compare_path_histograms, compare_path_histograms2]
    histogram_folders = [original_path_histograms, compare_path_histograms, compare_path_histograms2, compare_path_histograms3]
    create_box_plots(histogram_folders)