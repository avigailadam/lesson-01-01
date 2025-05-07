import json

# Define the job names
job_names = ["a", "b", "c"]

# Output the job names as a JSON array
with open("script_output.json", "w") as f:
    json.dump(job_names, f)