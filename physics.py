from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import os
import numpy as np
import time
from math import sin, cos, radians, pi
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import cv2

#All measurements are in SI units

#1000 time steps
total_state=1000000;

#3 features on the state [mass,x,y]
fea_num=3;

#G
G = 6.67428e-11;

#time step
diff_t=0;

def setup(total_state,n_body,fea_num,orbit):
  time_body_masspos = np.zeros((total_state,n_body,fea_num),dtype=float);
  if(orbit):
    diff_t = 1;
    time_body_masspos[0][0][0]=100 + np.random.rand()*400;
    time_body_masspos[0][0][1:fea_num]=0.0;
    for i in range(1,n_body):
      time_body_masspos[0][i][0]=np.random.rand()*8.98+0.02;
      distance=np.random.rand()*90.0+10.0;
      theta=np.random.rand()*360;
      theta_rad= radians(theta);
      #theta_rad = pi/2 - radians(theta);
      time_body_masspos[0][i][1]=distance*cos(theta_rad);
      time_body_masspos[0][i][2]=distance*sin(theta_rad);

  else:
    diff_t = 0.01;
    for i in range(n_body):
      time_body_masspos[0][i][0]=np.random.rand()*8.98+0.02;
      distance=np.random.rand()*90.0+10.0;
      theta=np.random.rand()*360;
      theta_rad= radians(theta);
      #theta_rad = pi/2 - radians(theta);
      time_body_masspos[0][i][1]=distance*cos(theta_rad);
      time_body_masspos[0][i][2]=distance*sin(theta_rad);
  return time_body_masspos;

#def norm(x):
# return np.sqrt(np.sum(x**2));

def gen(n_body,orbit):
  # initialization on just first state
  time_body_masspos=setup(total_state,n_body,fea_num,orbit);
  for i in range(1,total_state):
    time_body_masspos[i]=calc(time_body_masspos[i-1],n_body);
  return time_body_masspos;

def calc(cur_state,n_body):
  next_state=np.zeros((n_body,fea_num),dtype=float);
  #f_mat=np.zeros((n_body,n_body,2),dtype=float);
  #f_sum=np.zeros((n_body,2),dtype=float);
  #acc=np.zeros((n_body,2),dtype=float);
  for i in range(n_body):
    for j in range(i+1,n_body):
      if(j!=i):
        fx=get_force(cur_state[i][:3],cur_state[j][:3],x);
        fy = get_force(cur_state[i][:3], cur_state[j][:3], y);
        #fz = get_force(cur_state[i][:3], cur_state[j][:3], 'z');
        #f_mat[i,j]+=f;
        #f_mat[j,i]-=f;
    #f_sum[i]=np.sum(f_mat[i],axis=0);
    #acc[i]=f_sum[i]/cur_state[i][0];
    #next_state[i][0]=cur_state[i][0];
    next_state[i][3:5]=cur_state[i][3:5]+acc[i]*diff_t;
    next_state[i][1:3]=cur_state[i][1:3]+next_state[i][3:5]*diff_t;
  return next_state;

def get_force(body1, body2, axis):
  if(axis == 'x'):
    delta = abs(body1[1]-body2[1]);
  elif(axis == 'y'):
    delta = abs(body1[2] - body2[2]);
  else:
    delta = abs(body1[3]-body2[3]);
  F = (G*body1[0]*body2[0])/(delta**2)
  return F

def F(x):
    return

"""def make_video(xy,filename):
  os.system("rm -rf pics/*");
  FFMpegWriter = manimation.writers['ffmpeg']
  metadata = dict(title='Movie Test', artist='Matplotlib',
                  comment='Movie support!')
  writer = FFMpegWriter(fps=15, metadata=metadata)
  fig = plt.figure()
  plt.xlim(-200, 200)
  plt.ylim(-200, 200)
  fig_num=len(xy);
  color=['ro','bo','go','ko','yo','mo','co'];
  with writer.saving(fig, filename, len(xy)):
    for i in range(len(xy)):
      for j in range(len(xy[0])):
        plt.plot(xy[i,j,1],xy[i,j,0],color[j%len(color)]);
      writer.grab_frame();"""

if __name__=='__main__':
    time_body_masspos = gen(3,True);
    #xy=data[:,:,1:3];
    #make_video(xy,"test.mp4");
