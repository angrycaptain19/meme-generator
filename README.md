This project was created as part of Udacity's Intermediate Python nanodegree.
It contains a flask server and the front end for a meme generator.

The meme generator combines an image with a quote. The quotes are ingested from
various document types: docx, pdf, txt, and csv. The images are in jpg format.

Generated meme images are stored in a folder that can be specified as parameter.

# SETUP

The project requires the binary pdftotext and expects this binary to be included
in the path variable. The download is here: https://www.xpdfreader.com/download.html

The flask service can be run from the root directory using:

```
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload
```

This system uses the following libraries:

- Flask: this runs the web/API server.
- pandas: this is used to ingest csv files with quotes.
- Pillow: this is used to process images
- python-docx: this is used to ingest word documents with quotes
- requests: this is used to fetch images from 3rd party web sites

These dependencies are listed in `requirements.txt' and can be installed using:

```
pip install -r requirements.txt
```

# CLI

The project contains a simple cli which can be run from the terminal by invoking python3 meme.py

The script takes three optional CLI arguments:

- --body a string quote body
- --author a string quote author
- --path an image path

The script returns a path to a generated image. If any argument is not defined, a random selection is used.
