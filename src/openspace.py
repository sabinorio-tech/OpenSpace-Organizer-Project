import csv
import random

from src.table import Table

class OpenSpace:
    def __init__(self):
        self.number_of_tables = 6 
        self.tables = [Table() for _ in range(self.number_of_tables)] 
        """ [Table(), Table(), Table(), Table(), Table(), Table()] """

    def organize(self, names): 
        for table in self.tables:
            while table.has_free_spot() and names: 
                name = random.choice(names)
                table.assign_seat(name)
                names.remove(name) # Remove the name from the list when seated

    def display(self): 
        count = 1

        for table in self.tables: 
            print(f"Table {str(count)}: ")
            for seat in table.seats: 
                print(f"{seat.occupant}")
            count += 1

    def store(self, output_filename): 
        with open(output_filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            table_no = 1

            for table in self.tables:
                seated_names = ["Table " + str(table_no)]
                for seat in table.seats: 
                    seated_names.append(seat.occupant)
                writer.writerow(seated_names)
                table_no += 1