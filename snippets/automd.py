import json
import os

files = ['javascript','html','java','xml']

for fileName in files:
    with open(f'snippets/{fileName}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    readmePath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'README.md')

    with open(readmePath, 'a', encoding='utf-8') as readme:
        readme.write(f"\n\n## {fileName}\n")
        readme.write("|Prefix|Description|\n")
        readme.write("|------|-----------|\n")

    for item in data.values():
        # print(item);
        prefix = item['prefix']
        description = item['description']
        row = f"|`{prefix}`|{description}|\n"
        # Append the row to the README.md file
        with open(readmePath, 'a', encoding='utf-8') as readme:
            readme.write(row)
