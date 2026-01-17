# PDF-MERGER
this Python code will access your pdf files and merger them as a single file.
 Line by Line explanation of the code.
 #this access your system files ie the path to your doc files
def combine_pdf(list_of_files):
    merger = PyPDF2.PdfMerger() # this merger is a class in the module that helps you to combine diff. docs.
    for file in list_of_files: #this line will loop the doc found in your sys file
        merger.append(file) #this will add the looped file to the merger
    with open("output.pdf", "wb") as output: # this will save and open the new file that have been merged together and 'wb' will help to open it so that you can read it and understand it.
        merger.write(output) #this will help to open the merged doc
combine_pdf(inputFile) # you call the function and put the sys file


#open the folder where the documents ara with your terminal and run with this "  python3 Pdfmerger.py CV.pdf LETTER.pdf new.pdf"  (The doc arrangement is how it will appear)
