import data_csv


path = "ACUData.csv"


file = data_csv.preprocesData(path)

file.preper_file()
print(file.header)
print(file.rows)





