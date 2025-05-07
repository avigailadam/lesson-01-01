import json
import os

# Define the job names
job_names = ["a", "b", "c"]

# Get the workspace directory from the environment variable
output_path = os.path.join(os.getenv("GITHUB_WORKSPACE", "."), "script_output.json")

# Output the job names as a JSON array
with open(output_path, "w") as f:
    json.dump(job_names, f)