from abc import ABC, abstractmethod
from typing import List

from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class for classes that ingest quote files
    in specific formats.
    """

    valid_extension = ''

    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        """Checks whether file extension is correct"""
        return (cls.valid_extension and type(path) == str and
                path.lower().endswith(cls.valid_extension))

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Reads a quote file and returns a list of quotes."""
        pass
