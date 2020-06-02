import requests


api_url = 'https://leetcode-cn.com/graphql'
problem_url = 'https://leetcode-cn.com/problems/two-sum/description/'


class GraphQLError(RuntimeError):
    pass


def execute_graphql(url, payload, headers):
    r = requests.post(url, json=payload, headers=headers)
    json = r.json()
    if 'errors' in json:
        errors = json['errors']
        messages = [error['message'] for error in errors]
        raise GraphQLError(messages)
    return json['data']


def query_problem_data(query: str, title_slug: str):
    payload = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": title_slug,
        },
        "query": query,
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'referer': problem_url,
        'content-type': "application/json",
    }

    return execute_graphql(api_url, payload=payload, headers=headers)


def query_translated_title_by_slug(title_slug: str) -> str:
    query = '''query questionData($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                translatedTitle
              }
            }
            '''

    data = query_problem_data(query, title_slug)
    return data['question']['translatedTitle']


if __name__ == '__main__':
    translated_title = query_translated_title_by_slug('two-sum')
    print(translated_title)