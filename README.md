# EDA-tool-for-Scheduling-Binding-and-Verilog-file-generation

Given an input file and a resource constaints file in a specified csv format, this project can generate a optimal scheduling amd binding solution, adhering to the timing and resource constaints.
Based on the generated solution and the inputs files, a simulatable Verilog file is also generated.

As an example, the series of steps in the process of obtaining Pitch, Yaw and Roll values form the accelerometer sensor outputs, which are, acceration in X-dir (acc_x), acceration in Y-dir (acc_y) and acceration in Z-dir (acc_z).

The equations for the conversion are as follows:

acc_x = ((acc_x-thresh1)/adjustment-factor1) <br/>
acc_y = ((acc_y-thresh2)/adjustment-factor2) <br/>
acc_z = ((acc_z-thresh3)/adjustment-factor3) <br/>

pitch = atan(acc_x,sqrt(sq(acc_y)+sq(acc_z))) <br/>
yaw = atan(acc_z,sqrt(sq(acc_x)+sq(acc_y))) <br/>
roll = atan(acc_y,sqrt(sq(acc_x)+sq(acc_z))) <br/>

The series of steps is depicted in the dataflow graph named dataflow.pdf
