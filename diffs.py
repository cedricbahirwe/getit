#!/usr/bin/env python3
import subprocess
from prompting import *


def is_git_repo(directory: str):
    """Check if the provided directory is a git repository."""
    try:
        subprocess.run(['git', '-C', directory, 'rev-parse', '--is-inside-work-tree'],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def run_git_diff(directory: str):
    """Run git diff in the specified directory and return the output."""
    try:
        result = subprocess.run(['git', '-C', directory, 'diff'], check=False,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()  # Return the git diff output, if any.
    except subprocess.CalledProcessError as e:
        return None


def save_diff_to_file(diff_output: str):
    """Save the git diff output to a text file in the specified directory."""
    # file_path = os.path.join(directory, 'diff_output.txt')
    desktop_path = '/Users/cedricbahirwe/Desktop/diff_output.txt'
    with open(desktop_path, 'w') as file:
        file.write(diff_output)
    return desktop_path


def commit_to_repo(directory: str, commit_message: str):
    """Commit the changes with the provided commit message."""
    try:
        subprocess.run(['git', '-C', directory, 'add', '.'],
                       check=True)  # Stage all changes
        subprocess.run(['git', '-C', directory, 'commit',
                       '-m', commit_message], check=True)
        print(f"\nChanges committed message: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes: {e}")


def suggest_commit_message(directory: str, diff_content: str):
    """Suggest 3 commit messages and allow the user to pick or enter their own, then commit."""
    # question = f"Suggest 3 commit messages based on the diffs provided below.\n Just return an array of 3 strings, each message should be separated by \n and not have quote around and not be numbered: \n\n {
    # diff_content}"
    question = f"Based on the diffs provided below, suggest exactly 3 concise and meaningful commit messages. Each commit message should be on a new line and formatted as plain text. Do not include numbers, quotes, or any additional characters in the messages. Return only the commit messages as an array of 3 plain text strings.\n\n {
        diff_content}"
    commit_messages = ask_question(question)

    print("\nSuggested commit messages:")
    for i, msg in enumerate(commit_messages, 1):
        print(f"{i}. {msg}")
    print(f"{len(commit_messages)+1}. Enter your own commit message")
    print(f"{len(commit_messages)+2}. Exit")

    # Get user choice
    choice = input("\nChoose an option (1-5): ").strip()

    if choice in ['1', '2', '3']:
        selected_message = commit_messages[int(choice)-1]
        print(f"\nSelected commit message: {selected_message}")
        commit_to_repo(directory, selected_message)
    elif choice == '4':
        custom_msg = input("\nEnter your custom commit message: ").strip()
        print(f"\nYour custom commit message: {custom_msg}")
        commit_to_repo(directory, custom_msg)
    elif choice == '5':
        print("Exiting without committing.")
    else:
        print("Invalid option. Exiting.")
