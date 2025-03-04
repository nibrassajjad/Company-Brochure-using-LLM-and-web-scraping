import os
import sys
import subprocess

# Define environment name
env_name = "mycompanybrochure_v2"

# Check if the environment exists
if not os.path.exists(env_name):
    print(f"🔧 Creating virtual environment: {env_name}...")
    subprocess.run([sys.executable, "-m", "venv", env_name])
    print("✅ Virtual environment created.")
else:
    print("✅ Virtual environment already exists.")

# Define paths for Python and pip inside the environment
pip_executable = os.path.join(env_name, "Scripts", "pip") if os.name == "nt" else os.path.join(env_name, "bin", "pip")

# Required dependencies
dependencies = ["gradio", "requests", "beautifulsoup4", "ollama"]

# Install dependencies
print("🔍 Checking & installing dependencies...")
subprocess.run([pip_executable, "install"] + dependencies)
print("✅ Dependencies installed.")

# Pause to let the user read the output
# input("Press Enter to exit...")
