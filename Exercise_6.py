def func(way_list_1, way_list_2):
    if way_1[-3:] == 'txt':
        print("Файл " + way_1 + " формату *.txt.")
    elif way_1[-3:] == 'csv':
        print("Файл " + way_1 + " формату *.csv.")
    elif way_1[-3:] == 'dat':
        print("Файл " + way_1 + " формату *.dat.")

    if way_2[-3:] == 'txt':
        print("Файл " + way_2 + " формату *.txt.")
    elif way_2[-3:] == 'csv':
        print("Файл " + way_2 + " формату *.csv.")
    elif way_2[-3:] == 'dat':
        print("Файл " + way_2 + " формату *.dat.")

    with open(way_1, 'r') as w:
        content = w.read()

    with open(way_2, 'w') as k:
        print(content, file=k)

    return ""

way_1 = str(input("Вкажіть перший файл: "))
way_2 = str(input("Вкажіть другий файл: "))
way_list_2 = list(way_2)
way_list_1 = list(way_1)

print(way_list_1)

func(way_list_1, way_list_2)

#Exercise_6.txt
#Exercise_6.csv
