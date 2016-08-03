import math


#initilization of class
class hyperbox:
    v=None
    w=None
    name=''
    clas=None

#initialization of variables

h = [ hyperbox() for i in range(0,5)]
class_arr  = [] #classes of hyperbox
class_arr1  = []#only unique classes 
b=[range(1,5)]


inputs=[]

#input parameter should be passed in inputs array

#----------------------

#inputs=[1,2,5]


#----------------------


#h[]=hyperbox() Initialization of min and max values for hyperboxes

#h[1]=hyperbox()
h[1].v=[1,1.0,5]
h[1].w=[1,24.0,100]
h[1].clas=1
h[1].name='Dry Run'

#h[2]=hyperbox()
h[2].v=[2,0.0,5]
h[2].w=[2,1.0,100]
h[2].clas=2
h[2].name='Short Circuit'

#h[3]=hyperbox()
h[3].v=[3,0.0,5]
h[3].w=[3,1.0,100]
h[3].clas=3
h[3].name='Open Circuit'

#h[4]=hyperbox()
h[4].v=[4,0.0,5]
h[4].w=[4,1.0,100]
h[4].clas=4
h[4].name='MotorJam/Overload'

h[4].v=[6,1.0,5]
h[4].w=[6,24.0,100]
h[4].clas=5
h[4].name='OverTemperature'


#initilizing the input to hyperbox h[0]  
def initialize():
    h[0].v=inputs
    h[0].w=inputs
    h[0].clas=0
    h[0].name=None


#calculating function f(x,y), output ranges from 0 to 1
def f(a,b):
    global d
    c=a*b
    if c>1:
     d=1


    elif c<0:
     d=0

    elif range(0,1):
     d=c

    return d

#calculating membership function
def member(i):
    min1=[]
    #print("i:",i)
    for inp in range(len(inputs)):
        #print(h[0].w[inp],h[i].w[inp],h[i].v[inp],h[0].v[inp])
        min1.append(min(1-f(h[0].w[inp]-h[i].w[inp],4),1-f(h[i].v[inp]-h[0].v[inp],4)))
        #print("min:",min1[inp])
    #print("min val:", min(min1))
    b.append(min(min1))
    return min(min1)

#counting the number classes(total classes and class names and class declaration) 
def initclass():
    global cname,hyNum
    u1=0.0
    u=0.0
    cname=0
    hyNum=0
    for i in range(1,len(h)):
        class_arr.append(h[i].clas)
        #print (class_arr[i])
    #print("class: ",sorted(set(class_arr)))
    class_arr1=sorted(set(class_arr))
    count=len(sorted(set(class_arr)))
    #print("count:", count)
    for c in range(count):
        #print("c:",c,"classname:",class_arr1[c])
        for hyper in range(1,len(h)):
            #print("hyper:",hyper)
            mem = member(hyper)
            if h[hyper].clas==class_arr1[c]:
                u=1.0*mem
                #print("same",u)
            else:
                u=0.0*mem
                #print("not same",u)
            if u>u1:
                cname=h[hyper].clas
                #print("cname:",cname,"\t c:", h[hyper].clas)
                hyNum=hyper
                #print(hyNum)
                u1=u
    return hyNum








