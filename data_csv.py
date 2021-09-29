import csv

class fileCsv():
    "csv file modifi class"
    def __init__(self, path:str) -> None:
        self.path = path
        self.read()

    def read(self) -> None:
        self.rows = []
        self.header =[]
        with open(self.path, "r") as file:
            csvreader = csv.reader(file)
            self.header = next(csvreader) 
            for row in csvreader:
                self.rows.append(row)

    def modifi(self, data:list, position="end") -> None:
        with open(self.path, "a") as file:
            if position == "end":
                for row in data:
                    for x in row:
                        file.write(str(x)+"; ")
                    file.write("\n")

    def write(self, data:list, position="end") -> None:
        with open(self.path, "") as file:
            if position == "end":
                for row in data:
                    for x in row:
                        file.write(str(x)+"; ")
                    file.write("\n")



#class preProcesData():
