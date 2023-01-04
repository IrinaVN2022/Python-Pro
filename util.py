def format_list(elements):
    html_text = '<ol>\n'
    for element in elements:
        li = '<li>' + element + '</li>\n'
        html_text += li
    html_text += '</ol>\n'
    return html_text
