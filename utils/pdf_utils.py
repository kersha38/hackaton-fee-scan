import pdfquery
from pdfquery import PDFQuery
from pyquery import PyQuery

from constants.constants import CELL_WIDTH, CELL_HEIGHT


class PDFReader:
    pdf: PDFQuery

    def __init__(self, path):
        self.pdf = pdfquery.PDFQuery(path)
        self.pdf.load()

    def get_columns(self, title):
        positions = self.__get_label_columns_positions(title)
        # result: PDFQuery = self.pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % positions) # alternative

        result: PDFQuery = self.pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % positions)

        return result

    def __get_label_columns_positions(self, title: str):
        label: PyQuery = self.pdf.pq(f'LTTextLineHorizontal:contains("{title}")')
        label_len = len(title)
        left_label = float(label.attr('x0'))
        bottom_label = float(label.attr('y0'))
        left_corner = left_label - (CELL_WIDTH - label_len) / 3
        right_corner = left_corner + CELL_WIDTH
        bottom_corner = bottom_label - 4 * CELL_HEIGHT
        upper_corner = bottom_label - CELL_HEIGHT
        return left_corner, bottom_corner, right_corner, upper_corner
