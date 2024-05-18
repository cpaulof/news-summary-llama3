# How to run

Download a quant model from [Huggingface](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF).
Specify its path with MODEL_PATH inside config.py

```bash
git clone https://github.com/cpaulof/news-summary-llama3.git
cd news-summary-llama3
pip install -r requirements.txt
python controller.py
```

### New urls are fetched every few minutes and generation is made every few seconds when there is available unprocessed urls.

> **Note:** Any error on parsing articles html will result on that url being ignored.

### Generation example
![image](./docs/ex_generation.png)

### API request

```url 
http://HOST:PORT/news?amount=5&page=2
 ```

![image](./docs/ex_api_result.png)
