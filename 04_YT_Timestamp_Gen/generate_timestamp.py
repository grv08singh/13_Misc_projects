import google.generativeai as genai
import os

API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key="AIzaSyAQ5BNeQfxlUSdFQbRKszvqavHLl-2otQA")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)


def evaluate_timestamps(captions):

    prompt = f"""
    You are given a YouTube video transcript with timestamps. Your task is to extract only the important or meaningful moments from the transcript.

    🎯 For each important moment:
    - Include the timestamp (HH:MM:SS format)
    - Write just 1 to 3 words describing what's happening
    - Each line should follow this format:  
    `timestamp label`, for example: `00:00:00 Intro`

    🛑 DO NOT return a JSON list.  
    ✅ Just return plain lines like:
    00:00 Intro  
    00:15 Install Add-ins  
    00:45 Formula Example  
    ...

    💡 Only include super important timestamps where new question/problem start.  
    ⛔️ Skip unimportant lines or filler content.

    Here is the transcript:
    {captions}
    """

    # Generate evaluation using GenAI
    response = model.generate_content(prompt)

    return response.text