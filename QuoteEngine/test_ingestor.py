import unittest

from Ingestor import Ingestor
from CSVIngestor import CSVIngestor
from TextIngestor import TextIngestor
from DocxIngestor import DocxIngestor
from PDFIngestor import PDFIngestor


class TestIngestor(unittest.TestCase):
    # CSV file tests
    def test_can_ingest_csv(self):
        self.assertTrue(CSVIngestor.can_ingest("myfile.csv"))
        self.assertTrue(CSVIngestor.can_ingest("myfile.CSV"))
        self.assertFalse(CSVIngestor.can_ingest("myfile"))
        self.assertFalse(CSVIngestor.can_ingest(None))

    def test_parse_csv_simple(self):
        result = CSVIngestor.parse('../_data/SimpleLines/SimpleLines.csv')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2].body, 'Line 3')
        self.assertEqual(result[3].author, 'Author 4')

    def test_parse_csv_dog(self):
        result = CSVIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')
        self.assertEqual(len(result), 2)

    def test_parse_csv_fakefile(self):
        with self.assertRaises(FileNotFoundError):
            _ = CSVIngestor.parse('fakefile.csv')

    def test_parse_csv_wrongformat(self):
        with self.assertRaises(ValueError):
            _ = CSVIngestor.parse('../_data/DogQuotes/DogQuotesTXT.txt')

    # TXT file tests
    def test_can_ingest_text(self):
        self.assertTrue(TextIngestor.can_ingest("myfile.txt"))
        self.assertTrue(TextIngestor.can_ingest("myfile.TXT"))
        self.assertFalse(TextIngestor.can_ingest("myfile.csv"))
        self.assertFalse(TextIngestor.can_ingest(None))

    def test_parse_text_simple(self):
        result = TextIngestor.parse('../_data/SimpleLines/SimpleLines.txt')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2].body, 'Line 3')
        self.assertEqual(result[3].author, 'Author 4')

    def test_parse_text_dog(self):
        result = TextIngestor.parse('../_data/DogQuotes/DogQuotesTXT.txt')
        self.assertEqual(len(result), 2)

    def test_parse_text_fakefile(self):
        with self.assertRaises(FileNotFoundError):
            _ = TextIngestor.parse('fakefile.txt')

    def test_parse_text_wrongformat(self):
        with self.assertRaises(ValueError):
            _ = TextIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')

    # DOCX file tests
    def test_can_ingest_docx(self):
        self.assertTrue(DocxIngestor.can_ingest("myfile.docx"))
        self.assertTrue(DocxIngestor.can_ingest("myfile.DOCX"))
        self.assertFalse(DocxIngestor.can_ingest("myfile.csv"))
        self.assertFalse(DocxIngestor.can_ingest(None))

    def test_parse_docx_simple(self):
        result = DocxIngestor.parse('../_data/SimpleLines/SimpleLines.docx')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2].body, 'Line 3')
        self.assertEqual(result[3].author, 'Author 4')

    def test_parse_docx_dog(self):
        result = DocxIngestor.parse('../_data/DogQuotes/DogQuotesDOCX.docx')
        self.assertEqual(len(result), 4)

    def test_parse_docx_fakefile(self):
        with self.assertRaises(FileNotFoundError):
            _ = DocxIngestor.parse('fakefile.docx')

    def test_parse_docx_wrongformat(self):
        with self.assertRaises(ValueError):
            _ = DocxIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')

    # PDF file tests
    def test_can_ingest_pdf(self):
        self.assertTrue(PDFIngestor.can_ingest("myfile.pdf"))
        self.assertTrue(PDFIngestor.can_ingest("myfile.PDF"))
        self.assertFalse(PDFIngestor.can_ingest("myfile.csv"))
        self.assertFalse(PDFIngestor.can_ingest(None))

    def test_parse_pdf_simple(self):
        result = PDFIngestor.parse('../_data/SimpleLines/SimpleLines.pdf')
        self.assertEqual(len(result), 5)
        self.assertEqual(result[2].body, 'Line 3')
        self.assertEqual(result[3].author, 'Author 4')

    def test_parse_pdf_dog(self):
        result = PDFIngestor.parse('../_data/DogQuotes/DogQuotesPDF.pdf')
        self.assertEqual(len(result), 3)

    def test_parse_pdf_fakefile(self):
        with self.assertRaises(FileNotFoundError):
            _ = PDFIngestor.parse('fakefile.pdf')

    def test_parse_pdf_wrongformat(self):
        with self.assertRaises(ValueError):
            _ = PDFIngestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')

    # TXT/CSV/PDF/DOCx file tests
    def test_can_ingest(self):
        self.assertTrue(Ingestor.can_ingest('myfile.PDF'))
        self.assertFalse(Ingestor.can_ingest('myfile.HTML'))
        self.assertFalse(Ingestor.can_ingest(None))

    def test_parse_fakefile(self):
        with self.assertRaises(FileNotFoundError):
            _ = Ingestor.parse('fakefile.pdf')

    def test_parse_no_extension(self):
        with self.assertRaises(ValueError):
            _ = Ingestor.parse('fakefile')


if __name__ == '__main__':
    unittest.main()
