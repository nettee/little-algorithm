# Little Algorithm

| 题号 | 题目名 | 对应文章 |
| :-: | --- | --- |
{% for item in items %}| {{ item[0] }} | | {{ item[1].md_piece() }} |
{% endfor %}
