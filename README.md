# PageBriefly

## Overview

This project provides a modular Python solution for loading, processing, and summarizing textual data from specified URLs. It leverages various components of the `langchain` library, OpenAI's GPT models, and custom utilities to efficiently handle and summarize large volumes of text.

In addition, other alternatives such as scraping with BeautifulSoup and text processing with nltk and transformers have been explored (refer branches).

## Structure

The project is organized into a main script and a utility package (`utils`) containing several modules, each responsible for a specific part of the workflow:

- **`main.py`**: Orchestrates the entire text loading, processing, summarizing, and emailing workflow.
- **`utils/`**: A package containing modular utilities for the project.
  - **`config.py`**: Defines configuration, constants, and email settings.
  - **`data_loader.py`**: Handles loading data from URLs.
  - **`text_processing.py`**: Splits loaded text into manageable chunks.
  - **`document_management.py`**: Creates document objects from text chunks.
  - **`summarization.py`**: Summarizes the text using OpenAI's GPT models.
  - **`email_sender.py`**: Manages sending the summary via email.
  - **`email_content.py`**: Generates HTML content for emails.

## Setup

### Requirements

- Python 3.8+
- OpenAI API key (set as an environment variable `OPENAI_API_KEY`)
- Email settings for sending summaries (set the following environment variables):
  - `SENDER_EMAIL`: The email address from which summaries will be sent.
  - `SENDER_PASSWORD`: The app-specific password for the sender email account
  - `RECIPIENT_EMAIL`: The email address to which summaries will be sent.

### Installation

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Ensure you have set the necessary environment variables (`OPENAI_API_KEY`, `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECIPIENT_EMAIL`).

## Usage

To run the project, execute the `main.py` script:

```bash
python3 main.py
```

This will load the data from the URLs specified in `config.py`, process the text, summarize it, and send the summary via email to the specified recipient.

## Customization

You can customize the project by modifying the `config.py` file to include different URLs, adjust the text chunk size and overlap, change the OpenAI model used for summarization, or update the email settings for different sender or recipient addresses.