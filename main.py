import data_csv

if __name__ == "main":
    path = "ACUData.csv"
    file = data_csv.fileCsv(path)
    print(file.header)
    print(file.rows)





