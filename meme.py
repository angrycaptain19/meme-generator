import os
import random
import argparse

from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeGenerator import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme

    Arguments:
        path {str} -- the path to the image file
        body {str} -- the quote body to be added to the image
        author {str} -- the author of the quote
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate a meme with a quote.')
    parser.add_argument('--path', type=str, default=None,
                        help='path to the image file.')
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image.')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image.')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
