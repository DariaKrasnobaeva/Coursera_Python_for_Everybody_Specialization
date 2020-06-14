#Welcome Daria Krasnobaeva from Using Python to Access Web Data

#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and
#numbers. You will extract all the numbers in the file and compute the sum
#of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample file where we
#give you the sum for your testing and the other is the actual data you
#need to process for the assignment.

#Sample data: XXXXX(There are 90 values with a sum=445833)
#Actual data: XXXXX (There are 84 values and the sum ends with 522)

import re
handle = open('regex_sum_620030.txt')
numbers=list()
count=0
sum=0

for line in handle:
    stuff=re.findall('\d+',line)
    for i in stuff:
        sum=sum+float(i)
        count=count+1
print(sum, count)
    #    numbers.append(i)
    #if len(stuff)!=1:
    #    continue
    #numbers.append(stuff)
#    count=count+1
    #print(numbers)
    #
