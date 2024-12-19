import os
import json

# Function to process each JSON file and extract the manifest values
def extract_theme_info(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if 'manifest' in data:
            manifest = data['manifest']
            return {
                "name": manifest.get("name", ""),
                "description": manifest.get("description", ""),
                "author": manifest.get("author", ""),
                "license": manifest.get("license", ""),
                "link": f"https://raw.githubusercontent.com/nixietab/picodulce-themes/refs/heads/main/{filename}".replace("\\",'/')
            }
    return None

# List to store theme data
themes = []

# Loop through all files in the themes directory
themes_dir = 'themes'
for filename in os.listdir(themes_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(themes_dir, filename)
        theme_info = extract_theme_info(filepath)
        if theme_info:
            themes.append(theme_info)
            print(theme_info)


# Sort the themes list alphabetically by the 'name' key
themes.sort(key=lambda theme: theme['name'])

# Create the repo.json structure
repo_data = {
    "themes": themes
}

# Write to repo.json
with open('repo.json', 'w', encoding='utf-8') as outfile:
    json.dump(repo_data, outfile, indent=2)

print("repo.json has been generated and sorted alphabetically.")
