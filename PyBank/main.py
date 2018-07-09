import csv

csvpath = 'budget_data.csv'
num_months = 0
net_amount = 0
net_change = 0
last_amount = 0
first_row = True
greatest_increase_val = 0
greatest_decrease_val = 0

with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = '\n')
	csv_header = next(csvreader)

	for row in csvreader:

# The total number of months included in the dataset
		num_months += 1

# The total net amount of "Profit/Losses" over the entire period
		date_amount = row[0].split(",")
		this_amount = int(date_amount[1])
		this_date = date_amount[0]
		net_amount += this_amount

# The average change in "Profit/Losses" between months over the entire period
		if first_row is True:
			change = 0
			first_row = False
		else:
			change = this_amount - last_amount
		net_change += change
		last_amount = this_amount

# The greatest increase in profits (date and amount) over the entire period
		if this_amount > greatest_increase_val:
			greatest_increase_val = this_amount
			greatest_increase_date = this_date
# The greatest decrease in losses (date and amount) over the entire period
		elif this_amount < greatest_decrease_val:
			greatest_decrease_val = this_amount
			greatest_decrease_date = this_date

avg_change = round(net_change / (num_months - 1),2)		

output_file = "output.txt"
with open(output_file, 'w') as datafile:
	writer = csv.writer(datafile)
	writer.writerow(["Financial Analysis"])
	writer.writerow([("------------------")])
	writer.writerow(["Total months : " , str(num_months)])
	writer.writerow(["Net Amount : " , str(net_amount)])
	writer.writerow(["Average Change : " , str(avg_change)])
	writer.writerow(["Greatest Increase in Profits :" + str(greatest_increase_date) + " (" + str(greatest_increase_val) + ")"])
	writer.writerow(["Greatest Decrease in Profits :" + str(greatest_decrease_date) + " (" + str(greatest_decrease_val) + ")"])


print("Financial Analysis")
print ("-----------------")
print("Total months : " + str(num_months))
print("Net Amount : " + str(net_amount))
print("Average Change : " + str(avg_change))
print("Greatest Increase in Profits :" + str(greatest_increase_date) + " (" + str(greatest_increase_val) + ")")
print("Greatest Decrease in Profits :" + str(greatest_decrease_date) + " (" + str(greatest_decrease_val) + ")")



