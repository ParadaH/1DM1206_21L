import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QApplication, QDesktopWidget, QPushButton, \
    QHBoxLayout, QGroupBox, QFormLayout, QLabel, QScrollArea, QGridLayout, QFileDialog, QSlider
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from Pdf_creator import PdfSaveButton
from Data_interpreter import read_countries_data, make_list_of_countries
from Exceptions import Error

COUNTRY_COLUMN_ID = 1
FILENAME = None


class App(QMainWindow):

    def __init__(self, width, height, accepted_formats):
        super().__init__()
        self.__accepted_formats = accepted_formats

        self.setWindowTitle("COVID-19 Analysis app")
        self.__set_window_in_center(width, height)

        # Creating tabs
        self.__tabs_widget = TabsWidget(self, width, height)
        self.setCentralWidget(self.__tabs_widget)

        self.show()

    def __set_window_in_center(self, width, height):
        self.setGeometry(0, 0, width, height)
        screen_id = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QDesktopWidget().availableGeometry(screen_id).center()
        top_left = QPoint(center_point.x() - width / 2, center_point.y() - height / 2)
        self.move(top_left)


class TabsWidget(QWidget):
  
    def __init__(self, parent, width, height):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        self.__tabs = QTabWidget()
        self.__tabs.resize(width, height)

        self.__tab1 = Tab("Confirmed cases")
        self.__tab2 = Tab("Recovered")
        self.__tab3 = Tab("Deaths")

        self.__tabs.addTab(self.__tab1, "Confirmed cases")
        self.__tabs.addTab(self.__tab2, "Recovered")
        self.__tabs.addTab(self.__tab3, "Deaths")

        self.__tab1.setLayout(QVBoxLayout(self))
        self.__tab2.setLayout(QVBoxLayout(self))
        self.__tab3.setLayout(QVBoxLayout(self))

        layout.addWidget(self.__tabs)
        self.setLayout(layout)


class Tab(QWidget):

    def __init__(self, oyname):
        super().__init__()
        self.oy_name = oyname
        self.min_value = None
        self.max_value = None
        self.__window_view()
        self.list_of_countries = ListOfCountries()

    def __create_pdf_btn(self):
        btn_pdf = PdfSaveButton(self, "PDF", FILENAME, self.oy_name)
        return btn_pdf

    def __create_in_btn(self):
        btn_in = QPushButton("IN")
        btn_in.clicked.connect(self.__handle_in_dir)
        return btn_in

    def __create_sliders(self):
        sliders = Sliders(self)
        return sliders

    def __handle_in_dir(self):
        try:
            dir_path = QFileDialog.getOpenFileName(self, "test", "*.csv")
            filename = dir_path[0]
            global FILENAME
            FILENAME = filename
            self.__country_list = CountryTable(self, make_list_of_countries(filename))
            self.group_box.addWidget(self.__country_list, 1, 2, 1, 1)
            self.group_box.addWidget(self.__create_pdf_btn(), 4, 1, 1, 1)
            self.group_box.addWidget(self.__create_sliders(), 4, 2, 1, 1)
            self.setLayout(self.group_box)
        except:
            Error("UnableToReadTheFile")

    def __window_view(self):
        self.group_box = QGridLayout()
        self.group_box.addWidget(self.__create_in_btn(), 4, 2, 1, 1)
        self.setLayout(self.group_box)


class CountryTable(QScrollArea):

    def __init__(self, parent, countries):
        super().__init__()
        self.__parent = parent
        self.__scroll_tab_view(countries)
        self.__oy_name = self.__parent.oy_name
        self.__btn_of_countries = []
        self.__list_of_countries = []

    # Creating box with countries
    def __scroll_tab_view(self, countries):
        btn_layout = QFormLayout()
        btn_group = QGroupBox()
        self.__btn_of_countries = countries

        for i in range(len(self.__btn_of_countries) - 1):
            country_name = self.__btn_of_countries[i + 1]
            btn = QPushButton(country_name)
            btn.clicked.connect(self.__get_country_name(country_name))
            btn_layout.addRow(btn)

        btn_group.setLayout(btn_layout)
        self.setWidget(btn_group)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)

    def __get_country_name(self, country_name):
        return lambda _: self.__country_names(country_name)

    def __country_names(self, country_name):
        if country_name not in self.__list_of_countries:
            if len(self.__parent.list_of_countries.list_of_countries) < 6:
                self.__list_of_countries.append(country_name)

                plot = PlotDeveloper(self.__parent, self.__list_of_countries, self.__oy_name)
                self.__parent.group_box.addWidget(plot, 1, 1, 2, 1)
                self.__parent.setLayout(self.__parent.group_box)
                self.__parent.list_of_countries.list_of_countries = self.__list_of_countries

                self.__parent.show()
            else:
                Error("UnableToShowMoreCountries")


        elif country_name in self.__list_of_countries:
            self.__list_of_countries.remove(country_name)

            plot = PlotDeveloper(self.__parent, self.__list_of_countries, self.__oy_name)
            self.__parent.group_box.addWidget(plot, 1, 1, 2, 1)
            self.__parent.setLayout(self.__parent.group_box)
            self.__parent.list_of_countries.list_of_countries = self.__list_of_countries

            self.__parent.show()


class PlotDeveloper(FigureCanvasQTAgg):

    def __init__(self, parent, country_data, oy_name):
        self.__parent = parent
        self.__list_of_countries = country_data
        self.__oy_name = oy_name
        fig, self.ax = plt.subplots(figsize=(4, 4), dpi=100)
        super().__init__(fig)
        self.draw_plot()

    def draw_plot(self):
        n_of_patients_in_countries = read_countries_data(FILENAME, self.__list_of_countries)
        for country, data in n_of_patients_in_countries.items():
            plt.semilogy(data, label=country)

        self.ax.set_xlabel("Days")
        self.ax.set_ylabel(self.__oy_name)
        self.ax.set_xlim([self.__parent.min_value, self.__parent.max_value])
        self.ax.grid()
        self.ax.legend()


class Sliders(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.__parent = parent
        self.__prepare_sliders_panel()

    def __init_view(self):
        self.__layout = QGridLayout()
        self.__parent.setLayout(self.__layout)
        self.show()

    def __prepare_sliders_panel(self):
        slider_min_width = 250
        min_value, max_value = 0, 400

        sliders = DoubleSlider(self.__parent, min_value, max_value, slider_min_width)
        self.__parent.group_box.addWidget(sliders, 4, 2, 1, 1)


class DoubleSlider(QWidget):

    def __init__(self, parent, min_value, max_value, min_width):
        super().__init__()
        self.__parent = parent
        self.__min_value = min_value
        self.__max_value = max_value
        self.__min_width = min_width

        self.__low_slider = self.__prepare_low_slider()
        self.__high_slider = self.__prepare_high_slider()

        self.__prepare_layout()

    def __prepare_low_slider(self):
        slider = self.__prepare_slider(self.__min_value)
        slider.valueChanged.connect(self.__on_change_low)
        return slider

    def __prepare_high_slider(self):
        slider = self.__prepare_slider(self.__max_value)
        slider.valueChanged.connect(self.__on_change_high)
        return slider

    def __prepare_slider(self, init_value):
        slider = QSlider(QtCore.Qt.Horizontal)
        slider.setMinimumWidth(self.__min_width)
        slider.setMinimum(self.__min_value)
        slider.setMaximum(self.__max_value)
        slider.setValue(init_value)
        return slider

    def __on_change_low(self):

        MIN_VALUE = self.__low_slider.value()
        self.__parent.min_value = MIN_VALUE
        new_low_value = self.__low_slider.value()
        high_value = self.__high_slider.value()

        if new_low_value >= high_value:
            self.__high_slider.setValue(new_low_value)

        plot = PlotDeveloper(self.__parent, self.__parent.list_of_countries.list_of_countries, self.__parent.oy_name)
        self.__parent.group_box.addWidget(plot, 1, 1, 2, 1)
        self.__parent.setLayout(self.__parent.group_box)

        self.__parent.show()

    def __on_change_high(self):

        MAX_VALUE = self.__high_slider.value()
        self.__parent.max_value = MAX_VALUE
        new_high_value = self.__high_slider.value()
        low_value = self.__low_slider.value()

        if new_high_value <= low_value:
            self.__low_slider.setValue(new_high_value)

        plot = PlotDeveloper(self.__parent, self.__parent.list_of_countries.list_of_countries, self.__parent.oy_name)
        self.__parent.group_box.addWidget(plot, 1, 1, 2, 1)
        self.__parent.setLayout(self.__parent.group_box)

        self.__parent.show()

    def __prepare_layout(self):
        self.__parent.group_box.addWidget(self.__low_slider, 2, 2)
        self.__parent.group_box.addWidget(self.__high_slider, 3, 2)


class ListOfCountries:

    def __init__(self):
        self.list_of_countries = []


if __name__ == '__main__':
    app = QApplication([])

    width, height = 800, 600
    accepted_formats = (".csv")

    tabs_app = App(width, height, accepted_formats)

    sys.exit(app.exec_())
