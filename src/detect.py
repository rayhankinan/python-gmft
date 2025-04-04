from typing import Iterator, Tuple
from gmft.detectors.base import BaseDetector, CroppedTable, ConfigT
from gmft.pdf_bindings.base import BasePDFDocument, BasePage

def detect_tables(detector: BaseDetector, page: BasePage) -> Iterator[CroppedTable]:
    for table in detector.detect(page):
        yield table

def ingest_pdf(detector: BaseDetector[ConfigT], doc: BasePDFDocument) -> Iterator[Tuple[BasePage, Iterator[CroppedTable]]]:
    for page in doc:
        yield page, detect_tables(detector, page)