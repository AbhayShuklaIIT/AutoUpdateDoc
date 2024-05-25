import os

def main():
    pr_number = os.getenv('PR_NUMBER')
    pr_title = os.getenv('PR_TITLE')
    pr_body = os.getenv('PR_BODY')
    pr_user = os.getenv('PR_USER')

    print(f"PR Number: {pr_number}")
    print(f"PR Title: {pr_title}")
    print(f"PR Body: {pr_body}")
    print(f"PR User: {pr_user}")

    # Your code to process the PR data
    # ...

if __name__ == "__main__":
    main()