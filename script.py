import os

def main():
    pr_number = os.getenv('PR_NUMBER')
    pr_title = os.getenv('PR_TITLE')
    pr_body = os.getenv('PR_BODY')
    pr_user = os.getenv('PR_USER')
    pr_files = os.getenv('PR_FILES')

    print(f"PR Number: {pr_number}")
    print(f"PR Title: {pr_title}")
    print(f"PR Body: {pr_body}")
    print(f"PR User: {pr_user}")
    print(f"PR Files: {pr_files}")

    # Convert the PR_FILES string to a list
    pr_files_list = pr_files.split()

    # Your code to process the PR data and files
    # ...
    for file in pr_files_list:
        print(f"Modified file: {file}")

if __name__ == "__main__":
    main()
    