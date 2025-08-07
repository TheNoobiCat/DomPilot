# Example usage for DomPilot
from DomPilot import LLMClient
from DomPilot import DomPilotAgent
import asyncio
from DomPilot import LogLevel

async def main():
    api_key = "ollama model doesn't need a key here"
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
