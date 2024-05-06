import os
import json
import re
import matplotlib.pyplot as plt
import matplotlib

def compare_json_files(folder_paths, interesting_queries):
    matplotlib.rcParams.update({'font.size': 22})
    folder_values = {}
    folder_names = []
    file_name_order = {}
    file_name_index = 0

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

                    if file_name not in file_name_order:
                        file_name_order[file_name] = file_name_index
                        file_name_index += 1

                    if folder_label in folder_values:
                        folder_values[folder_label].append(mean_value)
                    else:
                        folder_values[folder_label] = [mean_value]

    bar_width = 1 / len(folder_values)
    margin = 0.05
    bar_width = bar_width - margin
    hatches = ['/', 'xx', '\\', '...', '**', '--', '||']

    for i in range(0, len(folder_values)):
        folder_name = folder_names[i]
        folder_value = folder_values[folder_name]

        sorted_float_values = [folder_value[file_name_order[filename]] for filename in interesting_queries]

        x_values = range(0, len(folder_value))

        x_values = [float(x_value) + (-1 + i * bar_width) for x_value in x_values]
            
        plt.bar(x_values, sorted_float_values, bar_width, color='lightgrey', edgecolor='black', alpha=0.5, label=folder_name, hatch=hatches[i])

    interesting_queries = [query.replace('.json', '') for query in interesting_queries]

    plt.xlabel('Query')
    plt.ylabel('Execution time (s)')
    plt.title('Runtime Comparison with Histograms')
    plt.xticks([i - ((bar_width + (margin * (len(folder_values)))) /2) - 0.5 for i in range(len(interesting_queries))], interesting_queries, rotation=45, ha='right')
    plt.legend(title="Implementations")
    plt.tight_layout()
    plt.show()

#interesting_queries = ["10c.json", "28b.json", "3b.json"]

# Naive no hist
# interesting_queries = ["4c.json", "8c.json", "10c.json", "17a.json", "17e.json", "28a.json"] 

# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/naiv_1_percent/indexes", "Naive 1%"),
#     ("test-results/naiv_5_percent/indexes", "Naive 5%")
# ]

# Naive hist
# interesting_queries = ["3c.json", "4c.json", "7a.json", "14a.json", "19c.json", "22d.json", "28a.json", "28c.json", "29c.json", "31c.json" ] 

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/naiv_1_percent/histograms_and_indexes", "Naive 1%"),
#     ("test-results/naiv_5_percent/histograms_and_indexes", "Naive 5%")
# ]


# Upper bound no hist
#interesting_queries = ["3a.json", "3b.json", "3c.json", "9a.json", "10a.json", "10b.json", "10c.json", "16a.json", "16b.json", "16c.json", "17a.json", "17e.json", "18c.json", "19a.json", "19b.json", "25c.json", "29a.json", "29b.json", "29c.json"]
# interesting_queries = ["9a.json", "10c.json", "16a.json", "16b.json", "16c.json", "17a.json", "17e.json", "18c.json", "19a.json", "19b.json", "25c.json"]
# interesting_queries = ["3a.json", "3b.json", "3c.json", "10a.json", "10b.json", "29a.json", "29b.json", "29c.json"]

# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/upper_bound_4_levels_incremental_0_1/indexes", "UpperBound01"),
#     ("test-results/upper_bound_4_levels_incremental_0_15/indexes", "UpperBound015"),
#     ("test-results/upper_bound_4_levels_incremental_0_2/indexes", "UpperBound02")
# ]


#Upper bound hist
# interesting_queries = ['3b.json','5c.json','8d.json','9b.json','10c.json','16b.json','16c.json','17b.json','17c.json','17d.json','17f.json','19c.json','20a.json','28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31a.json','31b.json','31c.json']
# interesting_queries = ['10c.json','17b.json','17c.json','17d.json','17f.json','19c.json']
# interesting_queries = ['3b.json','5c.json','8d.json','9b.json','20a.json']
# interesting_queries = ['28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31a.json','31b.json','31c.json']

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/upper_bound_fixed_0_1/histograms_and_indexes", "UpperBound01"),
#     ("test-results/upper_bound_fixed_0_15/histograms_and_indexes", "UpperBound015"),
#     ("test-results/upper_bound_fixed_0_2/histograms_and_indexes", "UpperBound02")
# ]


#Bounding box alpha=0.5 beta=0.4 gamma=0.1 uten hist
#interesting_queries = ["1a.json", "10c.json", "13d.json", "16c.json", "17a.json", "17b.json", "17c.json", "17d.json", "17e.json", "25c.json", "26c.json", "28a.json", "28b.json", "28c.json", "29a.json", "29b.json", "29c.json", "30c.json", "31a.json", "31c.json"]
#interesting_queries = ["10c.json", "16c.json", "25c.json"]
# interesting_queries = ["1a.json", "13d.json", "17a.json", "17b.json", "17c.json", "17d.json", "17e.json", "26c.json", "28a.json", "28b.json", "28c.json", "29a.json", "29b.json", "29c.json", "30c.json", "31a.json", "31c.json"]

# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_1_dec_0_05/indexes", "G1BoundingBox01"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_15_dec_0_075/indexes", "G1BoundingBox015"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/indexes", "G1BoundingBox02")
# ]


#Bounding box alpha=0.5 beta=0.4 gamma=0.1 hist
# interesting_queries = ['3b.json','3c.json','8c.json','9b.json','10c.json','17b.json','17c.json','17d.json','17f.json','18c.json','19c.json','20a.json','22b.json','26c.json','28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31a.json','31b.json']
# interesting_queries = ['10c.json','17b.json','17c.json','17d.json','17f.json','19c.json']
# interesting_queries = ['3b.json','3c.json','8c.json','9b.json','20a.json','22b.json','26c.json']
# interesting_queries = ['28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31a.json']

# folder_paths = [
#     ("test-results/original/histograms_and_indexes", "Original"),
#     ("test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_1_dec_0_05/histograms_and_indexes", "G1BoundingBox01"),
#     ("test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_15_dec_0_075/histograms_and_indexes", "G1BoundingBox015"),
#     ("test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_2_dec_0_1/histograms_and_indexes", "G1BoundingBox02")
# ]


#Bounding box alpha=0.7 beta=0.2 gamma=0.1 no hist
#interesting_queries = ["1a.json", "10c.json", "16b.json", "16c.json", "17a.json", "17e.json", "25c.json", "28a.json", "28b.json", "28c.json", "29a.json", "29b.json", "29c.json"]
#interesting_queries = ["10c.json", "28c.json"]
# interesting_queries = ["1a.json", "16b.json", "16c.json", "17a.json", "17e.json", "25c.json", "28a.json", "28b.json", "29a.json", "29b.json", "29c.json"]

# folder_paths = [
#     ("test-results/original/indexes", "Original"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_1_dec_0_05/indexes", "G2BoundingBox01"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_15_dec_0_075/indexes", "G2BoundingBox015"),
#     ("test-results/bounding_box_alpha_0_7_beta_0_2_gamma_0_1_inc_0_2_dec_0_1/indexes", "G2BoundingBox02")
# ]


#Bounding box alpha=0.7 beta=0.2 gamma=0.1 hist
# interesting_queries = ['3b.json','3c.json','8c.json','10c.json','17b.json','17c.json','17d.json','17f.json','19c.json','22a.json','22b.json','22c.json','22d.json','26c.json','28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31a.json','31b.json','31c.json']
# interesting_queries = ['10c.json','17b.json','17c.json','17d.json','17f.json','19c.json','31a.json']
# interesting_queries = ['3b.json','3c.json','8c.json','22a.json','22b.json','22c.json','22d.json','26c.json']
interesting_queries = ['28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31b.json','31c.json']

folder_paths = [
    ("test-results/original/histograms_and_indexes", "Original"),
    ("test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_1_dec_0_05/histograms_and_indexes", "G2BoundingBox01"),
    ("test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_15_dec_0_075/histograms_and_indexes", "G2BoundingBox015"),
    ("test-results/bounding_box_fixed_alpha_0_7_beta_0_2_gamma_0_1_incr_0_2_dec_0_1/histograms_and_indexes", "G2BoundingBox02")
]








# interesting_queries = ['3a.json','3c.json','9a.json','9b.json','10a.json','10b.json','10c.json','13d.json','15a.json','15c.json','15d.json','16a.json','16b.json','16c.json','16d.json','17a.json','17b.json','17c.json','17d.json','17e.json','19a.json','19b.json','20c.json','25a.json','28a.json','28b.json','28c.json']
# interesting_queries = ['9a.json','9b.json','10b.json','19a.json','19b.json']
# interesting_queries = ['10c.json']
# interesting_queries = ['15a.json','15c.json','15d.json','16a.json','16b.json','16c.json','16d.json','17a.json','17b.json','17c.json','17d.json','17e.json']
# interesting_queries = ['3a.json','3c.json','10a.json','20c.json','25a.json','28a.json','28b.json','28c.json']

# folder_paths = [
#     ("test-results/upper_bound_4_levels_incremental_0_15/indexes", "UpperBound015"),
#     ("test-results/bounding_box_alpha_0_5_beta_0_4_gamma_0_1_inc_0_2_dec_0_1/indexes", "G1BoundingBox02")
# ]


# interesting_queries = ['3c.json','4c.json','8c.json','8d.json','10c.json','16b.json','16c.json','22c.json','23a.json','24a.json','26a.json','26b.json','28a.json','28b.json','28c.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31b.json']
# interesting_queries = ['24a.json','29a.json','29b.json','29c.json','30a.json','30b.json','30c.json','31b.json']
# interesting_queries = ['10c.json','16b.json','16c.json']
# interesting_queries = ['3c.json','4c.json','8c.json','8d.json']
# interesting_queries = ['22c.json','23a.json','26a.json','26b.json','28a.json','28b.json','28c.json']

# folder_paths = [
#     ("test-results/upper_bound_fixed_0_15/histograms_and_indexes", "UpperBound015"),
#     ("test-results/bounding_box_fixed_alpha_0_5_beta_0_4_gamma_0_1_incr_0_2_dec_0_1/histograms_and_indexes", "G1BoundingBox02")
# ]


compare_json_files(folder_paths, interesting_queries)
