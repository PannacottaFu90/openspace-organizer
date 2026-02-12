class Seat:
    def __init__(self):
        self.free: bool = True
        self.occupant: str = ""

    def set_occupant(self, name: str):
        """
        set an occupant
        param: name of the occupant to be set
        retune: none
        """

        if self.free:
            self.occupant = name
            self.free = False
        else:
            print("Seat is already occupied by {}".format(self.occupant))

    def remove_occupant(self):
        """
        remove occupant from the seat
        param: none
        return: name of the removed occcupant
        """

        if self.free == False:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        else:
            print("Seat is already free")
            return ""

    def __str__(self):
        if self.free:
            return "Seat is free"
        else:
            return "Seat is occupied by {}".format(self.occupant)


class Table:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seats: list[Seat] = [Seat() for i in range(0, self.capacity)]

    def has_free_spot(self):
        """
        check if the spot is free
        param: none
        return: Boolean, trus if free spot
        """

        for seat in self.seats:
            if seat.free:
                return True
                break
        return False

    def assign_seat(self, name: str):
        """
        assign a seat to the occupant
        param: name of the occupant
        return: none
        """

        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break
        else:
            print("No available seat")

    def left_capacity(self):
        """
        return the left capacity of the table
        param: none
        return: int, number of free seats
        """

        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
            else:
                continue
        return count

    def __str__(self):
        return "Table with capacity {} and {} free seats".format(
            self.capacity, self.left_capacity()
        )
