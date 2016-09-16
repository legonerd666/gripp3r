#!/usr/bin/python3
import ev3dev.ev3 as ev3

#This creates and runs the motor plugged into ev3 port B for 3 seconds
lm = ev3.LargeMotor('outB')
lm.run_timed(time_sp=3000, speed_sp=100)

#This creates and runs the motor plugged into ev3 port C for 3 seconds
rm = ev3.LargeMotor('outC')
rm.run_timed(time_sp=3000, speed_sp=100)
~                                          
