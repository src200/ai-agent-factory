from autogen import ConversableAgent, register_function
from gpt_researcher import GPTResearcher
from typing_extensions import Annotated
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

assistant = ConversableAgent(
    "gpt-researcher",
    system_message="Your are a top research agent. You can conduct research and write reports.",
    llm_config={"config_list": [{"model": "gpt-4o", "temperature": 0.9, "api_key": os.getenv("OPENAI_API_KEY")}]},
    code_execution_config=False,
    human_input_mode="NEVER"
)

user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    human_input_mode="NEVER"
)

@user_proxy.register_for_execution()
@assistant.register_for_llm(
    name="conduct_research", description="Get the current weather in a given location."
)
async def conduct_research(query: Annotated[str, "The city and state, e.g. Toronto, ON."]) -> str:
    print("Conducting research...")
    researcher =  GPTResearcher(query, "research_report")
    research_result = await researcher.conduct_research()
    print("Research result", research_result)
    report =  await researcher.write_report()
    return report

register_function(
    conduct_research,
    caller=assistant,
    executor=user_proxy,
    name="conduct_research",
    description="conduct_research",
)

async def initiate_chat():
    reply = await user_proxy.a_initiate_chat(assistant, message="""
    Generate 10 viral tweets with catchy headers and long threads about the latest tools using generative AI.
    Include the following elements:
    0. Do extensive research on AI trends and latest news from industry and academia.
    1. Engage the audience with an intriguing fact or statistic about AI advancements.
    2. Use the trending hashtag to increase visibility, collect them from Twitter.
    3. Browse Twitter for fetching and analyzing viral content
    4. Start each thread with a striking fact or statistic that highlights the rapid advancement of generative AI.
    5. Mention the importance of staying updated with AI trends for tech enthusiasts and industry professionals.
    6. For each AI tool, start with an engaging header that captures its essence and utility.
    7. Delve into how each tool leverages AI, its impact, and real-world applications.
    8. Include high-quality images or videos that demonstrate the tool in action (if available).
    9. Encourage interaction by asking followers for their opinions or experiences with the tool.
    10. Summarize the key takeaways from the threads and invite followers to share the thread and tag people who would find this information useful.
    """, max_turns=6)
    print(reply)
    
asyncio.run(initiate_chat())