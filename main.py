import csv

class fileCsv():
    "csv file modifi class"
    def __init__(self, path):
        self.path = path

    def read(self):
        self.rows = []
        self.header =[]
        with open(self.path, "r") as file:
            csvreader = csv.reader(file)
            self.header = next(csvreader) 
            for row in csvreader:
                self.rows.append(row)

    def write(self, data, position="end"):
        with open(self.path, "w") as file:
            if position == "end":
                for row in data:
                    for x in row:
                        file.write(str(x),+" ")
                    file.write("n")








path = "ACUData.csv"
file = fileCsv(path)
file.read()
print(file.header)
print(file.rows)


# data = [1,2,3,4]
# file.write(data)
# print(file.header)
# print(file.rows)



# rows = []
# patch = "ACUData.csv"
# with open(patch, "r") as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)
