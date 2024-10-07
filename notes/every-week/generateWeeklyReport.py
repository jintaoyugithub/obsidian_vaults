import re
import glob
import argparse
from py_markdown_table.markdown_table import markdown_table

'''
The extracted data should looks like:
[
        {"Title 1": "Value1", "Title 2": "Value2", "Title 3": "Value 3"},
        {"Title 1": "Value4", "Title 2": "Value5", "Title 3": "Value 6"},
        ...
]
'''
def CreateMDTable(filepaths):
    # Open and read the file
    data = []

    for filepath in filepaths:
        with open(filepath, 'r') as file:
            md_content = file.read()

        # Extract the necessary info with regular expression
        find_headers = r'\|\s([A-Z]\w+)'
        find_contents = r'\|\s#(\w+)\/(\w+).*?\|.*?\|\s(\d+)'

        headers = re.findall(find_headers, md_content)
        contents = re.findall(find_contents, md_content)

        # make sure the contents are not empty
        if contents:
            # extract the data from the header
            Top, Branch, Time = headers
            # construct the table with the data
            for row in contents:
                top, branch, time = row
                time = int(time)
                # check if the branch is already exist
                found = False
                for item in data:
                    if item[Branch] == branch:
                        item[Time] += time
                        found= True
                        break

                if not found:
                    data.append({
                        Top: top,
                        Branch: branch,
                        Time: time
                })
        else:
            print("empty contents")

    # create the markdown table
    markdown = markdown_table(data).get_markdown()
    print(markdown)


def GenerateFilePath():
    parser = argparse.ArgumentParser(description="Process files input")
    parser.add_argument('files', nargs='+', help='Process markdown md files')
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        all_files.extend(glob.glob(pattern))

    # 输出匹配的文件
    if all_files:
        root = './'
        for i in range(len(all_files)):
            all_files[i] = root + all_files[i]
            print("Matched file: " + all_files[i])
        return all_files
    else:
        print("No files matched.")


def Run():
    files = GenerateFilePath()
    CreateMDTable(files)


if __name__ == "__main__":
    Run()



