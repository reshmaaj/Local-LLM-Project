import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-r1:8b"

def build_prompt(messages):
    prompt = ""
    for msg in messages:
        prompt += f"{msg['role'].upper()}: {msg['content']}\n"
    return prompt.strip()

def call_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Ollama request failed: {e}")

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
    ]

    prompt = build_prompt(messages)
    print("Prompt:\n", prompt)

    answer = call_ollama(prompt)
    print("\nAssistant:", answer)

    messages.append({"role": "assistant", "content": answer})