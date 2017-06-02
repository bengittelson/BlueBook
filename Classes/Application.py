class Application:
    def __init__(self, inFile):
        self.fileName = inFile
        self.idNum = None
        self.text = None

    #get text from a pdf
    def getTextFromPDF(self):
        # from pyPdf import PdfFileReader
        # myFile = PdfFileReader(file(self.fileName, "rb"))
        import PyPDF2
        myPDFObj = open(self.fileName, 'rb')
        myReader = PyPDF2.PdfFileReader(myPDFObj)

        #extract text from each page
        for pageNum in range (0, myReader.numPages):
            pageObject = myReader.getPage(pageNum)
            pageText = pageObject.extractText()
            print pageText


        inText = "Ben2"
        self.text = inText