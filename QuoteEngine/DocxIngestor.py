from typing import List
from docx import Document
from docx.opc.exceptions import PackageNotFoundError


from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Ingests docx files that contain quotes.
    Each line in the file has a quote followed by the author of the quote.
    """

    valid_extension = '.docx'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a docx file and returns a list of quotes."""
        if not cls.can_ingest(path):
            raise ValueError('Wrong file format')

        try:
            document = Document(path)
            lines = [p.text for p in document.paragraphs]
            return [QuoteModel.from_line(line)
                       for line in lines if line != '']
        except PackageNotFoundError:
            raise FileNotFoundError(
                f'File not found or wrong format: {path}')
