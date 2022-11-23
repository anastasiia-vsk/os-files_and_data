from datetime import datetime
now = datetime.now()
print(now)
birthday = str(input("Введіть дату народження: "))
birthday_date = datetime.strptime(birthday, "%d-%m-%Y %H:%M:%S.%f")

millisec_birthday = birthday_date.timestamp() * 1000
millisec_now = now.timestamp() * 1000

years_old = millisec_now - millisec_birthday

#print(birthday_date)
#print(years_old_1)

print(years_old)

#05-10-2016 13:30:00.0