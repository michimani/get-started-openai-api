import sys
from util.token_count import tokens
from util.client import init_openai


MODEL_FOR_COMPLETION = "text-ada-001"


def completion(client, query):
    tks, count = tokens(query)
    print("token count:{} tokens:{}\nquery\n-----\n{}\n-----".format(count, tks, query))

    res = client.Completion.create(
        model=MODEL_FOR_COMPLETION, prompt=query, max_tokens=count, temperature=0
    )

    for choice in res.choices:
        print(choice.text)


DEFAULT_QUERY = """
Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new Batman movie!
Sentiment:"""

if __name__ == "__main__":
    client = init_openai()

    args = sys.argv

    query = DEFAULT_QUERY
    if len(args) > 1:
        query = args[1]

    completion(client, query)
