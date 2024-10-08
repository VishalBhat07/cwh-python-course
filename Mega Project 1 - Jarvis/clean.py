import re
import html2text

def clean_text(text):
    # Convert HTML to plain text
    html_to_text = html2text.HTML2Text()
    html_to_text.ignore_links = True
    text = html_to_text.handle(text)

    # Remove Markdown formatting (simple removal of common Markdown symbols)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Remove bold formatting
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Remove italic formatting
    text = re.sub(r'\#\s*', '', text)               # Remove headings
    text = re.sub(r'\n+', ' ', text)                 # Remove new lines and multiple spaces
    text = re.sub(r'\s+', ' ', text)                 # Collapse multiple spaces to a single space

    return text.strip()