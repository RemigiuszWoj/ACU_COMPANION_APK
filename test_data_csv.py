import data_csv

def test_read():
    file = data_csv.fileCsv("test_file.csv")
    expected_header ="Hello\n"
    expected_raws = "Word\n"
    assert expected_header == file.header
    assert expected_raws == file.rows