from contextlib import contextmanager
from typing import Iterator
from io import BytesIO
import tempfile

from gmft.pdf_bindings.base import BasePDFDocument
from gmft_pymupdf import PyMuPDFDocument

@contextmanager
def create_temp_pdf(buffer: BytesIO) -> Iterator[BasePDFDocument]:
    with tempfile.NamedTemporaryFile() as f:
        f.write(buffer.getbuffer())
        f.flush()

        doc = PyMuPDFDocument(f.name)

        try:
            yield doc
        finally:
            doc.close()