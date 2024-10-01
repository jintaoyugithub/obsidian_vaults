---
tags: [
    - git
]
create date: 2024-09-30
---

# Git Submodules

## Commonly used

`Clone` 

When you clone some github repos which have their own submodules, it's better to clone recursively

```bash
git clone --recursive <url>
```

`Add`:

```bash
git submodule add <url>
```

`Remove`:

Remove a submodule from the project is way more complex than add it.

First you should remove the submodule info in files **.gitmodule** and **.git/config**.

And then run the commend

```bash
git rm --cached <path/to/submodule>
```

`Update`:

Sometimes you don't know if the project has submodules in advance, you can run the command below to check and update the submodules.

```bash
git submodule update --init --recursive
```

