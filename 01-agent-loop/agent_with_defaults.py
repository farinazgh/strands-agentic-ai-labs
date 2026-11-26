from strands import Agent
from strands.models import BedrockModel
from strands.vended_tools import file_editor, shell
from strands.vended_tools.web_fetch import web_fetch

MODEL_ID = "us.anthropic.claude-sonnet-4-6"
USER_PROMPT = (
    "Research the current state of AI agent deployment patterns in production, "
    "including common architectures, challenges teams face, and best practices. "
    "Write a summary to report.md"
)


def main() -> None:
    research_agent = Agent(
        model=BedrockModel(model_id=MODEL_ID),
        tools=[
            file_editor,  # Read, create and modify local files.
            shell,  # Execute shell commands.
            web_fetch,  # Retrieve and process content from web URLs.
        ],
        # Automatically manage context through compression and offloading.
        # Alternatives: "agentic", False, None, or a custom ContextManager.
        # auto → SDK-driven context management.
        # agentic → LLM-driven context management.
        context_manager="auto",
    )

    research_agent(USER_PROMPT)


if __name__ == "__main__":
    main()
