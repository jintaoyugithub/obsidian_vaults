---
tags: 
    - note_takings
create date: 2024-09-29
---

# obsidian

## Links

The most exciting feature in Obsidian is the `Link`, it can even point to a markdown file that doesn't exist yet. you can use `Ctrl + Mouse Click` in Obsidian app or `gf` in neovim to create a new markdown file based on that title and open it.

I can go to a [[random]] markdown file in the **vaults/temp-notes**, if it's not exist, the obsidian will ask you if you want create a one.

You can even link headings in other files, like [[examples#headline one]]

Note: you can only see these below in obsidian app, not in obsidian.nvim. However you can still natigate among the blocks which have been marked by obsidian app in neovim.

And you can display the content of that heading hold in Obsidian app by doing the following:

![[examples#headline two]]

You can link the paragrah as well

![[examples#^e6a91b]]

You can also specify the marker for the block

![[examples#^test]]

if you want to link a block inside the same md file:

1. you need to generated a `block id` for it, like ^testid
2. link the id somewhere else with:

![[#^testid]]


Recommendation on when to use a link:

- Books
- Concept that you gonna reuse

## Hashtags

I think hashtag in Obsidian would make you easier combine the ideas that seems unrelated but connect to one concept. like #gameIdeas #todo #toNote etc.

For example, I got some very nice #obsidian/tips today and I wanna add them to a official document later.

In the meantime, I got some content that is also relate to #obsidian/tips somewhere in [[examples#headline one]], I can also add this hashtag to make me find them easier.


**Links vs. Hashtags**

Basically hashtags increase searchability, they provide quicker search for your content and make better pages. Hashtags are more about broadly search, and links to papers to explain them in depth.

For example, I'm learning std lib of c++, I can create a hashtag #cpp/std and when I read something new about this topic I can write them down immediately mark with that hashtag and organized them during the night.

Or we encounter some error or bug when writing c++, however it's difficult for us to give them a unified classification. At this time, labeling them will #cpp/error/link or #cpp/error/compile make it easier for us to find them.


## Images

![test.png](assets/imgs/test.png)

## Math expression

Pretty similar to the original markdown file, obsidian use `$..$` and `$$...$$` to write the math formula, for example

$a = b + c$

$$\begin{vmatrix}a & b\\
c & d
\end{vmatrix}=ad-bc$$
