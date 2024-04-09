# import os
# import json

# def compare_json_files(original_folder, upper_bound_folder, output_file):
#     with open(output_file, 'w') as md_file:
#         # Write header to the Markdown file
#         md_file.write("# JSON File Comparison\n\n")
        
#         # Get list of files in the original folder
#         original_files = os.listdir(original_folder)
        
#         for file_name in original_files:
#             original_file_path = os.path.join(original_folder, file_name)
#             upper_bound_file_path = os.path.join(upper_bound_folder, file_name)
            
#             # Check if the file exists in both folders
#             if os.path.isfile(original_file_path) and os.path.isfile(upper_bound_file_path):
#                 # Check if the file has a JSON extension
#                 if file_name.endswith('.json'):
#                     # Read data from both JSON files
#                     with open(original_file_path, 'r') as original_file, open(upper_bound_file_path, 'r') as upper_bound_file:
#                         original_data = json.load(original_file)
#                         upper_bound_data = json.load(upper_bound_file)
                        
#                         # Extract mean, median, min, and max values from both files
#                         original_results = original_data['results'][0]
#                         upper_bound_results = upper_bound_data['results'][0]
                        
#                         original_mean = original_results['mean']
#                         upper_bound_mean = upper_bound_results['mean']
                        
#                         original_median = original_results['median']
#                         upper_bound_median = upper_bound_results['median']
                        
#                         original_min = original_results['min']
#                         upper_bound_min = upper_bound_results['min']
                        
#                         original_max = original_results['max']
#                         upper_bound_max = upper_bound_results['max']
                        
#                         # Calculate differences
#                         diff_mean = original_mean - upper_bound_mean
#                         diff_median = original_median - upper_bound_median
#                         diff_min = original_min - upper_bound_min
#                         diff_max = original_max - upper_bound_max
                        
#                         # Write comparison to the Markdown file
#                         md_file.write(f"## Comparison for file '{file_name}':\n\n")
#                         md_file.write("| Metric | Original | Upper Bound | Difference |\n")
#                         md_file.write("|--------|----------|-------------|------------|\n")
#                         md_file.write(f"| Mean   | {original_mean}  | {upper_bound_mean}    | {diff_mean}    |\n")
#                         md_file.write(f"| Median | {original_median}  | {upper_bound_median}    | {diff_median}    |\n")
#                         md_file.write(f"| Min    | {original_min}  | {upper_bound_min}    | {diff_min}    |\n")
#                         md_file.write(f"| Max    | {original_max}  | {upper_bound_max}    | {diff_max}    |\n\n")

# # Paths to the folders containing the JSON files and the output Markdown file
# original_folder = "runs/original"
# upper_bound_folder = "runs/upper-bound"
# output_file = "comparison.md"

# # Call the function to compare JSON files and write results to the Markdown file
# compare_json_files(original_folder, upper_bound_folder, output_file)

import os
import json
import re
import matplotlib.pyplot as plt

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def compare_json_files(original_folder, upper_bound_folder, output_file):
    # Lists to store file names and corresponding mean values
    file_names = []
    original_means = []
    upper_bound_means = []

    # Get list of files in the original folder
    original_files = os.listdir(original_folder)

    for file_name in original_files:
        original_file_path = os.path.join(original_folder, file_name)
        upper_bound_file_path = os.path.join(upper_bound_folder, file_name)

        # Check if the file exists in both folders
        if os.path.isfile(original_file_path) and os.path.isfile(upper_bound_file_path):
            # Check if the file has a JSON extension
            if file_name.endswith('.json'):
                # Read data from both JSON files
                with open(original_file_path, 'r') as original_file, open(upper_bound_file_path, 'r') as upper_bound_file:
                    original_data = json.load(original_file)
                    upper_bound_data = json.load(upper_bound_file)

                    # Extract mean values from both files
                    original_results = original_data['results'][0]
                    upper_bound_results = upper_bound_data['results'][0]

                    original_mean = original_results['mean']
                    upper_bound_mean = upper_bound_results['mean']

                    # Append file name and mean values to lists
                    file_names.append(file_name.replace('.json', ''))
                    original_means.append(original_mean)
                    upper_bound_means.append(upper_bound_mean)

    # Sort file names based on natural sorting order
    sorted_indices = sorted(range(len(file_names)), key=lambda k: natural_sort_key(file_names[k]))
    sorted_file_names = [file_names[i] for i in sorted_indices]
    sorted_original_means = [original_means[i] for i in sorted_indices]
    sorted_upper_bound_means = [upper_bound_means[i] for i in sorted_indices]

    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(sorted_file_names)), sorted_original_means, color='b', alpha=0.5, label='Upper bound incr=0.15')
    plt.bar(range(len(sorted_file_names)), sorted_upper_bound_means, color='r', alpha=0.5, label='Bounding box alpha=0.5 beta=0.4 gamma=0.1 incr=0.15 decr=0.075')
    plt.xlabel('Query')
    plt.ylabel('Mean Value (s)')
    plt.title('Run Time Comparison')
    plt.xticks(range(len(sorted_file_names)), sorted_file_names, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Paths to the folders containing the JSON files and the output Markdown file
#original_folder = "test-results/original/indexes"
#original_folder = "test-results/original/histograms_and_indexes"

#original_folder = "test-results/upper_bound_4_levels_incremental_0_15/indexes"
original_folder = "test-results/upper_bound_4_levels_incremental_0_15/histograms_and_indexes"


#original_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/indexes"
#original_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/indexes"
#original_folder = "test-results/upper_bound_4_levels_incremental_0_15/indexes"
#original_folder = "test-results/upper_bound_4_levels_incremental_0_15/histograms_and_indexes"

#upper_bound_folder = "test-results/naiv_5_percent/indexes"
#upper_bound_folder = "test-results/naiv_5_percent/histograms_and_indexes"
#upper_bound_folder = "test-results/naiv_1_percent/indexes"
#upper_bound_folder = "test-results/naiv_1_percent/histograms_and_indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_2/indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_2/histograms_and_indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_15/indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_15/histograms_and_indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_1/indexes"
#upper_bound_folder = "test-results/upper_bound_4_levels_incremental_0_1/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075/indexes"
upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1/indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075/indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075/histograms_and_indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05/indexes"
#upper_bound_folder = "test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05/histograms_and_indexes"

#upper_bound_folder = "results"

# Call the function to compare JSON files and plot the mean values
compare_json_files(original_folder, upper_bound_folder, None)  # No need for an output file in this case


