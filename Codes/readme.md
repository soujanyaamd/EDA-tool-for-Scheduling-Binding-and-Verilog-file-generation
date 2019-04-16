This folder contains the Python Codes to implement Scheduling, Binding and .v file generation

### 1. avdss_2.py
This is a simple code to schedule every operation AS SOON AS POSSILBLE (ASAP).<br/> 
It does not take into consideration the resource constraints. <br/>

This code outputs 2 lists: <br/>
1. Time Slot List:  It is a list of lists. The index of each list specifies the scheduled time slot of the opertions inside the list<br/>
2. ASAP List:  This list contains as many enteries as the number of operations to be performed. The number specified at a particular index indicates the Time Slot in which the operation corresponding to the index number is scheduled.<br/>


### 2. avdss_6.py
This code outputs the Time Slot List considering the Resource Constrains.


### 3. avdss_7.py
This code outputs the final Scheduling and Binding solution.
The operations performed in each time slot, the hardware it is bound to and the time required for each time slot is printed.

### 4. avdss_9.py
This code generates a simulatable verilog .v file along with the scheduling and binding solution.

### 5. avdss_10.py
This is same as avdss_9.py, but generates a Scheduling and Binding Solution and a verilog file based on the constraints given in operators1.csv
