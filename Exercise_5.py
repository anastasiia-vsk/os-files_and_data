from datetime import datetime
now = datetime.now()
str_now = str(now)
print(str_now)
type_1 = datetime.strptime(str_now, "%Y-%m-%d %H:%M:%S.%f")
#type_2 = datetime.strptime(str(now), "%m-%d-%Y %H:%M")
#type_3 = datetime.strptime(str(now), "%d/%m/%Y %H:%M")
#type_4 = datetime.strptime(str(now), "%Y-%m-%d %H:%M")

print(type_1)


#DD.MM.YYYY
#MM-DD-YYYY
#DD/MM/YYYY
#YYYY-MM-DD
