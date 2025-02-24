# **AI Ghostwriter**

AI Ghostwriter is a powerful tool designed to assist with generating content in real-time using a mix of local and online LLMs (Large Language Models). The project integrates models such as Mistral-7B, TinyLlama, Whisper, and others to create an efficient system for automatic content generation. It is built to function as a local AI assistant that can be used for a variety of applications such as blog writing, story creation, and more.

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Setup](#setup)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Models](#models)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Overview**

AI Ghostwriter utilizes a combination of **offline models** (e.g., Mistral-7B) and **online models** (e.g., Hugging Face’s TinyLlama and Whisper) to generate high-quality content with minimal effort. With the use of real-time generation, focus tools, and AI-driven assistance, it aims to streamline the creative writing process.

Key components include:
- **Real-time typing simulation** for automatic content generation.
- **Offline local models** to maintain privacy and reduce reliance on online services.
- **Online model access** for larger and more optimized models like TinyLlama and Whisper.
- **User-friendly prompts** to guide content creation.

---

## **Features**
- **Offline and Online Model Integration**: AI Ghostwriter can seamlessly switch between local and online models to balance between model size and performance.
- **Real-Time Typing Simulation**: Simulates human-like typing, adding a realistic touch to the content generation process.
- **Multiple Models Support**: Incorporates various LLMs (Large Language Models) like Mistral-7B, TinyLlama, Whisper, and more.
- **Multi-Step Content Generation**: Iterative content refinement using real-time feedback and corrections.
- **Focus and Timing Mechanism**: Allows users to configure delays for screen focus and adjust timing for content creation.
- **Customizable for Various Use Cases**: Suitable for blog writing, story generation, product descriptions, and more.
- **Easy Model Management**: Easily add, update, or replace models as per project needs.

---

## **Installation**

To run AI Ghostwriter locally, you need to install several dependencies. Follow the instructions below:

### **Requirements**
- Python 3.11 or later
- Virtual environment (Recommended)
- Hugging Face API key for model access
- Pytorch and Transformers libraries

### **Steps**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ethandlr/AI-Ghostwriting.git
   cd AI-Ghostwriting
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**:
   - For **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - For **Mac/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your Hugging Face API Key** (for online model access):
   - Add your Hugging Face API key in your environment variables or set it as an argument in the scripts:
     ```bash
     export HF_API_KEY="your_key_here"
     ```

6. **Download models** (This is handled by the script `download_models.py`, so simply run it):
   ```bash
   python download_models.py
   ```

---

## **Setup**

After completing the installation, you can set up and configure the models and settings.

### **Configuring the Models**

In the `config.py` file, define your paths for the models you want to use, including any local paths for offline models. For example:

```python
# Local models path configuration
LOCAL_MODEL_PATH = "path/to/local_model"
ONLINE_MODEL_PATH = "path/to/online_model"
```

Ensure you have the correct paths for your models (either local or Hugging Face).

---

## **Usage**

### **Running the AI Ghostwriter**

To start generating content, use the main script:

```bash
python main.py
```

This will start the content generation process. You’ll be prompted for the type of content you want to generate (e.g., blog post, story, product description).

#### **Example:**
```bash
Enter a prompt (type 'exit' to quit): Write a blog post about Artificial Intelligence in Healthcare
Generated Text:
Artificial Intelligence (AI) is revolutionizing healthcare in ways we could never have imagined just a few decades ago...
```

---

## **Project Structure**

Here’s the project structure and purpose of each file:

```
AI-Ghostwriting/
│
├── .venv/                # Virtual environment
├── models/               # Models for text generation
├── scripts/              # Custom scripts for downloading and managing models
│   ├── download_models.py
│   └── model_manager.py
├── config.py             # Configuration settings (e.g., model paths)
├── main.py               # Main program to interact with the Ghostwriter
├── auto_typing.py        # Typing simulation for content generation
├── README.md             # Project documentation
└── requirements.txt      # Dependencies for the project
```

---

## **Models**

AI Ghostwriter integrates the following models:

1. **Mistral-7B**: A powerful 7-billion parameter model for high-quality text generation.
2. **TinyLlama**: A lightweight 1.1B parameter model for quick responses and smaller applications.
3. **Whisper**: A state-of-the-art model for automatic speech recognition.
4. **Customizable with Hugging Face Models**: Use any available model from Hugging Face (depending on size and purpose).

---

## **Contributing**

If you'd like to contribute to the AI Ghostwriter project, follow these steps:

1. Fork the repository.🍴
2. Clone your fork locally.🍴
3. Create a new branch:🌿
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit:🚼
   ```bash
   git commit -m "Add feature"
   ```
5. Push your changes:🏃‍➡️
   ```bash
   git push origin feature-name
   ```
6. Submit a pull request to the original repository.🏃

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.❤️
