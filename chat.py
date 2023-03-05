import sys
import os
import json
from util.client import init_openai
from util.token_count import tokens

MODEL_FOR_CHAT_COMPLETION = 'gpt-3.5-turbo'


def chat_completion(client, messages):
    res = client.ChatCompletion.create(
        model=MODEL_FOR_CHAT_COMPLETION,
        messages=messages
    )

    for c in res.choices:
        print('{}: {}\n'.format(c['message']['role'], c['message']['content']))
        messages.append(c['message'])

    return res.usage['total_tokens']


CHAT_HISTORY_DIR = './chat_history'


def load_chat_history(chat_id):
    try:
        with open(os.path.join(CHAT_HISTORY_DIR, chat_id)) as f:
            history = json.load(f)
            return history
    except Exception:
        return []


def save_chat_history(chat_id, messages):
    file_path = os.path.join(CHAT_HISTORY_DIR, chat_id)
    with open(file_path, 'w') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


TOKENS_LIMIT = 4096


if __name__ == "__main__":
    client = init_openai()

    args = sys.argv

    messages = []
    if len(args) > 1 and len(args[1]) > 0:
        messages.append({
            'role': 'system',
            'content': args[1],
        })

    tokens_total = 0

    while tokens_total < TOKENS_LIMIT:
        try:
            query = input(
                'Please enter your message (press `Ctr + C` to end chat) \n>> ')

            if len(query) == 0:
                continue

            _, count = tokens(query)
            if (tokens_total + count) > TOKENS_LIMIT:
                print('Your message is too long.')
                print('Please enter your message less than {} tokens.'.format(
                    TOKENS_LIMIT - (tokens_total)))
                continue

            messages.append({
                'role': 'user',
                'content': query,
            })

            usage = chat_completion(client, messages)
            tokens_total += usage
            print('(current token total: {})\n'.format(tokens_total))

        except KeyboardInterrupt:
            print()
            print('See you again.')
            exit()
