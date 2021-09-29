import data_csv


path = "ACUData.csv"
file = data_csv.fileCsv(path)

ppd = data_csv.preprocesData()

ppd.preper_file(file)
print(file.header)
print(file.rows)





