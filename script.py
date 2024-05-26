import os
from googleapiclient.discovery import build


pr_title = os.getenv('PR_TITLE')
pr_body = os.getenv('PR_BODY')
pr_diff = os.getenv('PR_DIFF')



# API key for accessing the Google Docs API
API_KEY = 'AIzaSyAZ73ggefuQndZg9i1zodPb-TykfdoxRGc'

# ID of the Google Doc you want to update
DOCUMENT_ID = '1hELcJdxkvA5_-6jGfdHjoYYdeEX5dmioYkL2Y8CzsVU'

def main():
    # Build the service
    service = build('docs', 'v1', developerKey=API_KEY)

    # Get the document content
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()

    # Modify the document content
    content = doc.get('body').get('content')
    new_content = "Hello, this is an updated content!"
    content.append({'paragraph': {'elements': [{'textRun': {'content': new_content}}]}})

    # Update the document
    service.documents().batchUpdate(
        documentId=DOCUMENT_ID,
        body={'requests': [{'insertText': {'location': {'index': len(content) - 1}, 'text': new_content}}]}
    ).execute()

if __name__ == '__main__':
    main()


