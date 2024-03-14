# Read the html.json file
import json

with open('javascript.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data.values():
    # print(item);
    prefix = item['prefix']
    description = item['description']
    row = f"|`{prefix}`|{description}|\n"
    # Append the row to the README.md file
    with open('c:/Users/snapi/vplus-snippets/README.md', 'a', encoding='utf-8') as readme:
        readme.write(row)