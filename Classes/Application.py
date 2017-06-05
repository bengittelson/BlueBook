import re


class Application:
    def __init__(self, inFile):
        self.fileName = inFile
        self.idNum = None
        self.text = None
        self.relText = None

    #get text from a pdf using PyPDF2
    def getTextFromPDF(self):
        import PyPDF2
        myPDFObj = open(self.fileName, 'rb')
        myReader = PyPDF2.PdfFileReader(myPDFObj)

        #extract text from each page
        pages = []
        for pageNum in range (0, myReader.numPages):
            pageObject = myReader.getPage(pageNum)
            pageText = pageObject.extractText()
            pages.append(pageText)
        self.text = pages
        #print self.text

    #NOTE: This won't work unless you can get the updated version of slate.
    def getTextWithSlate(self):
        from pdfminer.pdfdocument import PDFDocument
        import slate
        with open(self.fileName) as myFile:
            myText = slate.PDF(myFile)
        print myText

    def getTextWithTextract(self):
        import textract
        myText = textract.process(self.fileName, method='pdfminer', encoding='ascii')
        # myText = myText.split('\n')
        # for line in myText:
        #     print line
        myText.strip('\n')
        self.text = str(myText)

    #may need an abstract class for scalability: https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
    def getRelevantText(self):
        begin = re.compile(r"\n2017 Joint.* ")
        self.relText = re.match(begin, self.text)
        print self.relText

    def getID(self):
        id = re.compile('\n\n2848-1L')
        # id = re.compile(r"\d{4}\s?.\s?dL")
        print id.search(self.text).string
        self.idNum = id.search(self.text)
        print self.idNum


