import os
import dotenv
import webbrowser
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
dotenv.load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize OpenAI client for DALL-E 3
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up Gemini generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 400,
}


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config
                        )
prompt_parts = [
    "Create a Dall-E prompt describing a specific, cute, or unexpected scenario involving a raccoon. The description should be direct and detailed enough to visualize the scene for image generation. Avoid introductory phrases like 'Imagine a world where' and focus directly on the raccoon's actions or setting",
]

response = model.generate_content(prompt_parts)
generated_prompt = response.text
# Generate an image based on the scenario with DALL-E 3
image_response = client.images.generate(
    model="dall-e-3",
    prompt=generated_prompt,
    n=1,
    size="1024x1024"
)

# Get the URL of the generated image
image_url = image_response.data[0].url  
print("Generated image URL:", image_url)
        
# Open the generated image in a web browser
webbrowser.open(image_url)
