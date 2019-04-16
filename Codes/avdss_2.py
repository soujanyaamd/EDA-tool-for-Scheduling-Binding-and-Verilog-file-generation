import csv
import numpy

def ASAP():
    asaplist=[0]*row_count
    l=0
    tslist = [[0]]
    timeslot=1
    ltemp=[]
    for i in range (1,row_count):
        if(dataflow[i,3]=='ind' and dataflow[i,7]=='ind'):
            ltemp.append(i)
            asaplist[i]=timeslot
    tslist.append(ltemp)
    while ((len(tslist)*(l-2))<row_count):
        ltemp=[]
        timeslot=timeslot+1
        for j in range (1,row_count):
            for y in range (0, len(tslist[l+1])):
                if(input1[j-1]==outputs[tslist[l+1][y]-1]):
                    asaplist[j]=timeslot
                    ltemp.append(j)
        tslist.append(ltemp)
        l=l+1
    print('Time Slot List',tslist)
    return asaplist   # containing time slot of each operator in seq
def ALAP(dataflow): 
    return alaplist   # containing time slot of each operator in seq
def ILP(asaplist, alaplist):    
    return ilplist    # containing time slot of each operator aft scheduling with resource constraint
inputs = csv.reader(open("input.csv"), delimiter=",")
file = open("input.csv")
row_count = len(file.readlines())
#print(row_count)
x = list(inputs)
dataflow = numpy.array(x)
#print(dataflow)
with open('input.csv') as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            data.setdefault(header, list()).append(value)
outputs = data['OUTPUT']
input1 = data['INPUT 1']
input2 = data['INPUT 2']
operators = csv.reader(open("operators.csv"), delimiter=",")
y = list(operators)
operator_constraints = numpy.array(y)
asaplist=ASAP()
print ('ASAP LIST',asaplist)
