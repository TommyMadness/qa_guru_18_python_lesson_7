import os.path

from pypdf import PdfReader

reader = PdfReader("/tmp/sample.pdf")

print(reader.pages)
print(len(reader.pages))
print(reader.pages[0].extract_text())

# assert "Phasellus congue" in reader.pages[0]
print(os.path.getsize("/tmp/sample.pdf"))
assert os.path.getsize("/tmp/sample.pdf") == 18810