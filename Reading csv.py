import csv
sum_ = 0
myset = []
with open('employee.csv') as csvfile:
      readCSV=csv.reader(csvfile,delimiter=';')
      for row in readCSV:
            sum_ = sum_ + int(row[3])
            myset.append(row[4])

      print(sum_)
      print(set(myset))