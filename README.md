# AI Webpage Summarizer (Gemini 2.0 Flash)

This project is a simple web application that summarizes the content of any public web page using Google's Gemini 2.0 Flash generative AI model. The app is built with [Streamlit](https://streamlit.io/) for the user interface and leverages the Gemini API for fast, high-quality summarization.

## Features
- Enter any URL and get a concise summary of the page content
- Uses Gemini 2.0 Flash for state-of-the-art summarization
- Fast and easy-to-use Streamlit interface

## Live Demo
Try the app instantly here: [AI Webpage Summarizer Streamlit App](https://mainpy-gltypunvojvqwntzq288sx.streamlit.app/)

## Getting Started

### Prerequisites
- Python 3.8+
- A Google Gemini API key (see [Google Generative AI documentation](https://ai.google.dev/))

### Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd Zocket
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key as an environment variable:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

### Running Locally
```bash
streamlit run main.py
```

## Usage
- Enter the URL of any public web page in the input box.
- Wait a few seconds for the summary to be generated.
- Read the concise summary generated by Gemini 2.0 Flash.

## Project Structure
- `main.py` - Streamlit app and core logic
- `requirements.txt` - Python dependencies

## License
This project is for educational/demo purposes.
