

from src.openspace import OpenSpace
from src import utils

input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

names = utils.read_names_from_csv(input_filepath)

open_space = OpenSpace()
open_space.organize(names)
open_space.store(output_filename)
open_space.display()