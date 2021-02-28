from typing import List
from csv import reader

import pandas as pd
from docx.opc.exceptions import PackageNotFoundError

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Ingests csv files that contain quotes.
    Each line in the file has a quote followed by the author of the quote.
    """

    valid_extension = '.csv'

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a csv file and returns a list of quotes."""
        if not cls.can_ingest(path):
            raise ValueError('Wrong file format')

        try:
            df = pd.read_csv(path)
            results = df.apply(lambda x: QuoteModel(x.body, x.author), axis=1)
            return list(results)
        except AttributeError:
            raise ValueError('Wrong file format')
        except PackageNotFoundError:
            raise FileNotFoundError
