import os
import openai
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

# Set up environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

# Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content (modify tags as needed for the specific website)
        content = "\n".join([p.get_text(strip=True) for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website content: {e}")
        return None

# Function to query ChatGPT API
def query_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error communicating with ChatGPT API: {e}")
        return "I'm sorry, I couldn't process your request."

# Chatbot implementation
def chatbot(url):
    print("\nChatbot initialized. Fetching website content...")

    # Scrape the website
    content = scrape_website(url)
    if not content:
        print("Failed to retrieve content. Exiting chatbot.")
        return

    print("Website content fetched successfully. You can now interact with the chatbot. Type 'exit' to quit.\n")

    # Chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Include scraped content in the prompt
        prompt = f"The user is asking a question about the following website content: \n\n{content}\n\nQuestion: {user_input}"
        response = query_chatgpt(prompt)
        print(f"ChatGPT: {response}\n")

# Run the chatbot if executed directly
if __name__ == "__main__":
    website_url = input("https://pytorch.org/docs/stable/index.html") # Enter the URL of the website to interact with
    chatbot(website_url)
