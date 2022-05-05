import stylecloud
from stop_words import get_stop_words
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

filePdf = "unTexto.pdf"
txtPdf = "untexto2.txt"
device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
interpreter = PDFPageInterpreter(PDFResourceManager(), device)
doc = PDFDocument()
parser = PDFParser(open(filePdf, 'rb'))
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize()
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    with open(txtPdf, 'w', encoding="utf-8") as fw:
        print("num page:{}".format(len(list(doc.get_pages()))))
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    results = x.get_text()
                    fw.write(results)

irrelevantWords = get_stop_words('spanish')
stylecloud.gen_stylecloud(file_path=txtPdf,
                          icon_name='fab fa-apple',
                          colors='yellow',
                          background_color='black',
                          output_name='output.png',
                          custom_stopwords=irrelevantWords
                          )

