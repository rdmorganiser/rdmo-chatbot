import chainlit as cl
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://chat-ai.academiccloud.de/v1"
)

cl.instrument_openai()

settings = {
    "model": "llama-3.3-70b-instruct",
    "max_tokens": 100,
    "temperature": 0.5
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you use your deep knowledge of research "
                           "data managment to info the user about RDMO on each question.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
