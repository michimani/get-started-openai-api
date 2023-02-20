import openai
import os
import sys
from token_count import tokens


def init():
    org_id = os.getenv("OPENAI_ORGANIZATION_ID")
    api_key = os.getenv("OPENAI_API_KEY")

    if org_id is None or len(org_id) == 0:
        print("OPENAI_ORGANIZATION_ID is empty")
        return

    if api_key is None or len(api_key) == 0:
        print("OPENAI_API_KEY is empty")
        return

    openai.organization = org_id
    openai.api_key = api_key


MODEL_FOR_COMPLETION = 'text-ada-001'


def completion(query):
    tks, count = tokens(query)
    print('token count:{} tokens:{}\nquery\n-----\n{}\n-----'.format(count, tks, query))

    res = openai.Completion.create(
        model=MODEL_FOR_COMPLETION,
        prompt=query,
        max_tokens=count,
        temperature=0
    )

    for choice in res.choices:
        print(choice.text)


DEFAULT_QUERY = """
Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new Batman movie!
Sentiment:"""

if __name__ == "__main__":
    init()

    args = sys.argv

    query = DEFAULT_QUERY
    if len(args) > 1:
        query = args[1]

    completion(query)
