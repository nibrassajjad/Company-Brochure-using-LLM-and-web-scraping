# Download and Run in Windows (User-friendly mode)

The codes has been tested to be working on 

<img src="https://github.com/user-attachments/assets/6842589a-e622-4963-b0b9-6202b7946718" align="right" width="200" />
<img src="https://github.com/user-attachments/assets/66b1eea2-0d60-4d1f-9baa-cb7c1e5dfd1d" align="right" width="120" />
<img src="https://github.com/user-attachments/assets/a63eb989-a832-42b4-bb8e-194bfe7bc2da" align="right" width="150" />

**CPU:** AMD Ryzen 5, 3.59 GHz, 16 GB RAM 

**GPU:** NVIDIA GeForce RTX 2060

**Python Version:** 3.10.11 

**LLM Model:** Llama 3.2 (Size: 2 GB)

## How to start 

- If this is your first time setting up the program, complete **Step 1** through **Step 6**.

- For subsequent runs, just perform **Step 5** and **Step 6**.

## Step 1: Download & Install Python

- Download Python for Windows from the [Python website](python.org) .
- Install Python

Video tutorial on how to install Python:

[![Video Tutorial](https://img.youtube.com/vi/C3bOxcILGu4/0.jpg)](https://www.youtube.com/watch?v=C3bOxcILGu4)

## Step 2: Download & Install Llama 3.2

- Download Ollama for Windows from the [Ollama website](https://ollama.com/download)
- Install Llama 3.2 model by opening command prompt (cmd) and entering the command `ollama run llama3`
- Once the model is downloaded and the chatbot starts running, you can exit/close the command prompt.

Video tutorial on how to install Llama 3.2:

[![Video Tutorial](https://img.youtube.com/vi/LptVU0B6rt4/0.jpg)](https://www.youtube.com/watch?v=LptVU0B6rt4)

## Step 3: Download Python files from this Git folder

- Download `environment.py` and `brochure_v2.py` into the directory where you'll run the program.
- For this tutorial, we'll download the files to **E:/brochure/**.

![image](https://github.com/user-attachments/assets/9190c9fa-cc18-4b3b-a182-465e5cdbd690)

## Step 4: Setup virtual environment

To run the program, you need to install some dependency files that can be easily done with one line in command prompt.

**For tutorial I downloaded the python files in E:/brochure/** <img src="https://github.com/user-attachments/assets/350fdc2a-b748-452f-836d-1fee979378d4" align="right" width="300" />

- Open command prompt.
- Type & enter `E:` *(or whichever disk drive you saved the files in)*
- Type & enter `cd brochure` *(or whichever directory you saved the files in)*
- Type & enter `python environment.py`
- Wait till environment is completely setup. You will see the message "Dependencies Installed."<img src="https://github.com/user-attachments/assets/906e51ff-1cf9-42bf-9083-0f8e0ad31b80" align="right" width="300" />
- Close/exit the command prompt.

## Step 5: Turn on Ollama

- Search and open Ollama from your Windows Start menu.
- You will know Ollama is turned on when its icon appears in the taskbar’s notification area.
<img src="https://github.com/user-attachments/assets/aebeffeb-01d7-4b2b-ace9-5c3f489f3e2c" align="center" width="250" />
<img src="https://github.com/user-attachments/assets/c40dc0f7-21ae-402c-8c56-1d56ee0fe563" align="center" width="500" />

## Step 6: Run the Program!

- Open command prompt.
- Type & enter `E:` *(or whichever disk drive you saved the files in)*
- Type & enter `cd brochure` *(or whichever directory you saved the files in)*
- Type & Enter `python brochure_v2.py` in the command prompt.
- Wait for the program to start-up in your browser. It should appear like this:

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c448dfc-b88a-4e09-801a-d6619e6a3006" width="500" />
</p>

- Feel free to input any website. It should produce a brochure once the program has its processing completed.
- To exit the program, press Ctrl + Break/Pause on the command prompt.
- You can close the browser tab and exit the command prompt safely afterwards.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9eab5810-7d75-4baf-b28e-7f9a0707ee3c" width="500" />
</p>

## Limitations:

- Due to Llama 3.2 model's limitations, user might not get well-detailed content. You can try 2 to 3 times to see if you get a better brochure. If you want to try using other models, feel free to fork the repository and modify the code.
- The sub-links should have well-structured names that relate to the title of their respective pages to help the LLM make accurate decisions. (for example: `https://www.anthropic.com/careers` would work but not `https://www.anthropic.com/434121`)
- The brochure generation may suffer from hallucinated content due to the token limit of Llama 3.2 model. This happens when the context window overflows with the scraped content. 
- Abnormal results will be generated if you are not linking the main page of the website.
- Some websites are blocked from scrapping and you will get "❌ Unable to fetch content. Please check the URL and try again. ❌" message.
- Sometimes, the program might show "❌ No relevant links found. Try again. ❌" due to the LLM processing taking longer time in your local machine or failing to fetch links. 

## License:
This project is open-source and available under the MIT License.

## Author notes
If you liked this project, please leave a star! Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/nibras-sajjad/) if you would like to connect.












