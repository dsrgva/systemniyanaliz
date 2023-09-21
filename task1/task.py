import csv
import sys

def get_cell_value(file_path, row_number, column_number):
    try:
        with open(file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)
            
            if row_number <= 0 or row_number > len(data):
                print("Номер строки выходит за пределы файла.")
                return
            
            row = data[row_number - 1]
            
            if column_number <= 0 or column_number > len(row):
                print("Номер колонки выходит за пределы строки.")
                return
            
            cell_value = row[column_number - 1]
            print(f"Значение ячейки ({row_number}, {column_number}): {cell_value}")
    
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("В командной строке введите <путь_к_csv_файлу> <номер_строки> <номер_колонки>")
    else:
        file_path = sys.argv[1]
        row_number = int(sys.argv[2])
        column_number = int(sys.argv[3])
        get_cell_value(file_path, row_number, column_number)
