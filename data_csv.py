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
                    
    def write_difrent(self, data:list, path:str, position="end") -> None:
        with open(path, "") as file:
            if position == "end":
                for row in data:
                    for x in row:
                        file.write(str(x)+"; ")
                    file.write("\n")
    

class preprocesData():
    
    def split_header(self, file:fileCsv) -> None:
        header = file.header[0].split(";")
        header.pop()
        file.header = header

    def split_raws(self, file:fileCsv) -> None:
        split_rows = []
        rows = file.rows
        for row in rows:
            tmp = row[0].split(";")
            tmp.pop()
            split_rows.append(tmp)
        file.rows = split_rows

    def transpose(self, file:fileCsv) -> None:
        file.rows = [list(i) for i in zip(*file.rows)]

    def preper_file(self, file:fileCsv) -> None:
        self.split_header(file)
        self.split_raws(file)
        self.transpose(file)
