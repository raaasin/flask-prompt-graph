import openai
import os
from dotenv import load_dotenv
load_dotenv()
# Ensure you have set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

PROMPT = "Dinausaur notices meteor in the sky and is scared."

response = client.images.generate(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

# Print the URL of the generated image
print(response.data[0].url)
