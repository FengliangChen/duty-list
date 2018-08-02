#!/usr/bin/env python3

import calendar
import copy

morning = 3
noon = 6
night = 9

k = calendar.monthrange(2018,8)

def get_whenday(day):
	return calendar.weekday(2018,8,day)

# generate a list of days, with sub-list represents the 3 duty status.
duty = [0, 0, 0]
month_list =[]
month_days = int(k[1])
a=0
while a < month_days:
	month_list.extend('1')
	month_list[a] = copy.deepcopy(duty)
	a += 1

simon = month_list


#How many days in the first circulation(Two weeks).
def cir_days():
	if k[0] > 5:
		return 15
	else:
		return 14 - k[0]


# Give value to list.
point_to_shift = 0  #Note only consider 3 circulation.
day = 1
point_to_day = day - 1
first_cir = cir_days()

def shift_value():
	if point_to_shift == 0:
		return 3
	if point_to_shift == 1:
		return 6
	if point_to_shift == 2:
		return 9

for n in range(first_cir):
	day += 1
	print('hahaha',day,point_to_day)
	if get_whenday(day-1) < 6:
		simon[point_to_day][point_to_shift] = shift_value()
	else:
		simon[point_to_day][point_to_shift] = 0
	point_to_day += 1

if get_whenday(1) != 6:
	point_to_shift += 1

while point_to_day < k[1]:
	for n in range(14):
		day += 1
		print('day is',day,point_to_day)
		if day > k[1] + 1:
			break
		if get_whenday(day-1) < 6:
			simon[point_to_day][point_to_shift] = shift_value()
		else:
			simon[point_to_day][point_to_shift] = 0
		point_to_day += 1
	point_to_shift += 1

print(simon)

