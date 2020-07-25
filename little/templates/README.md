# Little Algorithm

| 题号 | 题目名 | 题解代码 | 对应文章 |
| :-: | --- | --- | --- |
{% for item in items %}| [{{ item[1].fid }}]({{ item[1].url }}) | {{ item[1].title }}<br />{{ item[1].translated_title }} | {{ item[1].solutions.md_piece() }} | {{ item[2].md_piece() }} |
{% endfor %}
