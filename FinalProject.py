from os import system


class Search:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Search(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Search(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.findval(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.findval(value)
        else:
            return str(value) + " is found "

def sort(c):

    for i in range(len(c)):

        min_idx = i
        for j in range(i + 1, len(c)):

            if c[min_idx] > c[j]:

                min_idx = j

        c[i], c[min_idx] = c[min_idx], c[i]

    for i in range(len(c)):
        print("%d" % c[i], end = " ")

def menu():
    print("""
        
              Welcome to 
        Search and Sort Program
        _______________________
        
        1. Sort Numbers
        2. Search for Numbers and Text
        3. Exit
    
    """)

    return input("Enter your Choice here: ")


while True:
    choice = menu()
    if choice == "1":

        print("""
            
             Welcome to 
            Sort Program
            
            1. One by one
            2. Bulk
            3. Exit
        
        """)
        sort_choice = input("Enter your Choice: ")
        if sort_choice == "1":
            x_list = list()
            while True:

                x = input("Enter your Number or Pass ")
                if x.lower() == "pass":
                    break
                else:
                    try:
                        x_list.append(int(x))
                    except ValueError:
                        print("That's not integer \n")
            print("\n Sorted Nums: ")
            sort(x_list)
        elif sort_choice == "2":
            y = input("Enter number seperated by space \n")
            y_list = list()
            try:
                y_line = y.split(None)
                for i in range(len(y_line)):
                    y_list.append(int(y_line[i]))
            except ValueError:
                print("That's not integer \n")
            print("\nSorted Nums: ")
            sort(y_list)

        elif sort_choice == "3":
            break

        else:
            continue

    elif choice == "2":
        print("""
        
                  Welcome to 
            Number and Text Search
            
            1. Search in Text
            2. Search in List of Numbers
            3. Exit
        
        """)

        search_choice = input(" Txt or Num: ")
        while True:
            node = Search("")
            if search_choice == "1" or search_choice.lower() == "txt" :

                _txt = input(" Enter your text \n")
                _txt_idx = _txt.split(None)

                for i in range(len(_txt_idx)):
                    node.insert(_txt_idx[i])

                _find_ = input("Search For? ")
                print("")
                print(node.findval(_find_))
                break


            elif search_choice == "2":

                z = input("Enter number seperated by space \n")
                try:
                    z_line = z.split(None)
                    node = Search(z[0])
                    for i in range(len(z_line)):
                        node.insert(z_line[i])

                except ValueError:
                    print("That's not integer \n")

                _find_ = input("Search For? ")
                print("")
                print(node.findval(_find_))
                break

            elif search_choice == "3":
                break

            else:
                continue

    elif choice == "3":

        break

    else:
        continue




