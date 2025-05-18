import codecs

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            continue
        elif not inside_tag:
            text += char

    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    final_text = '\n'.join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)

delete_html_tags('draft.html')
