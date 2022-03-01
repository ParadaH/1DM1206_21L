COUNTRY_COLUMN_ID = 1


def read_countries_data(filepath, countries):
    countries_data = dict()
    with open(filepath, "r") as f:
        for line in f:
            maybe_country = line.split(",")[COUNTRY_COLUMN_ID]
            if maybe_country in countries:
                line = line.strip()
                n_of_patients_in_time = get_patients_as_vector(line)
                countries_data[maybe_country] = n_of_patients_in_time

    return countries_data


def get_patients_as_vector(country_data_line):
    n_of_unimportant_column = 4
    n_of_patients_in_time = country_data_line.split(",")[n_of_unimportant_column:]
    n_of_patients_in_time = [int(val) for val in n_of_patients_in_time]

    return n_of_patients_in_time

def make_list_of_countries(filepath):
    list_of_countries = []
    with open(filepath, "r") as f:
        for line in f:
            if line.split(",")[1] not in list_of_countries:
                list_of_countries.append(line.split(",")[1])
    return list_of_countries
