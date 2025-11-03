# data_holder.py

class DataHolder:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def show_data(self):
        print("Data 1:", self.data1)
        print("Data 2:", self.data2)

north_south = [2, 3, 3, 9, 7, 7, 7, 7, 9]
east_west = [3, 4, 5, 7, 8, 9, 9, 10, 11]

data_object = DataHolder(north_south, east_west)