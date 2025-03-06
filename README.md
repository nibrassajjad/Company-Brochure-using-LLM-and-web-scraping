# Company Brochure using LLM (Llama 3.2) and Web-scraping

This project scrapes web pages, extracts relevant company information, and generates a **professional brochure** using a LLM model. It filters and structures extracted data to create concise and informative content

<p align="center">
  <img src="https://github.com/user-attachments/assets/5c78fb22-4846-482f-8d76-a1c031e07208" width="800" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/ba8f3b93-6bec-4378-a3e6-350347b4b424" width="1000" />
</p>

# Features
User just insert link to main page! The code will scrape through all the links in that web page and extract:

- Page titles

- Page URLs

- Main textual content

- Filters out irrelevant content with help of LLM

- Combines extracted data into a structured format

- Uses LLM to generate a professional brochure

- Ensures the generated brochure is well-structured, concise, and relevant

- An User-friendly setup mode that enables you to interact with the program via an UI!

# How to use

## Option 1: Download and Run in your Computer (User-friendly mode)
Go to [`Download an Run`](https://github.com/nibrassajjad/Company-Brochure-using-LLM-and-web-scraping/tree/main/Download%20and%20Run) folder and follow instructions inside the folder.

## Option 2: In Jupyter Notebook/Jupyter Lab (Debug mode)
Open file [`webpagebrochure.ipynb`](https://github.com/nibrassajjad/Company-Brochure-using-LLM-and-web-scraping/blob/main/webpagebrochure.ipynb) and run through the steps with instructions inside. **If you are using downloaded Llama 3.2 model, make sure it is turned on/activated in your computer.**

# Installation prequisites
- **Python 3.x** [`(Click here for video guide)`](https://youtu.be/C3bOxcILGu4?si=xK9DHOaXPhrEGP1o)
- **Required Python libraries:**
  beautifulsoup4 ollama urljoin requests gradio time
- **Llama 3.2** [`(Click here for video guide)`](https://www.youtube.com/watch?v=LptVU0B6rt4)


You can experiment with other LLM models instead of using Ollama (e.g. GPT-4). For quick guide on how to load models using API key you can use **Step 4b** of my code in another repository as reference:

https://github.com/nibrassajjad/Webpage-Descriptor-using-LLM/blob/main/Webpage%20Descriptor.ipynb

# Limitations
This is an experimental model in its early stages, so it may have some overlooked limitations. If you encounter any issues, feel free to reach out.

Known limitations:
- If you are using the coded Llama 3.2 model, you might get not well-detailed content due to model's limitations. You can retry to see if you can get better brochure.
- The links should have well-structured names that relate to the title of their respective pages to help the LLM make accurate decisions.
- If you're using the offline Llama 3.2 model, the brochure generation may suffer from hallucinated content due to the token limit. This happens when the context window overflows with the scraped content. Using a more powerful LLM, like GPT-4o mini, could help mitigate this issue.
- Abnormal results will be generated if you are not linking the main page of the website.

# License
This project is open-source and available under the MIT License.

# Author notes
If you liked this project, please leave a star! Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/nibras-sajjad/) if you would like to connect.



