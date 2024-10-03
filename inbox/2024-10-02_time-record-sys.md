---
tags: 
    - project
create date: 2024-10-02
---

# Time Record System

## Brainstorms

The current structure of my daily time usage log is:

**Note**: Here are all the top categories

- #weakness: 
- #daily
- #work:
- #study:
- #ent.:

| Categories       | Events                       | Time(in mins) |
|------------------|------------------------------|---------------|

I wanna use python to extract the table data from a markdown file, and accumulate the time for each branch of the top categories.

The workflow may look like:

1. Open and process the file one by one (with argparse lib)
2. Find all the necessary info with re lib
3. Accumulate the time for the same branches
4. Create a new markdown file and open it, generate a table with the output result we just got
5. we can manually insert the weekly table


I gonna use [[regualr-explanation]] to find and extract the content from a table in the markdown file.

For find all the key infos:

- Top categories: \|\s#\w+\/
- Branches: \/\w+
- Time: \|\s\d+

However the condition of this can work is that we only have one table in the markdown files and the table should be like this:

| Categories     | Events | Time(in mins) |
|----------------|--------|---------------|
| #topCat/branch | Name   | Time used     |


## References

- [py-markdown-table](https://pypi.org/project/py-markdown-table/): generate formatted tables in markdown
- [re](https://docs.python.org/3/library/re.html): regular expression operations, usefule to find the content
- [argparse](): parse the parameters from the terminal

