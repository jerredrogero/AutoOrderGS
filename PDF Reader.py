import PyPDF2
#PDF Text Reader

object = open(r'C:\Users\Alienware Aurora R6\Downloads\Invoice_81.pdf','rb')

reader = PyPDF2.PdfFileReader(object)
pageobject = reader.getPage(0)
print(pageobject.extractText())
