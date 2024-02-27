def generate_html_email_body(url, summary_text):
    introduction_sentence = f"The following is a brief of the given URL: {url}"
    summary_as_bullets = "".join([f"<li>{sentence.strip()}</li>" for sentence in summary_text.split('\n') if sentence.strip() != ''])

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
