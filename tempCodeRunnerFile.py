class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        t = (id, movie_name, time)
        self.__show_list.append(t)

        # self.seats[id] = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        grid = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(0)
            grid.append(row)

        self.seats[id] = grid
            
    def book_seats(self, id, tup):
        if id in self.seats:
            seat = self.seats[id]
            for row, col in tup:
                
                if row - 1 >= 0 and row <= self.rows and col - 1 >= 0 and col <= self.cols:

                    if seat[row-1][col-1] == 0:
                        seat[row-1][col-1] = 1
                        print("Seat Booked Successfully")
                    else:
                        print("Already Booked")

                else:
                    print("Invalid tup")

        else:
            print("Invalid Id") 
            

    def view_show_list(self):

        for showID, MovieName, showTime in self.__show_list:
            print(f'Show id: {showID}, Show Name: {MovieName}, Show time: {showTime}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid id")
        else:
            seat = self.seats[id]
            for i in range(self.cols):
                Row = []
                for j in range(self.rows):
                    if seat[i][j] == 0:
                        Row.append(seat[i][j])
                print(Row)

Hall_first = Hall(5, 5, 6)

Hall_first.entry_hall(Hall_first)
Hall_first.entry_show(2, 'cinema', "5pm")
Hall_first.entry_show(3, 'Bahibali', "7pm")
Hall_first.entry_show(4, 'chomolkko', "3am")
print(Hall_first.__show_list)