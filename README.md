# DomPilot

**DomPilot** is the next-generation AI web scraping library, powered by Playwright and Large Language Models (LLMs). It brings autonomous, agentic exploration to web data extraction—think of it as your digital detective for the web!

---

## 🚀 Why DomPilot?

- **Agentic Exploration:** DomPilot doesn’t just scrape—it *thinks*. It explores websites like a human, following links, filling forms, and adapting strategies to extract exactly the data you need.
- **LLM-Powered Intelligence:** Uses LLMs to reason about site structure, choose the best tools, and adapt to any website.
- **Playwright Integration:** Leverages the power of Playwright for robust, stealthy, and dynamic browser automation.
- **Smart Tools:** Built-in tools for navigation, content extraction, contact info discovery, form handling, and more.
- **Schema-Driven:** You define the data schema—DomPilot ensures the output matches, no matter how complex the site.
- **Memory & Adaptation:** Remembers clues, adapts strategies, and never gives up until all options are exhausted.

---

## 📦 Installation

Install DomPilot from PyPI:

```bash
pip install DomPilot==0.1.1
```

> **Note:** You’ll also need to install Playwright browsers (one-time setup):

```bash
python -m playwright install
```

---

## ✨ Quickstart Example

```python
from DomPilot import LLMClient, DomPilotAgent, LogLevel
import asyncio

async def main():
    # Configure your LLM endpoint (OpenAI, Azure, or local Ollama)
    api_key = "your-api-key"  # Not needed for local models like Ollama
    endpoint_url = "http://localhost:11434/v1/chat/completions"
    model = "qwen3:4b"

    client = LLMClient(api_key, endpoint_url, model, max_tokens=100000000)
    agent = DomPilotAgent(client, log_level=LogLevel.VERBOSE)

    url = "https://example.com"
    task_desc = "describe what this website is about"
    response_schema = {
        "description": "string"
    }

    agent.provide_task(url, task_desc, response_schema, headless=False)
    result = await agent.run_agent()
    print("Final Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🧠 How It Works

1. **Define Your Task:** Specify the target URL, a natural language task description, and the exact schema for the data you want.
2. **Agentic Exploration:** DomPilot’s agent autonomously explores the site—navigating, searching, clicking, and extracting—using LLM-powered reasoning.
3. **Schema-Matched Output:** The agent returns data that matches your schema, or fails only after exhaustive, intelligent exploration.

---

## 🛠️ Core Features

- **Autonomous Navigation:** Follows links, clicks buttons, fills and submits forms, and adapts to site structure.
- **Smart Extraction Tools:** 
  - `text_content`, `content`, `find_contact_info`, `extract_structured_data`, `find_navigation_links`, `get_all_forms`, `smart_fill_form`, and more.
- **Memory & Reasoning:** Remembers clues, avoids redundant actions, and adapts strategies on the fly.
- **LLM-Driven:** Works with OpenAI, Azure OpenAI, or local LLMs (like Ollama).
- **Stealth Mode:** Uses `playwright-stealth` to bypass anti-bot measures.

---

## 🔥 Example Use Cases

- Extract company info, contact details, or product data from any website.
- Scrape technical documentation, user profiles, or multi-page listings.
- Automate complex, multi-step web data extraction tasks with minimal code.

---

## 📚 Documentation

See [example.py](example.py) for a full working example.

For advanced usage, custom schemas, and agent strategies, check the source code and in-depth comments.

---

## 📝 License

MIT License © 2025 TheNoobiCat

Contributions welcome!

---

Ready to supercharge your web scraping?  
**DomPilot**: Explore. Extract. Dominate the DOM.
