from nltk.tokenize import sent_tokenize

def generate_html_email_body(url, summary_text):
    introduction_sentence = f"The following is a brief of the given URL: {url}"

    sentences = sent_tokenize(summary_text)
    summary_as_bullets = "".join([f"<li>{sentence.strip()}</li>" for sentence in sentences if sentence.strip() != ''])

    email_body = f"""
    <html>
        <body>
            <p>{introduction_sentence}</p>
            <ul>
                {summary_as_bullets}
            </ul>
        </body>
    </html>
    """
    return email_body
