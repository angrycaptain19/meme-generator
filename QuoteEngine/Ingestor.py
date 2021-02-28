from typing import List

from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """
    Ingests csv/txt/docx/pdf files that contain quotes.
    Each line in the file has a quote followed by the author of the quote.

    This class dispatches to a specialized class for each file format.
    """

    classMapping = {
        'csv': CSVIngestor,
        'txt': TextIngestor,
        'docx': DocxIngestor,
        'pdf': PDFIngestor,
    }

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        try:
            extension = path.split('.')[-1].lower()
            return extension in cls.classMapping.keys()
        except KeyError:
            # file has no extension
            return False
        except AttributeError:
            # File path is not a string
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a file and returns a list of quotes."""
        try:
            extension = path.split('.')[-1].lower()
            return cls.classMapping[extension].parse(path)
        except KeyError:
            raise ValueError(f'file has no extension {path}')
