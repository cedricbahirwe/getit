
# GetIt Project

## Overview
GetIt is a Python-based tool designed to simplify the process of reviewing and committing changes in a Git repository.

The project detects changes in the repository, generates suggested commit messages using an AI-powered prompt system, and allows users to commit their changes with minimal effort.

## Files and Structure

- **main.py**: The main entry point that checks if the current directory is a Git repository, runs `git diff` to find changes, and triggers the commit process.
- **commiter.py**: Contains functions to interact with Git, such as checking if a directory is a Git repository, running `git diff`, and committing changes with a selected or custom commit message.
- **prompter.py**: Uses OpenAI's API to generate commit message suggestions based on the changes detected in the repository.
- **.gitignore**: Ensures that certain files and directories are ignored by Git.
- **requirements.txt**: Lists the necessary Python libraries for running the project.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
   ```bash
   git clone git@github.com:cedricbahirwe/getit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd getit-master
   ```
3. Run the project:
   ```bash
   python main.py
   ```

   The script will:
   - Check if the current directory is a Git repository.
   - Run `git diff` to detect changes.
   - Generate commit message suggestions using AI.
   - Allow you to select or input a custom commit message.
   - Commit the changes.

## Requirements

This project requires Python 3.x and the following dependencies listed in `requirements.txt`:

- OpenAI API (for generating commit messages)
- Python-dotenv (for loading environment variables)
- Tiktoken (tokenization for handling prompts)

Make sure to set up your OpenAI API key in a `.env` file as follows:

```plaintext
OPENAI_API_KEY=your-api-key
```
