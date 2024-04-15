import os
import json
import re
import matplotlib.pyplot as plt
import matplotlib

def compare_json_files(folder_paths, interesting_queries):
    matplotlib.rcParams.update({'font.size': 22})
    folder_values = {}
    folder_names = []

    for folder_path, folder_label in folder_paths:
        files = os.listdir(folder_path)
        folder_names.append(folder_label)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            if file_name.endswith('.json') and file_name in interesting_queries:
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    results = data['results'][0]
                    mean_value = results['mean']

                    if folder_label in folder_values:
                        folder_values[folder_label].append(mean_value)
                    else:
                        folder_values[folder_label] = [mean_value]

    bar_width = 1 / len(folder_values)
    margin = 0.05
    bar_width = bar_width - margin
    hatches = ['//', 'xx', '\\\\', '..']

    for i in range(0, len(folder_values)):
        folder_name = folder_names[i]
        folder_value = folder_values[folder_name]
        x_values = range(0, len(folder_value))

        x_values = [float(x_value) + (-1 + i * bar_width) for x_value in x_values]
            
        plt.bar(x_values, folder_value, bar_width, color='lightgrey', alpha=0.5, label=folder_name, hatch=hatches[i])

    interesting_queries = [query.replace('.json', '') for query in interesting_queries]

    plt.xlabel('Query')
    plt.ylabel('Mean Value (s)')
    plt.title('Run Time Comparison')
    plt.xticks([i - ((bar_width + (margin * (len(folder_values)))) /2) - 0.5 for i in range(len(interesting_queries))], interesting_queries, rotation=45, ha='right')
    plt.legend(title="Implementations")
    plt.tight_layout()
    plt.show()

interesting_queries = ["10c.json", "28b.json", "3b.json"]

# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/naiv_5_percent/indexes", "Naive 5%"),
#     ("test-results/naiv_1_percent/indexes", "Naive 1%")
# ]

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/naiv_5_percent/histograms_and_indexes", "Naive 5%"),
#     ("test-results/naiv_1_percent/histograms_and_indexes", "Naive 1%")
# ]



# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/upper_bound_4_levels_incremental_0_2/indexes", "Upper Bound incr=0.2"),
#     ("test-results/upper_bound_4_levels_incremental_0_15/indexes", "Upper Bound incr=0.15"),
#     ("test-results/upper_bound_4_levels_incremental_0_1/indexes", "Upper Bound incr=0.1")
# ]

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/upper_bound_4_levels_incremental_0_2/histograms_and_indexes", "Upper Bound incr=0.2"),
#     ("test-results/upper_bound_4_levels_incremental_0_15/histograms_and_indexes", "Upper Bound incr=0.15"),
#     ("test-results/upper_bound_4_levels_incremental_0_1/histograms_and_indexes", "Upper Bound incr=0.1")
# ]




# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.2 decr=0.1"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075/indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.15 decr=0.075"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.1 decr=0.05")
# ]

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/histograms_and_indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.2 decr=0.1"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075/histograms_and_indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.15 decr=0.075"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/histograms_and_indexes", "Bounding Box alpha=0.5 beta=0.4 gamma=0.1 incr=0.1 decr=0.05")
# ]



folder_paths = [
    ("test-results/original/indexes", "Original"),
    ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1/indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.2 decr=0.1"),
    ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075/indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.15 decr=0.075"),
    ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05/indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.1 decr=0.05")
]

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1/histograms_and_indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.2 decr=0.1"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075/histograms_and_indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.15 decr=0.075"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05/histograms_and_indexes", "Bounding Box alpha=0.7 beta=0.2 gamma=0.1 incr=0.1 decr=0.05")
# ]

compare_json_files(folder_paths, interesting_queries)
