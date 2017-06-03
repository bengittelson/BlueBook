class Application:
    def __init__(self, inFile):
        self.fileName = inFile
        self.idNum = None
        self.text = None

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

    #
    def getTextWithSlate(self):
        from pdfminer.pdfdocument import PDFDocument
        import slate
        with open(self.fileName) as myFile:
            myText = slate.PDF(myFile)
        print myText

