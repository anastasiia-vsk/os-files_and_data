def organize(date, ivent):
    with open("Календар.txt", "a") as file:
        file.write(date + ivent + "\n")
    return ""

date = str(input("Введіть дату та час: "))
ivent = str(input("Введіть подію:  "))

organize(date, ivent)

#ivent = str(input("Введіть подію: "))
#date_final = datetime.strptime(date, "%d/%m/%Y %H:%M")

#05/10/2016 13:30
#Обід