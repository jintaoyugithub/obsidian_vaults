import os
import re
import glob
import argparse
import datetime
from py_markdown_table.markdown_table import markdown_table

'''
The extracted data should looks like:
[
        {"Title 1": "Value1", "Title 2": "Value2", "Title 3": "Value 3"},
        {"Title 1": "Value4", "Title 2": "Value5", "Title 3": "Value 6"},
        ...
]
'''


def CleanTable(table):
    # clean the unnecessary lines
    cleaned_table = ''
    for line in table.splitlines():
        if line.startswith('|'):
            cleaned_table += line + '\n'

    print('\n' + cleaned_table)
    return cleaned_table


def CreateMDTable(filepaths):
    # Open and read the file
    data = []

    for filepath in filepaths:
        with open(filepath, 'r') as file:
            md_content = file.read()

        # Extract the necessary info with regular expression
        find_headers = r'\|\s([A-Z]\w+)\s+\|\s([A-Z]\w+)\s+\|\s([A-Z]\w+)\(in mins\)'
        find_contents = r'\|\s#(\w+)\/(\w+).*?\|.*?\|\s(\d+)'

        headers = re.findall(find_headers, md_content)
        contents = re.findall(find_contents, md_content)

        # make sure the contents are not empty
        if contents:
            # extract the data from the found first header
            Top, Branch, Time = headers[0]
            # construct the table with the data
            for row in contents:
                top, branch, time = row
                time = int(time)
                # check if the branch is already exist
                found = False
                if data:
                    for item in data:
                        if item[Branch] == branch:
                            item[Time] += time
                            found = True
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
    markdown_tb = markdown_table(data).get_markdown()
    return markdown_tb


def GenerateFilePath():
    parser = argparse.ArgumentParser(description="Process files input")
    parser.add_argument('files', nargs='+', help='Process markdown md files')
    args = parser.parse_args()

    all_files = []
    for pattern in args.files:
        all_files.extend(glob.glob(pattern))

    # 输出匹配的文件
    if all_files:
        # root = './'
        for i in range(len(all_files)):
            all_files[i] = all_files[i]
            print("Matched file: " + all_files[i])
        return all_files
    else:
        print("No files matched.")


def ComputeCurrentWeek():
    # 获取当前日期
    current_date = datetime.datetime.now()

    # 获取当前年份
    current_year = current_date.year

    # 获取ISO周数（ISO标准：每年第一周是包含第一个星期四的周）
    current_week_number = current_date.isocalendar()[1]

    return "week-" + str(current_week_number) + "-" + str(current_year) + '.md'


def WriteContent2File(dir, name, content):
    # make sure the folder exist, if not create a new one
    os.makedirs(dir, exist_ok=True)

    # Create full path
    file_path = os.path.join(dir, name)

    # Create the file and write the content to it
    with open(file_path, 'w', encoding='utf-8') as file:  # 使用 utf-8 编码
        file.write(content)


def Run():
    files = GenerateFilePath()
    mdtb = CreateMDTable(files)
    cleaned_tb = CleanTable(mdtb)
    current_week = ComputeCurrentWeek()
    WriteContent2File('../notes/weekly-reports', current_week, cleaned_tb)


if __name__ == "__main__":
    Run()
