# pdf_reader.py

import fitz # for importing PyMuPDF

def read_pdf(path:str):
    doc=fitz.open(path)
    # text={}
    text=""
    lnk=[]
    for page in doc:
        # text[page.number]=page.get_text()
        text+=page.get_text()
        for link in page.get_links():
            if "uri" in link:
                lnk.append(link["uri"])
    doc.close()
    return text, lnk