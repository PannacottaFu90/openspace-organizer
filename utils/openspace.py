import random
from utils.table import Table


class Openspace:
    def __init__(self):
        self.number_of_tables: int = 6
        self.tables: list[Table] = [Table(4) for i in range(0, self.number_of_tables)]

    def organize(self, names: list):
        """
        organize the names into tables
        param: list of names
        return: none
        """
        self.left_over = []
        random.shuffle(names)

        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
            else:
                self.left_over.append(name)

    def display(self):
        """
        display the tables and their occupants
        param: none
        return: none
        """
        count = 0
        for table in self.tables:
            count = count + 1
            print("Table {}:".format(count))
            for seat in table.seats:
                print(seat)

        else:
            print(
                "All tables are displayed, {} people have not a seat. Here's the list of names: {}".format(
                    len(self.left_over), self.left_over
                )
            )

    def export_excel(self):
        """
        export the tables and their occupants to an excel file
        param: none
        return: none
        """
        import pandas as pd

        data = {}
        table_list = []
        count = 0
        for table in self.tables:
            count = count + 1
            for seat in table.seats:
                data = {
                    "Table_name": "Table {}".format(count),
                    "Occupant": seat.occupant,
                }
                table_list.append(data)
        if len(self.left_over) > 0:
            for name in self.left_over:
                data = {"Table_name": "No seat", "Occupant": name}
                table_list.append(data)
        df = pd.DataFrame(table_list)
        df.to_excel("Today_s_positions.xlsx", index=False)
