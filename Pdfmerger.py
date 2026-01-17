import sys, PyPDF2

inputFile = sys.argv[1:]
def combine_pdf(list_of_files):
    merger = PyPDF2.PdfMerger()
    for file in list_of_files:
        merger.append(file)
    with open("output.pdf", "wb") as output:
        merger.write(output)
combine_pdf(inputFile)
