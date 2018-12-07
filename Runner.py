import random

class Runner:

    # global stacks
    non_visited = []
    visited = []

    def file_reader(self, file, file_2):

        fname = []
        fname_2 = []

        with open(file) as restaurant_list:
            for line in restaurant_list:
                fname = line.rstrip().split(',')

        self.stacker(fname, self.non_visited)

        with open(file_2) as visited:
            for line in visited:
                fname_2 = line.rstrip().split(',')

        self.stacker(fname_2, self.visited)

    def get_non_visited(self):
        print(self.non_visited)

    def get_visited(self):
        print(self.visited)

    def stacker(self, x, list):

        # puts content from file into stack
        for i in x:
            list.append(i)

    def shuffler(self):
        # shuffles restaurants that haven't been visited

        random.shuffle(self.non_visited)

    def refill_list(self, visited):

        count = 0
        fname = []

        with open("List.txt", "w") as file:
            for i in visited:
                if count == len(visited) - 1:
                    file.write(i)
                else:
                    file.write(i + ",")
                count += 1

        with open("visited.txt", "w") as file:
            file.write("tonteria ")

        self.visited = []

        with open("List.txt") as restaurant_list:
            for line in restaurant_list:
                fname = line.rstrip().split(',')


        self.stacker(fname, self.non_visited)


    def get_place(self):
        if not self.non_visited:
            self.refill_list(self.visited)

        self.shuffler()
        tmp = self.non_visited.pop()
        self.list_writer("List.txt", self.non_visited)
        self.visited.append(tmp)
        self.list_writer("visited.txt", self.visited)

        if tmp == "nishi ramen":
            return "F"
        return tmp

    def list_writer(self, filename, place):

        count = 0

        with open(filename, "w") as file:
            for i in place:
                if count == len(place)-1:
                    file.write(i)
                else:
                    file.write(i + ",")
                count += 1


    def places(self):

        return 0

    # def visited_list(self:
    #
    #     return 0


r = Runner()
x = r.file_reader("List.txt", "visited.txt")
# r.get_non_visited()
# r.get_visited()
print("You're going to: " + r.get_place())
print("\n")
print("Remainding places: ")
r.get_non_visited()
print("\n")
print("You've been to: ")
r.get_visited()