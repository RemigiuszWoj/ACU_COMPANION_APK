#import pytest
import data_csv

def test_read():
    file = data_csv.fileCsv("test_file.csv")
    expected_header ="a;b;c;"
    expected_raws = "1;2;3;"
    assert expected_header == file.header[0]
    assert expected_raws == file.rows[0][0]

# def test_writh():
#     file = data_csv.fileCsv("test_file.csv")
#     expected_raws = [1,2,3]
#     file.write_difrent(expected_raws,"test_file_write.py")
#     file2 =data_csv.fileCsv("test_file_write.py")
#     assert expected_raws == file2.header
    
def test_split_header():
    path = "test_file.csv"
    file = data_csv.preprocesData(path)
    file.split_header()
    assert file.header == ['a', 'b', 'c']

def test_split_raws():
    path = "test_file.csv"
    file = data_csv.preprocesData(path)
    file.split_raws()
    assert file.rows == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def test_transpoze():
    path = "test_file.csv"
    file = data_csv.preprocesData(path)
    file.split_raws()
    file.transpose()
    assert file.rows == [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]

def test_preper_file():
    path = "test_file.csv"
    file = data_csv.preprocesData(path)
    file.split_header()
    file.split_raws()
    file.transpose()
    assert file.header == ['a', 'b', 'c']
    assert file.rows == [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]





