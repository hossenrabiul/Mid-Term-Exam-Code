class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        t = (id, movie_name, time)
        self.__show_list.append(t)

        grid = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append("Empty")
            grid.append(row)

        self._seats[id] = grid
            
    def book_seats(self, id, tup):
        if id in self._seats:
            seat = self._seats[id]
            for row, col in tup:
                
                if row - 1 >= 0 and row <= self.rows and col - 1 >= 0 and col <= self.cols:

                    if seat[row-1][col-1] == "Empty":
                        seat[row-1][col-1] = "BooKed"
                        print("\nSeat Booked Successfully\n")
                    else:
                        print("\nAlready Booked\n")

                else:
                    print("\nInvalid tup\n")

        else:
            print("\nInvalid Id\n") 
            

    def view_show_list(self):
        if not self.__show_list:
            print("\nNo shows available ! \n")
            return
        for showID, MovieName, showTime in self.__show_list:
            print(f'\nShow id: {showID}, Show Name: {MovieName}, Show time: {showTime}\n')

    def view_available_seats(self, id):
        if id not in self._seats:
            print("\nInvalid id\n")
        else:
            seat = self._seats[id]
            for i in range(self.cols):
                Row = []
                for j in range(self.rows):
                    if seat[i][j] == "Empty":
                        Row.append(seat[i][j])
                print(' '.join(map(str, Row)))

Hall_first = Hall(5, 5, 6)                                                                                                                                                                    
Hall_first.entry_show(1, "Bahubali", "5pm")

while True:
    print("Option : ")

    print("\t1. Book Seats : ")
    print("\t2. view_show_list : ")
    print("\t3. view_available_seats")
    print("\t4. Exit-")

    ch = int(input("\n\tEnter Option : "))
    
    if ch == 1:
       Id = int(input("Enter The Id : "))
       Col = int(input("Enter The Col : "))
       Row = int(input("Enter The Row : "))

       Hall_first.book_seats(Id, [(Col, Row)])

    elif ch == 2:

        Hall_first.view_show_list()

    elif ch == 3:
        Id = int(input("Enter The Id : "))
        Hall_first.view_available_seats(Id)

    else:
        print("Exit -!")
        break



    



