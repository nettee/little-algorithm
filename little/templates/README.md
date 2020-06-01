# Little Algorithm

| 题号 | 题目名 | 对应文章 |
| :-: | --- | --- |
{% for item in items %}| [{{ item[1].fid }}]({{ item[1].url }}) | {{ item[1].title }}| {{ item[2].md_piece() }} |
{% endfor %}
