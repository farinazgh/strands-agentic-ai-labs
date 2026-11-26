from strands import Agent, tool
from strands.vended_tools import file_editor
from strands.vended_tools.web_fetch import web_fetch

# Simulated internal product database.
PRODUCT_CATALOG = {
    "wireless headphones": "SKU-WH100: Wireless Headphones Pro - $79.99, 142 in stock, 4.5★ rating, launched 2025-03",
    "usb-c hub": "SKU-UC200: USB-C Hub 7-in-1 - $45.00, 89 in stock, 4.2★ rating, launched 2024-11",
    "mechanical keyboard": "SKU-MK300: Mechanical Keyboard RGB - $149.99, 23 in stock, 4.8★ rating, launched 2025-01",
    "noise cancelling": "SKU-NC400: Noise Cancelling Earbuds - $129.99, 67 in stock, 4.6★ rating, launched 2025-05",
}

NO_PRODUCTS_MESSAGE = (
    "No products found matching '{query}'. Available: "
    "wireless headphones, usb-c hub, mechanical keyboard, noise cancelling"
)

# Define the agent's role, behaviour and tool usage instructions.
SYSTEM_PROMPT = (
    "You are a product research analyst. You help the team understand market "
    "positioning by comparing competitor pricing with our internal catalog.\n\n"
    "When given a research task:\n"
    "1. Use web_fetch to gather public market data from the web\n"
    "2. Use query_product_database to check our internal pricing and inventory\n"
    "3. Write a brief competitive analysis and save it to report.md using file_editor"
)

# Define the specific task submitted by the user.
USER_PROMPT = (
    "Research what wireless headphones are trending on the market and compare it "
    "against our offerings. Write a short competitive positioning summary and "
    "save it to report.md"
)


# Expose a deterministic Python function as an agent tool.
@tool
def query_product_database(query: str) -> str:
    """Query the internal product database for inventory and pricing information.

    Args:
        query: Search query for products (e.g., "wireless headphones", "USB-C hub")
    """
    normalized_query = query.lower()

    matches = [
        product_details
        for product_name, product_details in PRODUCT_CATALOG.items()
        if product_name in normalized_query
    ]

    if matches:
        return "\n".join(matches)

    return NO_PRODUCTS_MESSAGE.format(query=query)


def main() -> None:
    research_agent = Agent(
        # Register vended and custom tools.
        tools=[
            web_fetch,  # Retrieve and process web content.
            file_editor,  # Read, create and modify local files.
            query_product_database,  # Query the simulated product database.
        ],
        # Provide persistent behavioural instructions to the model.
        system_prompt=SYSTEM_PROMPT,
    )

    # Invoke the agent loop with the user prompt.
    research_agent(USER_PROMPT)


if __name__ == "__main__":
    main()
