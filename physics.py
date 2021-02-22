"""Usage:
          physics.py
@ Jekaterina Gamper 2020
Runs physics simulation to produce visual data of bodies interacting through gravitational force.
------------------------------------------------
All measurements are in SI units:
Total_state - number of states(1000);
Fea_num - 3 features of the state [mass,x,y];
G - Gravitational const;
Diff_t - time step;
------------------------------------------------
Options:
  -h --help                       Show help.
  --version                       Show version.
"""

import argparse
import sys
import os
import numpy as np
import time
from math import sin, cos, radians, pi
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2


Total_state = 10
Fea_num = 3
G = 6.67428e-11
Diff_t = 1

def setupofthesystem(Total_state, n_body, Fea_num, orbit):
  time_body_masspos = np.zeros((Total_state, n_body, Fea_num), dtype=float)
  if(orbit):
    diff_t = 1
    time_body_masspos[0][0][0] = 100 + np.random.rand()*400
    time_body_masspos[0][0][1:Fea_num] = 0.0
    for i in range(1, n_body):
      time_body_masspos[0][i][0] = np.random.rand()*8.98+0.02
      distance = np.random.rand()*90.0+10.0
      theta = np.random.rand()*360
      theta_rad = radians(theta)
      time_body_masspos[0][i][1] = distance*cos(theta_rad)
      time_body_masspos[0][i][2] = distance*sin(theta_rad)

  else:
    diff_t = 1
    for i in range(n_body):
      time_body_masspos[0][i][0] = np.random.rand()*8.98+0.02
      distance = np.random.rand()*90.0+10.0
      theta = np.random.rand()*360
      theta_rad = radians(theta)
      time_body_masspos[0][i][1] = distance*cos(theta_rad)
      time_body_masspos[0][i][2] = distance*sin(theta_rad)
  return time_body_masspos


def producing_data(n_body, orbit):
  # initialization on just first state
  time_body_masspos = setupofthesystem(Total_state, n_body, Fea_num, orbit)
  print(time_body_masspos[0])
  for i in range(1, Total_state):
    print("state", i)
    time_body_masspos[i] = calc(time_body_masspos[i-1], n_body)
  return time_body_masspos

def calc(cur_state, n_body):
  next_state = np.zeros((n_body, Fea_num), dtype=float)
  for i in range(n_body):
    for j in range(n_body):
        if(i != j):
          print("ij force on i by j", i, j)
          fx = get_force(cur_state[i], cur_state[j], 'x')
          fy = get_force(cur_state[i], cur_state[j], 'y')
          print(fx, fy)
        #fz = get_force(cur_state[i], cur_state[j], 'z');
    #f_sum[i]=np.sum(f_mat[i],axis=0);
    #acc[i]=f_sum[i]/cur_state[i][0];
    #next_state[i][0]=cur_state[i][0];
    #next_state[i][3:5]=cur_state[i][3:5]+acc[i]*diff_t;
    #next_state[i][1:3]=cur_state[i][1:3]+next_state[i][3:5]*diff_t;
  return next_state

def get_force(body1, body2, axis):
  if(axis == 'x'):
    delta = body1[1]-body2[1]
    print(delta)
  elif(axis == 'y'):
    delta = body1[2] - body2[2]
  #else:
    #delta = body1[3]-body2[3];

  F = -1*(G*body1[0]*body2[0]*delta)/(delta**3)
  return F



if __name__=='__main__':
    time_body_masspos = producing_data(2, True)
    #xy=data[:,:,1:3];
    #make_video(xy,"test.mp4");