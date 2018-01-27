import os


class Config:
    MAIN_WINDOW_WIDTH = 800
    MAIN_WINDOW_HEIGHT = 600
    DIR_HOME = os.path.expanduser("~")
    DIR_APP_ROOT = os.path.dirname(os.path.realpath(__file__))

    DIR_INPUT_DEFAULT = os.path.join(DIR_APP_ROOT, "in")
    PATH_SOURCEDATA = None
    RAW_DATA = []

    DIR_OUTPUT_DEFAULT = os.path.join(DIR_APP_ROOT, "out")
    DIR_OUTPUT = DIR_OUTPUT_DEFAULT
    DEFAULT_LATEX_FILENAME = "output.tex"
    LATEX_TARGET_FILE = os.path.join( DIR_OUTPUT, DEFAULT_LATEX_FILENAME)
    DEFAULT_PDF_FILENAME = "output.pdf"
    PDF_TARGET_FILE = os.path.join(DIR_OUTPUT, DEFAULT_PDF_FILENAME)

    DEFAULT_PAGE_WIDTH_MM = 297
    DEFAULT_PAGE_HEIGHT_MM = 210
    PAGE_WIDTH_MM = DEFAULT_PAGE_WIDTH_MM
    PAGE_HEIGHT_MM = DEFAULT_PAGE_HEIGHT_MM

    DEFAULT_CARD_WIDTH_MM = 70
    DEFAULT_CARD_HEIGHT_MM = 50
    CARD_WIDTH_MM = DEFAULT_CARD_WIDTH_MM
    CARD_HEIGHT_MM = DEFAULT_CARD_HEIGHT_MM

    # The following fields have to be calculated by the program:
    CARDS_PER_PAGE = 0
    CARD_ROWS_PER_PAGE = 0
    CARD_COLUMNS_PER_PAGE = 0

    def __init__(self):
        pass
