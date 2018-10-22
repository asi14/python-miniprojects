import datetime
import calendar

starting_date = 3
end_date = 22
month = 10
year=2018

for i in range(3,23):
	temp_datetime = datetime.datetime(year,month,i)
	weekday_num = temp_datetime.weekday()
	if weekday_num == 0 or weekday_num == 2:
		print(calendar.day_name[weekday_num] + ', ' + temp_datetime.strftime('%b %d, %Y') + '. 1:30pm - 3:30pm')	
	elif weekday_num == 4:
		print(calendar.day_name[weekday_num] + ', ' + temp_datetime.strftime('%b %d, %Y') + '. 1:00pm - 5:00pm')	
