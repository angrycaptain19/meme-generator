from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """
    Ingests docx files that contain quotes.
    Each line in the file has a quote followed by the author of the quote.
    """

    valid_extension = '.txt'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a txt file and returns a list of quotes."""
        if not cls.can_ingest(path):
            raise ValueError('Wrong file format')

        result = []
        with open(path, 'r') as f:
            for row in f:
                if row.rstrip() != '':
                    try:
                        body, author = row.rstrip().split('-')
                        result.append(QuoteModel(body.replace(
                            '"', ''), author.replace('"', '')))
                    except ValueError:
                        raise ValueError('Wrong file format')

        return result
