# import pytesseract
# from PIL import Image
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# img = Image.open('Capture.png')
# text = pytesseract.image_to_string(img)
# print(text)

#
# import pytesseract
# from PIL import Image
#
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# img = Image.open('Test_Result_Reports/Capture.png')
# text = pytesseract.image_to_string(img)
# print(text)
# # text_list = text.split()
# #
# # for i in range (len(text_list)):
# #     print(text_list[i])



# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('Test_Result_Reports/cbc-sample.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
# print(pageObj.extractText())

# closing the pdf file object


text = pageObj.extractText()
text_list = text.split()
# for item in text_list:
#     print(item)

print(text_list.index('RBC(Total Count)'))












pdfFileObj.close()
