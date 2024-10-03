---
tags: [
    - project
]
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

```python
for path in filepaths:
    open(path)

    if(fail_to_open):
        print(...)

```

I gonna use [[regualr-explanation]] to find and extract the content from a table in the markdown file.

## References

- [py-markdown-table](https://pypi.org/project/py-markdown-table/): generate formatted tables in markdown
- [re](https://docs.python.org/3/library/re.html): regular expression operations, usefule to find the content
- [argparse](): parse the parameters from the terminal

