from pypdf import PdfMerger

merger = PdfMerger()
pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]

pdfs = ["UNIT 1- Introduction to Cybercrime.pdf", "UNIT 2- Cybercrime and Cybersecurity.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()   