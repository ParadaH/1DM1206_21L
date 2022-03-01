import numpy as np
from math import pi, sin, cos
from matplotlib import pyplot as plt
import sys

COUNTRY_COLUMN_ID = 1

def validate_args(args):
    if len(args) < 2:
        print("Incorrect arguments. Expected filename and list of countries", file=sys.stderr)
        exit(-1)

def read_countries_data(filepath, countries):
    countries_data = dict()

    with open(filepath, "r") as f:
        for line in f:
            maybe_country = line.split(",")[COUNTRY_COLUMN_ID]

            if maybe_country in countries:
                line = line.strip()
                n_of_patients_in_time = get_patients_as_vector(line)

                countries_data[maybe_country] = n_of_patients_in_time

    return countries_data #zwraca slownik z panstwami

def get_patients_as_vector(country_data_line):
    n_of_unimportant_column = 4
    n_of_patients_in_time = country_data_line.split(",")[n_of_unimportant_column:]
    n_of_patients_in_time = [int(val) for val in n_of_patients_in_time]

    return n_of_patients_in_time

def display_data(n_of_patients_in_countries):
    for country, data in n_of_patients_in_countries.items():
        plt.semilogy(data, label=country) #na OY skala logarytmiczna

    plot_info()

def display_selected_data(filepath, countries):

    number_of_countries = len(countries)
    k = 6

    for i in range(2):
        for j in range(2):
            if(k < number_of_countries + 6):
                h = k - 6
                countries_data = read_countries_data(filepath, countries[h:k])
                plt.subplot2grid((2,2),(i,j))
                display_data(countries_data)
                k += 6
            else:
                break
    plt.show()

def plot_info():
    plt.xlabel("Days (subsequent data)")
    plt.ylabel("Total number of patients")
    plt.title("Covid-19 number of patients since 01.01.2020")
    plt.grid()
    plt.legend()

if __name__ == "__main__":
    args = sys.argv
    validate_args(args)

    filepath = args[1]
    country_names = args[2].split(",")

    if (len(args) > 3):
        if (args[3] == "abc"):
            sorted_country_names = sorted(country_names)
            display_selected_data(filepath, sorted_country_names)
        else:
            display_selected_data(filepath, country_names)
    else:
        display_selected_data(filepath, country_names)
