from contextlib import contextmanager
from typing import Iterator
from io import BytesIO
import tempfile

from gmft.pdf_bindings.base import BasePDFDocument
from gmft.pdf_bindings.pdfium import PyPDFium2Document

@contextmanager
def create_temp_pdf(buffer: BytesIO) -> Iterator[BasePDFDocument]:
    with tempfile.NamedTemporaryFile() as f:
        f.write(buffer.getbuffer())
        f.flush()

        doc = PyPDFium2Document(f.name)

        try:
            yield doc
        finally:
            doc.close()