# Website-ChatGPT Chatbot

This project demonstrates how to build a simple chatbot that uses OpenAI's ChatGPT API to interact with content extracted from a given website. The chatbot operates via the console and provides relevant answers based on the scraped website data.

## Features
- Scrapes content from a given URL using web scraping techniques.
- Processes the scraped content to extract meaningful text.
- Integrates with the ChatGPT API to provide context-aware responses.
- Operates entirely via the console, no frontend required.

---

## Prerequisites

### 1. API Key
- Obtain your API key from OpenAI [here](https://platform.openai.com/).
- Store your API key as an environment variable named `OPENAI_API_KEY`.

### 2. Required Libraries
Install the following Python libraries:

```bash
pip install openai requests beautifulsoup4 python-dotenv
```

### 3. Python Version
Ensure you are using Python 3.7 or later.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/website-chatgpt-chatbot.git
   cd website-chatgpt-chatbot
   ```

2. Set up your environment:
   - Add your `OPENAI_API_KEY` to the environment:
     ```bash
     export OPENAI_API_KEY="your_api_key_here"
     ```
   - Alternatively, create a `.env` file and add your key if using a library like `python-dotenv`.

3. Run the script:
   ```bash
   python chatbot.py
   ```

---

## Usage

1. **Input the Website URL**:
   When prompted, provide the URL of the website you want the chatbot to analyze.

2. **Interact with the Chatbot**:
   - Type your questions related to the website content.
   - To exit, type `exit`.

---

## Example

```bash
Enter the URL of the website to interact with: https://example.com
Chatbot initialized. Fetching website content...

Website content fetched successfully. You can now interact with the chatbot. Type 'exit' to quit.

You: What is this website about?
ChatGPT: 'This website provides information about [summary extracted from website content].'

You: Who is the target audience?
ChatGPT: 'The target audience appears to be [relevant information].'

You: exit
Goodbye!
```