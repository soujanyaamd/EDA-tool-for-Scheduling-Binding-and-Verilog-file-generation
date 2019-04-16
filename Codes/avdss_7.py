import csv
import numpy

def SCHEDULING():
    print('SCHEDULING AND BINDING SOLUTION')
    print(' ')
    l=0
    v=1
    tslist = [[0]]
    templist=[]
    ltemp=templist
    templist=[]
    tempoplist=[]
    oplist=tempoplist
    tempoplist=[]
    for i in range (1,row_count):
        if(dataflow[i,3]=='ind' and dataflow[i,7]=='ind'):
            ltemp.append(i)
            oplist.append(op[i-1])
    my_dict={i:oplist.count(i) for i in oplist}
    for key in my_dict:
        for k in range (1, row_count_op):
            if(key==operator[k-1]):
                if(int(quantity[k-1])<my_dict[key]):
                    extra=my_dict[key]-int(quantity[k-1])
                    for m in range (extra, len(ltemp)-1):
                        templist.append(ltemp[len(ltemp)-m])
                        tempoplist.append(oplist[len(oplist)-m])
                        ltemp[len(ltemp)-m]=0
                        oplist[len(oplist)-m]=0
                else:
                    m=0
    ltemp=ltemp[:len(ltemp)-m]
    oplist=oplist[:len(oplist)-m]
    tslist.append(ltemp)
    my_dict={i:oplist.count(i) for i in oplist}
    maximum=[]
    print('TIMESLOT ',1)
    for key in my_dict:
        for k in range (1, row_count_op):
            if(key==operator[k-1]):
                maximum.append(timereq[k-1])
                for r in range (my_dict[key]):
                    print('operation',ltemp[r],'---->', key, r+1)
    print('Time slot 1 ---->',max(maximum),'nanoseconds')
    timerequired=int(max(maximum))
    print(' ')
    v=v+len(tslist[len(tslist)-1])
    while (1):
        ltemp=[]
        oplist=[]
        for z in range (0, len(templist)):
            ltemp.append(templist[z-1])
            oplist.append(tempoplist[z-1])
        templist=[]
        tempoplist=[]
        for j in range (1,row_count):
            lentslist=len(tslist)-1
            for y in range (0, len(tslist[lentslist])):
                if((input1[j-1]==outputs[tslist[lentslist][y]-1])):
                    ins = j
                    check1=1
                    break
                else:
                    check1=0
            for f in range (0,lentslist):
                for g in range (0, len(tslist[f])):
                    if(input2[j-1]==outputs[tslist[f][g]-1] or type2[j-1]=='NIL' or type2[j-1]=='ind'):
                        check2=1
                        break
                    else:
                        check2=0
                if (check2==1):
                    break
                
            for y in range (0, len(tslist[lentslist])):                
                if((input2[j-1]==outputs[tslist[lentslist][y]-1])):
                    check3=1
                    ins=j
                    break
                else:
                    check3=0
            for f in range (0,lentslist):
                for g in range (0, len(tslist[f])):
                    if(input1[j-1]==outputs[tslist[f][g]-1] or type2[j-1]=='NIL' or type2[j-1]=='ind'):
                        check4=1
                        break
                    else:
                        check4=0
                if(check4==1):
                    break
            if((check1==1 and check2==1) or (check3==1 and check4==1)):
                oplist.append(op[ins-1])
                ltemp.append(ins)
        l=l+1
        my_dict={i:oplist.count(i) for i in oplist}
        for key in my_dict:
            for k in range (1, row_count_op):
                if(key==operator[k-1]):
                    if(int(quantity[k-1])<my_dict[key]):
                        extra=my_dict[key]-int(quantity[k-1])
                        for m in range (0,extra):
                            p=0
                            for q in (0,len(oplist)-1):
                                if(p>=extra):
                                    break
                                if(oplist[p]==key):
                                    temp=ltemp[p]
                                    ltemp[p]=0
                                    oplist[p]=0
                                    tempoplist.append(key)
                                    templist.append(temp)
                                    p=p+1
                                else:
                                    continue
        ltemp=[x for x in ltemp if x!=0]
        oplist=[x for x in oplist if x!=0]
        if (ltemp != []):
            tslist.append(ltemp)
        my_dict={i:oplist.count(i) for i in oplist}
        t=0
        maximum=[]
        print('TIMESLOT ',l+1)
        for key in my_dict:
            for k in range (1, row_count_op):
                if(key==operator[k-1]):
                    maximum.append(timereq[k-1])
                    for r in range (my_dict[key]):
                        print('operation',ltemp[r+t],'---->', key, r+1)
            t=t+1
        print('Time required for slot', l+1, '---->',max(maximum),'nanoseconds')
        print(' ')
        timerequired=timerequired+int(max(maximum))
        v=v+len(tslist[len(tslist)-1])
        if v>row_count-1:
            break
    print('Total Time Required to complete the sequence of operations =',timerequired)
    return

inputs = csv.reader(open("input.csv"), delimiter=",")
x = list(inputs)
dataflow = numpy.array(x)
file = open("input.csv")
row_count = len(file.readlines())
with open('input.csv') as infile:
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            data.setdefault(header, list()).append(value)
outputs = data['OUTPUT']
input1 = data['INPUT 1']
input2 = data['INPUT 2']
type2 = data['TYPE 2']
op = data['OPERATOR']
operators = csv.reader(open("operators.csv"), delimiter=",")
y = list(operators)
operator_constraints = numpy.array(y)
file1 = open("operators.csv")
row_count_op = len(file1.readlines())
with open('operators.csv') as infile1:
    reader = csv.DictReader(infile1)
    data1 = {}
    for row in reader:
        for header, value in row.items():
            data1.setdefault(header, list()).append(value)
operator = data1['TYPE OF OP']
timereq = data1['TIME REQUIRED IN NANO SECONDS']
quantity=data1['NUM OF UNITS']
SCHEDULING()
