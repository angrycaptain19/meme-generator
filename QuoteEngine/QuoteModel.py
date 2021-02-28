class QuoteModel:
    '''Represents a quote'''

    def __init__(self, body: str, author: str):
        if type(body) != str or body == '':
            raise ValueError('Quote needs to be a nonempty string')

        if type(author) != str or author == '':
            raise ValueError('Author needs to be a non-empty string')

        self.body = body.strip()
        self.author = author.strip()

    @classmethod
    def from_line(cls, line: str):
        """Extracts a quote from a one-line string."""
        try:
            body, author = line.rstrip().split('-')

            return QuoteModel(body.replace('"', ''), author.replace('"', ''))
        except (ValueError, AttributeError):
            raise ValueError(
                'Line needs to have body and author separated by "-"')

    def __str__(self):
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        return f'<body={self.body}, author={self.author}>'
