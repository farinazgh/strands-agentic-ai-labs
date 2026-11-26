import os

from strands import Agent
from strands.models import BedrockModel
from strands.models.anthropic import AnthropicModel
from strands.models.ollama import OllamaModel
from strands.models.openai import OpenAIModel

# bedrock_model = BedrockModel(
#     model_id="us.anthropic.claude-opus-5"
# )

# anthropic_model = AnthropicModel(
#     client_args={"api_key": os.environ["ANTHROPIC_API_KEY"]},
#     model_id="claude-sonnet-5",
#     max_tokens=1024,
#     params={"temperature": 0.7},
# )


# openai_model = OpenAIModel(
#     client_args={"api_key": os.environ["OPENAI_API_KEY"]},
#     model_id="gpt-4o",
#     params={"max_tokens": 1000, "temperature": 0.7},
# )

OLLAMA_HOST = "http://localhost:11434"
OLLAMA_MODEL_ID = "gemma4:latest"
USER_PROMPT = "Explain the agent loop in one paragraph."


def main() -> None:
    ollama_model = OllamaModel(
        host=OLLAMA_HOST,
        model_id=OLLAMA_MODEL_ID,
    )
    agent = Agent(model=ollama_model)
    agent(USER_PROMPT)


if __name__ == "__main__":
    main()
