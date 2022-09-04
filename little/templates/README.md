# Little Algorithm

从 2020 年初开始，我在公众号《面向大象编程》上发表面试算法、LeetCode 题解相关文章，至今收获不少好评。此仓库是公众号内容的补充，包括公众号文章涉及到的题目的参考代码，以及 LeetCode 题目到文章链接的索引。

## 如何使用本仓库

1、关注我的公众号 **面向大象编程** 获取文章更新。我的公众号坚持原创更新，干货分享，绝对是值得关注的技术公众号。

2、公众号文章目前绝大部分都是拿 LeetCode 原题作为例题，讲解算法题解题思路。从下方「参考代码」部分的表格中找到你喜欢的 LeetCode 题目，即可找到对应的参考代码以及讲解文章链接。

## 文章题解

TBD

## 参考代码

| 题号 | 题目名 | 题解代码 | 对应文章 |
| :-: | --- | --- | --- |
{% for item in problem_view %}| [{{ item.fid }}]({{ item.problem.url }}) | {{ item.problem.title }}<br />{{ item.problem.translated_title }} | {{ item.problem.solutions.md_piece() }} | {{ item.article.md_piece() }} |
{% endfor %}

## 公众号文章整理

可关注公众号《面向大象编程》，在公众号菜单中有文章目录。