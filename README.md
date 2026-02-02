# Local LLM Inference with Ollama

This project demonstrates how to perform **local Large Language Model (LLM) inference** using [Ollama](https://ollama.com) without relying on any cloud-based APIs.

## Features

✅ Local LLM inference (no internet required after setup)  
✅ OpenAI-style chat message handling  
✅ Custom prompt construction  
✅ Error handling and configurable timeouts  

## Tech Stack

- Python  
- [Ollama](https://ollama.com)  
- DeepSeek-R1 (8B) model  
- REST API (`requests`)  

## Setup

### 1. Install Ollama

Follow the installation guide here: [Ollama Installation](https://ollama.com)

### 2. Pull the Model

```bash
ollama pull deepseek-r1:8b
