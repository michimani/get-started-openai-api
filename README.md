get-started-openai-api
===

Get started OpenAI API.


# Usage

1. Create .env

    ```bash
    cp .env.sample .env
    ```

    Edit it, and export.

    ```bash
    source .env
    ```

2. Activate virtual environment

    ```bash
    source .venv/bin/activate
    ```

3. Install modules

    ```bash
    pip install -r requirements.txt
    ```

## Completion

```bash
python completions.py '今日の天気は晴れでしたが、夕方には少しだけ雨が降って、すぐ止んで、そのあと風が強くなりました。明日の天気はどうなりますか？'
```

Output

```
token count:84 tokens:[20015, 232, 33768, 98, 5641, 25465, 36365, 245, 31676, 162, 247, 112, 39258, 30640, 22180, 25224, 35585, 23513, 13783, 243, 43095, 28618, 31676, 22887, 239, 22180, 46777, 2515, 239, 37239, 101, 35585, 165, 247, 235, 33180, 28134, 23513, 33623, 2515, 238, 29826, 95, 22174, 30640, 23513, 2515, 251, 5641, 40948, 30201, 165, 95, 101, 35585, 28156, 115, 31917, 26945, 28255, 30159, 22180, 25224, 16764, 23626, 236, 33768, 98, 5641, 25465, 36365, 245, 31676, 2515, 102, 29557, 26945, 28255, 30159, 33623, 27370, 171, 120, 253]
query
-----
今日の天気は晴れでしたが、夕方には少しだけ雨が降って、すぐ止んで、そのあと風が強くなりました。明日の天気はどうなりますか？
-----


明日は晴れ。
```

## Chat Completion

```bash
python chat.py 'あなたは電卓です。計算結果となる数字だけを答えてください。' '1+1='
```

Output

```
assistant: 2


current chat id: chatcmpl-6pelWDjzxVZayS4VMUj4kr6VCblYN
```

If you wish to continue chatting with the context of this conversation, pass the output Chat ID as the third argument.

```bash
python chat.py '' '*2=' chatcmpl-6pelWDjzxVZayS4VMUj4kr6VCblYN
```

```
assistant: 4


current chat id: chatcmpl-6penzqAybDnsDkmCfA4Fwk7NSu8Et
```

One more times.

```bash
python chat.py '' '**2=' chatcmpl-6penzqAybDnsDkmCfA4Fwk7NSu8Et
```

```
assistant: 16


current chat id: chatcmpl-6pep5Hn9PI1psGSXLQVusGNP0PcJS
```

One more..

```bash
python chat.py '' '**2=' chatcmpl-6pep5Hn9PI1psGSXLQVusGNP0PcJS
```

```
assistant: 256


current chat id: chatcmpl-6pepyrUMWDlXldx49uU1FgGVOkmgt
```

# Author

[michimani210](https://twitter.com/michimani210)