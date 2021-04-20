from pathlib import Path
import csv


def retrieve_all_filepaths_from_given_directory(directory, recursively=False):
    if recursively:
        path_ = Path(directory).glob("**/*")
    else:
        path_ = Path(directory).glob("*")
    filepaths = [file_.resolve() for file_ in path_ if file_.is_file()]
    return filepaths


def retrieve_list_of_rows_from_csv_filepath(file_):
    # reading csv file_
    with open(file_, "r", encoding="utf8", newline="") as csvfile:

        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # skip header of csv
        next(csvreader)

        # extracting each data row one by one and append it
        return [line for line in csvreader]


def retrieve_list_of_rows_from_multiple_csv_filepaths(file_path_list):
    # reading csv file_
    full_data_rows_list = []
    for csv_file in file_path_list:
        full_data_rows_list = (
            full_data_rows_list + retrieve_list_of_rows_from_csv_filepath(csv_file)
        )
    return full_data_rows_list

