import os
import sys
import subprocess

# Define the virtual environment path
venv_path = os.path.join(os.getcwd(), "mycompanybrochure_v2")
venv_python = os.path.join(venv_path, "Scripts", "python.exe")  # Windows path

# Check if the script is running inside the virtual environment
if sys.prefix != venv_path:
    print("Restarting script inside the virtual environment...")
    subprocess.run([venv_python, *sys.argv])  # Restart the script inside the venv
    sys.exit()  # Exit the current process

# Now the script is running inside the virtual environment
print("Running inside the virtual environment!")

print("✅ Virtual environment is active.")

import gradio as gr
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import ollama
import time

time.sleep(5)  # Wait for 5 seconds to ensure the virtual environment is active
# Define headers for web scraping
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Class to fetch webpage content
class Website:
    def __init__(self, url):
        self.url = url
        self.text = ""
        self.title = "No title found"
        self.links = []

        try:
            response = requests.get(url, headers=headers, timeout=10)  # Set timeout to avoid hanging
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
            self.body = response.content
            self.soup = BeautifulSoup(self.body, 'html.parser')
            self.title = self.soup.title.string if self.soup.title else "No title found"

            # Clean up text by removing unnecessary elements
            if self.soup.body:
                for irrelevant in self.soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = self.soup.body.get_text(separator="\n", strip=True)

            # Extract links
            links = [link.get('href') for link in self.soup.find_all('a')]
            self.links = [urljoin(self.url, link) for link in links if link]

        except requests.exceptions.RequestException:
            # Catch all request-related errors (e.g., invalid URL, timeout, network issues)
            self.text = ""  # Empty text indicates a failure
            self.links = []

# Function to filter relevant links using Ollama
def filter_relevant_links(links):
    if not links:
        return []

    links_text = "\n".join(links)
    prompt = f"""
    Here is a list of URLs extracted from a company's website:

    {links_text}

    Your task:
    - Identify URLs that would be most relevant to include in a brochure about the company, such as About page, Careers/Job page, Services.
    - Ignore links to terms of service, privacy, login pages, or external sites.
    - Return only relevant URLs without any additional text or explanations.

    Respond with the filtered list.
    """

    response = None
    while response is None:  # Keep retrying until we get a valid response
        try:
            response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        except Exception as e:
            print(f"Error encountered: {e}. Retrying in 5 seconds...")
            time.sleep(15)  # Wait for 15 seconds before retrying

    relevant_links = response['message']['content'].split("\n")
    return [link.strip() for link in relevant_links if link.strip() and link.startswith("http")]

# Function to generate the brochure
def generate_brochure_from_contents(scraped_text):
    prompt = f"""
    Create a brochure based on the following website content:,
    {scraped_text}
    Your task is to generate a professional brochure without any picture, page number, cover, etc. that highlights key information about the company, such as:
    - The title should be company name only, nothing else.
    - Services
    - Products
    - Values & Mission
    - Webpage
    - Career (only if available, else discard this part from being included in the brochure)

    The brochure should be detailed and informative. Do not include your talk other than brochure input. It should be focused solely on the content provided in the prompt without introducing any irrelevant material or placeholders like '[Cover Page]', '[Insert Twitter Handle]', or similar.
    Do not mention where to insert pictures. Ensure all content is strictly from the provided context, and avoid referencing external sites or inserting placeholder links. Do not hallucinate text.
    The brochure should only contain the relevant information without any extraneous formatting or mentions of page numbers like 'Cover page', 'Company Logo', 'Page 1', 'Back Cover', etc.
    """

    system_prompt = """You are a helpful assistant tasked with generating a professional brochure from a company's web content. Follow these rules:
    1. Do not add unnecessary formatting (e.g., page numbers, cover page, or picture placeholders).
    2. Focus only on the company's relevant information.
    3. Discard any irrelevant content, especially external links, and avoid introducing content like 'Cover Page', 'Back Cover', or placeholders.
    4. Organize the information in a clear, concise manner and do not insert unnecessary page numbers, external links, or picture placeholders.
    5. No assumptions or hallucinations. If some sections are missing from the content, exclude them entirely.
    6. No disclaimers or commentary. Do not add phrases like "Here is your brochure" or "This content follows the rules."
    """

    response = None
    while response is None:  # Keep retrying until we get a valid response
        try:
            response = ollama.chat(model="llama3.2", messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ])
        except Exception as e:
            print(f"Error encountered: {e}. Retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying

    return response['message']['content']

# Convert to markdown format
def convert_to_markdown(content):
    markdown = ""
    lines = content.split('\n')
    
    for line in lines:
        if line.startswith("**"):
            markdown += f"## {line.strip('**')}\n"
        elif line.startswith("*"):
            markdown += f"- {line[2:]}\n"
        else:
            markdown += f"{line}\n"
    
    return markdown

# Function to process the URL and generate a brochure
def process_url(url):
    if not url.startswith("http"):
        url = "https://" + url  # Ensure URL starts with "http" or "https"

    # Show the initial message
    yield "<p style='text-align: center; font-size: 18px;'><br><b><b>🔄 Please wait, your brochure is being generated... 🔄</p>"

    # Fetch the website
    web = Website(url)

    # Reset the variables to avoid stale data
    filter_links = []  
    web_contents = []  

    # Check if the website returned valid content
    if not web.text.strip():
        yield "<p style='text-align: center; font-size: 18px;'><br><b><b>❌ Unable to fetch content. Please check the URL and try again. ❌</p>"
        return

    # Step 1: Get filtered links
    filter_links = filter_relevant_links(web.links)
    time.sleep(15)
    
    if not filter_links:  # If no relevant links are found, return an error message
        yield "<p style='text-align: center; font-size: 18px;'><br><b><b>❌ No relevant links found. Try again. ❌</p>"
        return

    # Step 2: Extract text from each relevant link
    #web_contents = []
    for link in filter_links:
        web_page = Website(link)  
        
        # Filter out lines with at most 3 words
        filtered_text = "\n".join(line for line in web_page.text.split("\n") if len(line.split()) > 3)

        if filtered_text.strip():
            web_contents.append((web_page.title, link, filtered_text))

    if not web_contents:  # No useful content extracted
        yield "<p style='text-align: center; font-size: 18px;'><br><b><b>❌ Extracted content is too short or irrelevant. Try again. ❌</p>"
        return

    # Step 3: Prepare text for Ollama
    scraped_text = "\n\n".join([f"Title: {title}\nLink: {link}\nContent: {text}" for title, link, text in web_contents])

    # Step 4: Generate brochure
    brochure = generate_brochure_from_contents(scraped_text)

    # Convert to Markdown
    markdown_brochure = convert_to_markdown(brochure)

    # Final output replaces "Please wait" message
    yield markdown_brochure

# Gradio Interface
with gr.Blocks(theme='monochrome') as iface:
    gr.Markdown(
        "<h1 style='text-align: center;'>Company Brochure Generator</h1>"
        "<p style='text-align: center;'>Enter a company website URL to generate a markdown-formatted brochure.</p>"
    )

    inp = gr.Textbox(label="Web-page URL", placeholder="Enter Website URL")
    btn = gr.Button("Generate Brochure")  
    out = gr.Markdown(label="Generated Brochure")

    btn.click(process_url, inputs=inp, outputs=out)

# Launch Gradio App
iface.launch(inbrowser=True)
 