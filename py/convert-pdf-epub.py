import os
#to read filename from clipboard
import pyperclip
#pip install pymupdf
import pymupdf
#If pandoc.exe not available and/or don't need it, use pypandoc-binary instead
#pip install pypandoc
import pypandoc

#======== grab input filename from clipboard
item = pyperclip.paste()
#expects author#title.pdf
if not item or ".pdf" not in item or "#" not in item:
	print ("Expects authors#title.pdf in clipboard")
	exit()
else:
	print(f"Handling {item}")

#======== grab author(s) and title
INPUTFILE = item
x = [x.strip() for x in item.split('#')]
AUTHOR = x[0]
#ignore file extension
TITLE, _ = os.path.splitext(x[1])
TEMPFILE = f"{AUTHOR}#{TITLE}.xhtml"
EXTENSION = ".epub"
OUTPUTFILE = f"{AUTHOR}#{TITLE}{EXTENSION}"

#======== Open  PDF file
pdf_document = pymupdf.open(INPUTFILE)
#======== Iterate through pages
html_content = ""
for page_num in range(len(pdf_document)):
	page = pdf_document.load_page(page_num)
	#https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text
	html_content += page.get_text("xhtml",flags=pymupdf.TEXTFLAGS_XHTML)

#======== turn XHTML into EPUB, including metadata
#if CLI pandoc already on disk
os.environ.setdefault('PYPANDOC_PANDOC', r'c:\pandoc.exe')
extra_args=['--epub-title-page=false','--metadata',f'author={AUTHOR}','--metadata',f'title={TITLE}']
output = pypandoc.convert_text(html_content, format='html',to='epub',outputfile=OUTPUTFILE, extra_args=extra_args)
#remove XHTML file
os.remove(TEMPFILE)