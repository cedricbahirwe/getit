import os
from dotenv import load_dotenv
from diffs import *
import sys

load_dotenv()


def main():
    """Main function to check if git repo, run git diff, and handle output."""
    # Use the directory passed as an argument or the current working directory
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist. Exiting.")
        return

    if not is_git_repo(directory):
        print(f"'{directory}' is not a git repository. Exiting.")
        return

    diff_output = run_git_diff(directory)
    if not diff_output:
        print("No changes detected. Exiting.")
        return

    # For DEBUG purpose
    # file_path = save_diff_to_file(diff_output)
    # print(f"Git diff output saved to: {file_path}")

    # Suggest commit messages
    suggest_commit_message(directory, diff_output)


if __name__ == '__main__':
    main()
