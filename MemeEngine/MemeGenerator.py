import tempfile
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError


class MemeGenerator:
    def __init__(self, output_dir: str):
        """
        Create a MemeGenerator

        Argument:
            output_dir {str} -- the directory for storing pictures.
        """
        self.output_dir = output_dir

        if not Path(output_dir).exists():
            os.mkdir(output_dir)
            print(f'MemeGenerator created directory: {output_dir}')

        try:
            fontFile = os.path.dirname(__file__) + '/fonts/Roboto-Black.ttf'
            self.font_quote = ImageFont.truetype(fontFile, size=30)
            self.font_author = ImageFont.truetype(fontFile, size=15)
        except OSError:
            raise FileNotFoundError(
                'The font for the quote in the images is not found.')

    def make_meme(self, in_path: str, quote: str, author: str, width: int = 500) -> str:
        """
        Create a meme With a quote

        Arguments:
            in_path {str} -- the file location for the input image.
            text {str} -- the quote text.
            author {str} -- the author of the quote.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """

        try:
            img = Image.open(in_path)
        except FileNotFoundError:
            raise FileNotFoundError(f'Image file {in_path} does not exit')
        except UnidentifiedImageError:
            raise FileNotFoundError(
                f'Image path, {in_path} cannot be processed')

        if width is None or width > 500:
            width = 500

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        try:
            _, output_file = tempfile.mkstemp(
                suffix='.jpg', dir=self.output_dir)
        except FileNotFoundError:
            raise FileNotFoundError(
                f'Output directory {self.output_dir} does not exist')

        if quote is not None:
            draw = ImageDraw.Draw(img)
            draw.text((10, 10), quote, font=self.font_quote, fill='yellow')

        if author is not None:
            draw = ImageDraw.Draw(img)
            draw.text((10, 40), '- ' + author,
                      font=self.font_author, fill='yellow')

        img.save(output_file)
        return self.output_dir + '/' + Path(output_file).name


if __name__ == '__main__':
    meme = MemeGenerator('./tmp')
    path = meme.make_meme('../_data/photos/dog/xander_1.jpg',
                          'To be or not to be', 'Shakespeare', 500)
