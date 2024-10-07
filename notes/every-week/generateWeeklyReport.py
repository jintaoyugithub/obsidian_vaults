import re
import glob
import argparse
from py_markdown_table import MarkdownTable

'''
The extracted data should looks like:
[
        {"Title 1": "Value1", "Title 2": "Value2", "Title 3": "Value 3"},
        {"Title 1": "Value4", "Title 2": "Value5", "Title 3": "Value 6"},
        ...
]
'''

def ExtractTableFromFile(filepath):
    try:    
        # Open and read the file
        with open(filepath, 'r') as file:
            md_content = file.read()

        # Extract the necessary info with regular expression
        find_headers = r'\|\s([A-Z]\w+)'
        find_contents = r'\|\s#(\w+)\/(\w+).*?\|.*?\|\s(\d+)'

        headers = re.findall(find_headers, md_content)
        contents = re.findall(find_contents, md_content)

        print(headers)
        print(contents)


    except Exception as e:
        print("FATAL ERROR: {e}")

ExtractTableFromFile('/Users/jintao/vaults/notes/daily-notes/2024-10-03.md')



