import asyncio
from adk import Agent
from config import MODEL_NAME

class BlogAgent(Agent):
    def __init__(self):
        super().__init__(
            model=MODEL_NAME,
            system_prompt=open("prompts/system_prompt.txt").read(),
            tools=[
                "tools.google_search:google_search",
                "tools.summarizer:summarize",
                "tools.rss_reader:read_rss"
            ]
        )

    async def generate_blog(self, topic: str):
        response = await self.run(
            user_message=f"Write a research-backed blog post about: {topic}"
        )
        return response


if __name__ == "__main__":
    agent = BlogAgent()
    topic = "AI trends 2025"
    result = asyncio.run(agent.generate_blog(topic))
    print(result)


