from typing import Iterator, Tuple
from gmft.detectors.base import BaseDetector, CroppedTable
from gmft.pdf_bindings.base import BasePDFDocument, BasePage

def detect_tables(detector: BaseDetector, page: BasePage) -> Iterator[CroppedTable]:
    for table in detector.detect(page):
        yield table

def ingest_pdf(detector: BaseDetector, doc: BasePDFDocument) -> Iterator[Tuple[int, Iterator[CroppedTable]]]:
    for page in doc:
        yield page.page_number, detect_tables(detector, page)