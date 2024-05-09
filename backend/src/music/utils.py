import wikipedia
import asyncio
import aiohttp


async def fetch_wikipedia_summary(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError as e:
        return f"Page error: {e}"

async def get_wikipedia_summary_async(query):
    async with aiohttp.ClientSession() as session:
        result = await fetch_wikipedia_summary(query)
        return result