import os
import numpy as np
import pandas as pd

with open('config.txt') as f:
    s=f.readlines()
    duration= int(s[0])
    period= int(s[1])* duration
    pc_daisu=int(s[2])

    print(duration,period,pc_daisu)

model_name =[]
Jikyo_time=[]
Yosyoku_time = []

with open('time.txt') as f:
    s=f.readline()
    model_sum= int(s[0])
    for i in  range(1,model_sum+1):
        s= f.readline().split()
        model_name.append(s[0])
        Jikyo_time.append(int(s[1]))
        Yosyoku_time.append(int(s[2]))
        #print(f.readline().split())
        print(model_name[i-1] ,Jikyo_time[i-1],Yosyoku_time[i-1])

calc_list=[]
for i in range(0, int(period/duration)):
    print("i:",i)
    
    for j in range(1,model_sum+1): 
        print("j:",j)
        calc_list.append([i,j,0,Jikyo_time[j-1]])
        print("i*j+j",i*j+j)
        print(calc_list[i*model_sum+j-1])

#print(calc_list)

#print(len(calc_list))
print("calc_list[47]の各要素")
print(calc_list[47][0])
print(calc_list[47][1])
print(calc_list[47][2])
print(calc_list[47][3])
print("calc_list[47]の各要素")
print("test github")
print("test github")


        


""" b = np.array([[0,1,2],[4,5,6],[8,9,10],
                      [12,13,14],[16,17,18],[20,21,22]])
print(b)

print(b[0,1])
print(b[1,1]) """
