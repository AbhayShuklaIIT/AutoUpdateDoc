import os

def main():
    pr_title = os.getenv('PR_TITLE')
    pr_body = os.getenv('PR_BODY')
    pr_diff = os.getenv('PR_DIFF')

    print(f"PR Title: {pr_title}")
    print(f"PR Body: {pr_body}")
    print(f"PR Diff: {pr_diff}")

if __name__ == "__main__":
    main()
