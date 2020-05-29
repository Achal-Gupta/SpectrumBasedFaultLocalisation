import sys
import time
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import numpy as np
import math
import os
import csv


cwd =os.getcwd()
version=cwd.split("/")[-1]
program_name=cwd.split("/")[-2].split("_")[0]
print(cwd)
str_cwd=cwd.replace("/"+program_name+"/"+version,"")
print(str_cwd)
f_l=0

start_time=datetime.now()

with open('faultyLine.txt') as f:
    f_l = f.readline()

print("**************")
print(f_l)
print("**************")

f_l=int(f_l)




############Original##############
st1 = datetime.now()
df_train=pd.read_csv('statementResult.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed

suspicious=[]
#print len(y)
#print len(x[0])
#print total_passed,total_failed


f = total_failed
p = total_passed


for i in range(0,len(x[0])):
    nsuccess=0
    nfailure=0
    for j in range(0,len(y)):
        #print x[j][i],y[j][0]
        if x[j][i]==1 and y[j][0]==0:
            nsuccess=nsuccess+1
        elif x[j][i]==1 and y[j][0]==1:
            nfailure=nfailure+1
    try:
        #nfailure=Ncf... nsuccess=Ncs
        #Nf=total_failed.... Ns=total_passed
        #print nfailure,nsuccess

        ep = nsuccess
        ef = nfailure
        np1 = p - ep
        nf = f - ef

        sus_score = float(ef)/float(f)
        suspicious.append(sus_score)
        print(str(i)+"   "+str(sus_score))
    except ZeroDivisionError:
        suspicious.append(0)

d = {}
for i in range(0,len(suspicious)):
    key = float(suspicious[i])
    #print key
    if key !=0:
        if key not in d:
            d[key] = []
        d[key].append(i)

ct1=0
ct2=0
ct3=0
fct=0
print("Faulty line:"+str(f_l))
for x in sorted(d):
    print (x,len(d[x]))
    if f_l not in d[x] and fct==0:
          ct1=ct1+len(d[x])
    elif f_l not in d[x] and fct==1:
          ct3=ct3+len(d[x])
    else:
        fct=1
        ct2=len(d[x])
print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))

nwt1= (datetime.now() -st1)
o1=ct3+1
o2=ct3+ct2






############Original with uniqueness##############
st2 = datetime.now()
df_train=pd.read_csv('uniqueResult.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed

suspicious=[]
#print len(y)
#print len(x[0])
#print total_passed,total_failed


f = total_failed
p = total_passed


for i in range(0,len(x[0])):
    nsuccess=0
    nfailure=0
    for j in range(0,len(y)):
        #print x[j][i],y[j][0]
        if x[j][i]==1 and y[j][0]==0:
            nsuccess=nsuccess+1
        elif x[j][i]==1 and y[j][0]==1:
            nfailure=nfailure+1
    try:
        #nfailure=Ncf... nsuccess=Ncs
        #Nf=total_failed.... Ns=total_passed
        #print nfailure,nsuccess

        ep = nsuccess
        ef = nfailure
        np1 = p - ep
        nf = f - ef

        sus_score = float(ef)/float(f)
        suspicious.append(sus_score)
        print(str(i)+"   "+str(sus_score))
    except ZeroDivisionError:
        suspicious.append(0)

d = {}
for i in range(0,len(suspicious)):
    key = float(suspicious[i])
    #print key
    if key !=0:
        if key not in d:
            d[key] = []
        d[key].append(i)

ct1=0
ct2=0
ct3=0
fct=0
print("Faulty line:"+str(f_l))
for x in sorted(d):
    print (x,len(d[x]))
    if f_l not in d[x] and fct==0:
          ct1=ct1+len(d[x])
    elif f_l not in d[x] and fct==1:
          ct3=ct3+len(d[x])
    else:
        fct=1
        ct2=len(d[x])
print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))

nwt2= (datetime.now() -st2)
o3=ct3+1
o4=ct3+ct2







############Original with slicing##############
st3=datetime.now()
#code for retriving the sliced data
sdf=pd.read_csv('slice1.csv')
ys=np.array([sdf['In_Slice']]).T
ys=ys.tolist()


df_train=pd.read_csv('statementResult.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed

suspicious=[]
#print len(y)
#print len(x[0])
#print total_passed,total_failed


f = total_failed
p = total_passed


for i in range(0,len(x[0])):
    nsuccess=0
    nfailure=0
    for j in range(0,len(y)):
        #print x[j][i],y[j][0]
        if x[j][i]==1 and y[j][0]==0:
            nsuccess=nsuccess+1
        elif x[j][i]==1 and y[j][0]==1:
            nfailure=nfailure+1
    try:
        #nfailure=Ncf... nsuccess=Ncs
        #Nf=total_failed.... Ns=total_passed
        #print nfailure,nsuccess

        ep = nsuccess
        ef = nfailure
        np1 = p - ep
        nf = f - ef

        if ys[i][0]==0:
            sus_score=-999
        else:
            sus_score = float(ef)/float(f)
        suspicious.append(sus_score)
        print(str(i)+"   "+str(sus_score))
    except ZeroDivisionError:
        suspicious.append(0)

d = {}
for i in range(0,len(suspicious)):
    key = float(suspicious[i])
    #print key
    if key !=0:
        if key not in d:
            d[key] = []
        d[key].append(i)

ct1=0
ct2=0
ct3=0
fct=0
print("Faulty line:"+str(f_l))
for x in sorted(d):
    print (x,len(d[x]))
    if f_l not in d[x] and fct==0:
          ct1=ct1+len(d[x])
    elif f_l not in d[x] and fct==1:
          ct3=ct3+len(d[x])
    else:
        fct=1
        ct2=len(d[x])
print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))

nwt3= (datetime.now() -st3)
o5=ct3+1
o6=ct3+ct2






############Original with slicing and uniqueness##############
st4=datetime.now()
#code for retriving the sliced data
sdf=pd.read_csv('slice1.csv')
ys=np.array([sdf['In_Slice']]).T
ys=ys.tolist()


df_train=pd.read_csv('uniqueResult.csv')

#training output dataset
y = np.array([df_train['Result']]).T
y=y.tolist()
#print y

#training input dataset
df_train.drop(['Result'],1 , inplace=True)
t_in = df_train.values.tolist()
x = np.array(t_in)
x=x.tolist()
#print len(y[0])
total_failed=np.count_nonzero(y)
total_passed=len(y)-total_failed

suspicious=[]
#print len(y)
#print len(x[0])
#print total_passed,total_failed


f = total_failed
p = total_passed


for i in range(0,len(x[0])):
    nsuccess=0
    nfailure=0
    for j in range(0,len(y)):
        #print x[j][i],y[j][0]
        if x[j][i]==1 and y[j][0]==0:
            nsuccess=nsuccess+1
        elif x[j][i]==1 and y[j][0]==1:
            nfailure=nfailure+1
    try:
        #nfailure=Ncf... nsuccess=Ncs
        #Nf=total_failed.... Ns=total_passed
        #print nfailure,nsuccess

        ep = nsuccess
        ef = nfailure
        np1 = p - ep
        nf = f - ef

        if ys[i][0]==0:
            sus_score=-999
        else:
            sus_score = float(ef)/float(f)
        suspicious.append(sus_score)
        print(str(i)+"   "+str(sus_score))
    except ZeroDivisionError:
        suspicious.append(0)

d = {}
for i in range(0,len(suspicious)):
    key = float(suspicious[i])
    #print key
    if key !=0:
        if key not in d:
            d[key] = []
        d[key].append(i)

ct1=0
ct2=0
ct3=0
fct=0
print("Faulty line:"+str(f_l))
for x in sorted(d):
    print (x,len(d[x]))
    if f_l not in d[x] and fct==0:
          ct1=ct1+len(d[x])
    elif f_l not in d[x] and fct==1:
          ct3=ct3+len(d[x])
    else:
        fct=1
        ct2=len(d[x])
print("We have to search "+str(ct3+1)+" to "+str(ct3+ct2))

nwt4= (datetime.now() -st4)
o7=ct3+1
o8=ct3+ct2








end_time=datetime.now()
csvfile=open(str_cwd+"/simpson.csv", "a+")
spamwriter1 = csv.writer(csvfile, delimiter=',')
stmt_complex=[]
stmt_complex.append(program_name);
stmt_complex.append(str(version));
#stmt_complex.append(str(sys.argv[1]));
stmt_complex.append(f_l);
stmt_complex.append(o1);
stmt_complex.append(o2);
stmt_complex.append(nwt1);
stmt_complex.append(o3);
stmt_complex.append(o4);
stmt_complex.append(nwt2);
stmt_complex.append(o5);
stmt_complex.append(o6);
stmt_complex.append(nwt3);
stmt_complex.append(o7);
stmt_complex.append(o8);
stmt_complex.append(nwt4);
spamwriter1.writerow(stmt_complex);
