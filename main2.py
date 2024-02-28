from datetime import date
import time
import sys
import matplotlib.pyplot as plt
import serial
from read_m52_class import m5logger2

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

data0=[0]*10
data=[data0]*10
ser = serial.Serial(sys.argv[1],sys.argv[2])
sport=m5logger2()

while True:
 try:
  ttime=time.time()-start
  if ttime<0.001:
    ttime=0.0
  st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
  ss=str(time.time()-int(time.time()))
  rttime=round(ttime,2)
  array=sport.read_logger(ser)
  f.write(st+ss[1:5]+","+str(rttime)+","
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9])
  +"\n")
  print(st+ss[1:5]+","+str(rttime)+","
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+","+str(array[8])+","+str(array[9]))
  data.pop(-1)
  data.insert(0,array)
  rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
  x=range(0, 10, 1)
  plt.figure(200)
  plt.clf()
  plt.ylim(-25,30)
  tl0,=plt.plot(x,rez[0],label="T0")
  tl1,=plt.plot(x,rez[1],label="T1")
  tl2,=plt.plot(x,rez[2],label="T2")
  tl3,=plt.plot(x,rez[3],label="T3")
  tl4,=plt.plot(x,rez[4],label="T4")
  tl5,=plt.plot(x,rez[5],label="T5")
  tl6,=plt.plot(x,rez[6],label="T6")
  tl7,=plt.plot(x,rez[7],label="T7")
  tl8,=plt.plot(x,rez[8],label="T8")
  tl9,=plt.plot(x,rez[9],label="T9")
  plt.legend(handles=[tl0,tl1,tl2,tl3,tl4,tl5,tl6,tl7,tl8,tl9])
  plt.pause(0.1)
 except KeyboardInterrupt:
  f.close()
  ser.close()
  exit()
