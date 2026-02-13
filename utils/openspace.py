import random
import matplotlib.pyplot as plt
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

    def visualization(self):
        """
        visualize the tables and their occupants using matplotlib
        param: none
        return: none
        """

        table_per_row = 3
        row_per_table = 2
        fig, ax = plt.subplots(figsize=(30, 8))
        count = 0
        tcount = 0
        for table in self.tables:
            count = count + 1
            row = (count - 1) // table_per_row
            line = (count) % table_per_row
            x_base = line * 10
            y_base = row * -10
            tcount = 0
            for seat in table.seats:
                tcount = tcount + 1
                trow = (tcount - 1) // row_per_table
                tline = (tcount) % row_per_table
                x_final = x_base + tline * 2
                y_final = y_base - trow * 2
                if seat.free:
                    color = "green"
                else:
                    color = "red"
                circle = plt.Circle((x_final + 0.7, y_final), 0.9, color=color)

                ax.add_patch(circle)
                name = seat.occupant
                plt.text(x_final, y_final, name, va="center", fontsize=9)

            plt.text(
                x_base + 1.6,
                y_base + 1,
                "Tavolo {}".format(count),
                ha="center",
                fontweight="bold",
            )

        plt.axis("equal")
        plt.axis("off")
        plt.title("Openspace - Seating Arrangement", fontsize=16, fontweight="bold")
        plt.show()
