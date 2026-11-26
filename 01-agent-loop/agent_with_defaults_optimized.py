from pathlib import Path
from pprint import pprint

from strands import Agent
from strands.models import BedrockModel
from strands.vended_tools.web_fetch import make_web_fetch

MODEL_ID = "us.anthropic.claude-sonnet-4-6"

USER_PROMPT = (
    "Research current AI agent deployment patterns in production, "
    "including common architectures, challenges and best practices. "
    "Consult at most five authoritative sources. "
    "Fetch independent sources concurrently. "
    "Return a Markdown report of approximately 1000 words "
    "with source URLs."
)


def main() -> None:
    research_agent = Agent(
        model=BedrockModel(model_id=MODEL_ID),
        tools=[
            make_web_fetch(
                mode="markdown",
                max_content_chars=15000,
            ),
        ],
        context_manager="auto",
    )

    result = research_agent(USER_PROMPT)

    Path("report.md").write_text(
        str(result),
        encoding="utf-8",
    )

    pprint(result.metrics.get_summary())


if __name__ == "__main__":
    main()
