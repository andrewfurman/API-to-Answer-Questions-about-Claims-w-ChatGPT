import random
from openai import OpenAI
import os

def process_claim_question(claim_question: str) -> str:
    # Set up the OpenAI client
    client = OpenAI(
        # This will use the OPENAI_API_KEY from environment variables
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    
    # Prompt String (defines a multi paragraph string that can be used as the beginning of a prompt)
    background = """
    Please answer the question in plaintext and not in markdown format.

    If you don't know the answer, please respond with Based on the claim information provided, I'm unable to answer the question, and then explain why.

    Please use emojis at the start of new lines in the response. These emojis should distinctly represent the information provided on the line.

    Based on the below question, and the included information about the claim, can you tell me the answer to the question about the claim?  This answer should be provided in simple language that could easily be understood by a someone with low familiarity with healthcare claims.

    Also provide a detailed response below the simple answer that is inteded for a more sophistocated audience.
    """
    
    # Joins the background string and the claim question together
    prompt = background + claim_question

    # Send the question to ChatGPT and save the answer
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",  # or whichever model you prefer
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about claims."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the answer from the API response
    claim_answer = chat_completion.choices[0].message.content

    return claim_answer