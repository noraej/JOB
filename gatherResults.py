import json
import os
from collections import defaultdict
import matplotlib.pyplot as plt


#directory where results are stores
directory = "results/res"

#output path for json file
output_path_json = "results/collected_res/all_queries.json"

#output path for md file
output_path_md = "results/collected_res/all_queries.md"



def convertCommand(commandIn):
    if (commandIn == 'normal_run'):
        return 'No forced join'
    if (commandIn == 'with_nested_loop_join'):
        return 'Nested loop join'
    if (commandIn == 'with_hash_join'):
        return 'Hash join'

def convertFileName(filename):
    return filename.replace('.json', '')

# Marking interesting results 
def interesting_mark(interesting_flag):
    
    if(interesting_flag != "Not interesting"):
        return "❗"
    
    else: return ""


def sort_results(data):
    """
    Sort the results in the data dictionary by source file name.
    """
    sorted_data = {}
    for source_file in sorted(data.keys()):
        sorted_data[source_file] = data[source_file]
    return sorted_data

no_force_counter = 0
hj_counter = 0
nlj_counter = 0


# Identifies interesting results 
def compare(noForce, nlj, hj):
    #If no forced join is the fastes option -> not interesting because forcing joins did not give any results
    if ((noForce < nlj) & (noForce < hj)):
        return "Not interesting"
    
    #If nested loop join is fastest and no force runtime is not more than 2* from hj runtime 
    #Indicates that hj was chosen, but nlj might be a better choice
    if ((nlj < noForce) & (nlj < hj) and (noForce/2 < hj < noForce*2)):
        return "Nested loop was not chosen, but it was faster"
    
    #If hj is fastest and no force runtime is not more than 2* from nlj runtime 
    #Indicates that nlj was chosen, but hj might be a better choice
    if ((hj < noForce) & (hj < nlj) and (noForce/2 < nlj < noForce*2)):
        return "Hash join was not chosen, but is faster"

    else: return "Not interesting"


############## Generating combined json file ###################
data = []

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), 'r') as file:
            json_data = json.load(file)
                       
            for result in json_data['results']:
                result['source_file'] = filename

            data.extend(json_data['results'])

combined_data = {"results": data}

results = combined_data['results']

grouped_data = defaultdict(list)
for record in results:
    query = record["source_file"]
    grouped_data[query].append(record)

transformed_data = {}
for query, results in grouped_data.items():
    transformed_data[query] = {"results": results}


with open(output_path_json, 'w') as file:
    json.dump(sort_results(transformed_data), file, indent=4)


##################### Generating markdown file ####################

with open(output_path_json, 'r') as file:
    transformed_data = json.load(file)

with open(output_path_md, 'w') as md_file:

    for source_file, data in transformed_data.items():
        normMean = ''
        hjMean = ''
        nljMean = ''

        for result in data["results"]:
            if(result["command"] == "normal_run"):
                normMean = result["mean"]
            if(result["command"] == "with_nested_loop_join"):
                nljMean = result["mean"]
            
            if(result["command"] == "with_hash_join"):
                hjMean = result["mean"]

        interesting_flag = compare(normMean, nljMean, hjMean)

        if(interesting_flag == "Not interesting"):
            no_force_counter = no_force_counter + 1 
        
        if(interesting_flag == "Nested loop was not chosen, but it was faster"):
            nlj_counter = nlj_counter + 1 
        
        if(interesting_flag == "Hash join was not chosen, but is faster"):
            hj_counter = hj_counter + 1 
        

        md_file.write(f"## {interesting_mark(interesting_flag)} {convertFileName(source_file)}\n\n")
        md_file.write(interesting_flag + " \n\n")
        md_file.write("| Join method | Mean | StdDev | Median | Min | Max |\n")
        md_file.write("| ----------- | ---- | ------ | ------ | --- | --- |\n")

        for result in data["results"]:
            command = convertCommand(result["command"])
            mean = str(round(result["mean"], 2))
            stddev = str(round(result["stddev"], 2))
            median = str(round(result["median"], 2))
            min_val = str(round(result["min"], 2))
            max_val = str(round(result["max"], 2))

            md_file.write(f"| {command} | {mean} | {stddev} | {median} | {min_val} | {max_val} |\n")


print("No force: ", no_force_counter, " hash: ", hj_counter, "nlj: ", nlj_counter)
