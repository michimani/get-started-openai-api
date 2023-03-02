import sys
import os
import json
from util.client import init_openai

MODEL_FOR_CHAT_COMPLETION = 'gpt-3.5-turbo'


def chat_completion(client, base_content, query, chat_id):
    messages = []
    if chat_id != '':
        messages = load_chat_history(chat_id)

    if len(messages) == 0:
        messages = [
            {'role': 'system', 'content': base_content}
        ]

    messages.append({
        'role': 'user', 'content': query
    })

    res = client.ChatCompletion.create(
        model=MODEL_FOR_CHAT_COMPLETION,
        messages=messages
    )

    chat_id = res['id']

    for c in res.choices:
        print('{}: {}\n'.format(c['message']['role'], c['message']['content']))
        messages.append(c['message'])

    save_chat_history(chat_id, messages)
    print()
    print('current chat id: {}'.format(chat_id))


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


if __name__ == "__main__":
    client = init_openai()

    args = sys.argv

    if len(args) < 3:
        print('1st parameter: base content for system role')
        print('2nd parameter: your message')
        print('3rd parameter (option): chat ID of history')
        exit()

    base_content = args[1]
    query = args[2]

    chat_id = ''
    if len(args) > 3:
        chat_id = args[3]

    chat_completion(client, base_content, query, chat_id)
