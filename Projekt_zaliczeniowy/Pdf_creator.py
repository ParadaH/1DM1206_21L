from datetime import date
from io import BytesIO

from PyQt5.QtWidgets import QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from matplotlib.figure import Figure
from Data_interpreter import read_countries_data
from Exceptions import Error
FILENAME = None
LIST_OF_COUNTRIES = None
OY_NAME = None


class PdfSaveButton(QPushButton):

    def __init__(self, parent, name, filename, oy_name):
        super().__init__(name)
        self.__parent = parent
        self.__pdf_generator = PdfReportGenerator(self.__parent)

        global FILENAME, OY_NAME
        FILENAME = filename
        OY_NAME = oy_name

        self.clicked.connect(self.__save_btn_action)

    def __save_btn_action(self):
        if len(self.__parent.list_of_countries.list_of_countries) != 0:
            global LIST_OF_COUNTRIES
            LIST_OF_COUNTRIES = self.__parent.list_of_countries.list_of_countries

            self.__chart = Figurine(self.__parent)
            img_data = self.__chart.get_img()
            img = ImageReader(img_data)
            filename = self.__prepare_file_chooser()
            self.__pdf_generator.create_and_save_report(img, filename)
        else:
            Error("UnableToCreatePdfFile")

    def __prepare_file_chooser(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF report", filter="*.pdf")
        return filename



class PdfReportGenerator:

    def __init__(self, parent):
        self.__parent = parent
        self.__title = f"report ({date.today()})"

    def create_and_save_report(self, img, filepath, pagesize=A4):
        pdf_template = self.__create_pdf_template(filepath, img, pagesize)
        pdf_template.save()

    def __create_pdf_template(self, filepath, img, pagesize):
        canvas = Canvas(filepath, pagesize=pagesize)
        canvas.setFont("Times-Roman", 40)
        text = f"COVID-19 {self.__parent.oy_name}"
        title = text
        title_magic_offset, img_magic_offset = 100, 600
        title_x, title_y = A4[0] / 2, A4[1] - title_magic_offset
        img_x, img_y = 0, A4[1] - img_magic_offset

        canvas.drawCentredString(title_x, title_y, title)
        canvas.drawImage(img, img_x, img_y)

        return canvas


class Figurine(FigureCanvasQTAgg):
    __IMG_FORMAT = "png"

    def __init__(self, parent, figsize=(4, 4), dpi=100):
        self.__parent = parent
        self.__fig = Figure(figsize=figsize, dpi=dpi)
        super().__init__(self.__fig)
        self.__init_fig()

    def get_img(self):
        img_data = BytesIO()

        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)

        seek_offset = 0
        img_data.seek(seek_offset)

        return img_data

    def __init_fig(self):
        plot_config_id = 111
        self.__fig.add_subplot(plot_config_id)
        self.__fig.suptitle("COVID-19 specific cases graph")
        self.__plot_chart()
        self.__fig.tight_layout()

    def __plot_chart(self):
        ax = self.__fig.axes[0]

        n_of_patients_in_countries = read_countries_data(FILENAME, LIST_OF_COUNTRIES)
        for country, data in n_of_patients_in_countries.items():
            ax.semilogy(data, label=country)

        ax.set_xlabel("Days")
        ax.set_ylabel(self.__parent.oy_name)
        ax.set_xlim([self.__parent.min_value, self.__parent.max_value])
        ax.grid()
        ax.legend()
