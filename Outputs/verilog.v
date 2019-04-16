module avd (input acc_x,acc_y,acc_z,output pitch,yaw,roll);
reg acc_x1,acc_x2,acc_sq_x,acc_y1,acc_y2,acc_sq_y,acc_z1,acc_z2,acc_sq_z,pitch1,pitch2,pitch3,yaw1,yaw2,yaw3,roll1,roll2,roll3;
parameter adj1=0.82,para1=0.4,adj2=0.59,para2=0.1,adj3=0.1,para3=0.02;
always@(clk)
begin
acc_x1<=acc_x+adj1;
acc_y1<=acc_y+adj2;
#1 acc_z1<=acc_z+adj3;
acc_x2<=acc_x1/para1;
acc_y2<=acc_y1/para2;
#4 acc_sq_y<=sq(acc_y2);
acc_z2<=acc_z1/para3;
#7 acc_sq_z<=sq(acc_z2);
#9 acc_sq_x<=sq(acc_x2);
pitch1<=acc_sq_y+acc_sq_z;
#11 pitch2<=sqrt(pitch1);
yaw1<=acc_sq_x+acc_sq_y;
roll1<=acc_sq_z+acc_sq_x;
#15 pitch3<=pitch2*acc_x2;
yaw2<=sqrt(yaw1);
roll2<=sqrt(roll1);
#19 pitch<=atan(pitch3);
yaw3<=yaw2*acc_z2;
roll3<=roll2*acc_y2;
#23 yaw<=atan(yaw3);
roll<=atan(roll3);
#27 $finish
end
endmodule
