import csv
import os

TotalEarnings = 0
GreatestIncrease = 0
GreatestDecrease = 0
MonthList = []
ProfitList = []
ChangeList = []

input_file = os.path.join("Resources","budget_data.csv")
output_file = os.path.join("Analysis","report.txt")

data = open(input_file)

reader = csv.reader(data)
next (reader, None)

earnings = {}

                                #Creates a dict w/ months as the keys and profit as the value
for row in reader:
    earnings[row[0]] = float(row[1])
                                #Uses key count to derive total months
TotalMonths = len(earnings.keys())
                                #Loops through dict to collect values into 2 lists and calculates total earnings
for month, profit in earnings.items():
    TotalEarnings = TotalEarnings + profit
    MonthList.append(month)
    ProfitList.append(profit)
    
for i in range(len(ProfitList)-1):
                                                    #Populates difference per entry to calculate average change
    ChangeList.append(float(ProfitList[i+1] - ProfitList[i]))
    
    if ProfitList[i+1] - ProfitList[i] > GreatestIncrease:
        GreatestIncrease = ProfitList[i+1] - ProfitList[i]
        GeatestIncreaseMonth = MonthList[i+1]
                                                                #Identifies greatest increase/decrease and stores values
    elif ProfitList[i+1] - ProfitList[i] < GreatestDecrease:
        GreatestDecrease = ProfitList[i+1] - ProfitList[i]
        GeatestDecreaseMonth = MonthList[i+1]
    else:
        pass


AverageChange = round(sum(ChangeList)/len(ChangeList), 2)

print(f"Total Months: {TotalMonths}")
print(f"Total: {TotalEarnings}")    
print(f"Average Change: {AverageChange}")
print(f"The greatest increase in profits: {GeatestIncreaseMonth} $ {GreatestIncrease}")
print(f"The greatest decrease in profits: {GeatestDecreaseMonth} $ {GreatestDecrease}")

w = open(output_file, 'w')

w.write(f'''
Total Months: {TotalMonths}
Total: {TotalEarnings}
Average Change: {AverageChange}
The greatest increase in profits: {GeatestIncreaseMonth} $ {GreatestIncrease}
The greatest decrease in profits: {GeatestDecreaseMonth} $ {GreatestDecrease}

''')

w.close()


