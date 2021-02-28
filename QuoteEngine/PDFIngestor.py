from typing import List
import subprocess
import os
import tempfile

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """
    Ingests pdf files that contain quotes.
    Each line in the file has a quote followed by the author of the quote.
    """

    valid_extension = '.pdf'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a csv file and returns a list of quotes."""

        if not cls.can_ingest(path):
            raise ValueError('Wrong file format')

        try:
            _, output_file = tempfile.mkstemp(suffix='.txt')

            p = subprocess.run(
                ['pdftotext', '-layout', path, output_file], capture_output=True)

            if p.stderr.startswith(b'I/O Error'):
                raise FileNotFoundError(f'File not found: {path}')

            if p.stderr.startswith(b'Syntax Warning: May not be a PDF file'):
                raise ValueError(p.stderr)

            return TextIngestor.parse(output_file)
        except FileNotFoundError:
            raise FileNotFoundError(
                'Could not find the "pdftotext" utility. Please add it to the path.')
        finally:
            if os.path.isfile(output_file):
                os.remove(output_file)
