import re


def parse(markdown):
    """Convert markdown text to HTML."""
    # Process bold text (strong)
    markdown = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', markdown)
    
    # Process italic text (em)
    markdown = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', markdown)
    
    # Process list items (but don't wrap in <ul> yet)
    markdown = re.sub(r'^\* (.*?$)', r'<li>\1</li>', markdown, flags=re.M)
    
    # Wrap consecutive list items with <ul> tags
    markdown = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', markdown, flags=re.S)
    
    # Process headers (h1-h6)
    for level in range(6, 0, -1):
        pattern = r'^{} (.*?$)'.format('#' * level)
        markdown = re.sub(pattern, r'<h{0}>\1</h{0}>'.format(level), markdown, flags=re.M)
    
    # Process paragraphs (lines not starting with a tag)
    markdown = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', markdown, flags=re.M)
    
    # Remove newlines
    markdown = re.sub(r'\n', '', markdown)
    
    return markdown
