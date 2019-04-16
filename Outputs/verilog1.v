module avd (input acc_x,acc_y,acc_z,output pitch,yaw,roll);
reg acc_x1,acc_x2,acc_sq_x,acc_y1,acc_y2,acc_sq_y,acc_z1,acc_z2,acc_sq_z,pitch1,pitch2,pitch3,yaw1,yaw2,yaw3,roll1,roll2,roll3;
parameter adj1=0.34,para1=0.72,adj2=0.1,para2=0.23,adj3=0.39,para3=0.11;
always@(clk)
begin
acc_x1<=acc_x+adj1;
acc_y1<=acc_y+adj2;
acc_z1<=acc_z+adj3;
#1 acc_z2<=acc_z1/para3;
#4 acc_x2<=acc_x1/para1;
acc_sq_z<=sq(acc_z2);
#7 acc_y2<=acc_y1/para2;
acc_sq_x<=sq(acc_x2);
#10 acc_sq_y<=sq(acc_y2);
roll1<=acc_sq_z-acc_sq_x;
#12 pitch1<=acc_sq_y-acc_sq_z;
yaw1<=acc_sq_x-acc_sq_y;
yaw1<=acc_sq_x-acc_sq_y;
#16 pitch2<=sqrt(pitch1);
yaw2<=sqrt(yaw1);
yaw2<=sqrt(yaw1);
#20 yaw3<=yaw2*acc_z2;
roll<=atan(roll3);
#24 pitch3<=pitch2*acc_x2;
yaw<=atan(yaw3);
#28 pitch<=atan(pitch3);
#32 $finish
end
endmodule
