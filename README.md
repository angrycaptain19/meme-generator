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

# CLI

The meme generator can also be run via a command line interface to generate meme images.
The script meme.py implements the CLI.
