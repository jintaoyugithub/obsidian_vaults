import re

# 定义读取文件和提取内容的函数


def extract_data_from_markdown(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    # 正则表达式
    pattern = r"\| #(\w+)/(\w+)\s*\|.*?\|\s*(\d+)\s*\|"

    # 匹配并提取内容
    matches = re.findall(pattern, markdown_text)

    # 打印结果
    for match in matches:
        print(match)
        # top, branch, time = match
       # print(f"Top: {top}, Branch: {branch}, Time: {time} mins")


# 示例文件路径
file_path = '/Users/jintao/vaults/notes/daily-notes/2024-10-03.md'

# 调用函数
extract_data_from_markdown(file_path)
