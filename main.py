#Author Gogineni Sagar
#code to find the closest point to origin at a given direction(angle in degree)

from operator import sub
import math
def findPoint(p_1,angle,origin):
    m_0 = (math.tan((angle * math.pi) / 180))
    c_0 = origin[1] - m_0 * origin[0]
    slope_1 = map(sub, p_1[1], p_1[0])
    slope_1 = list(slope_1)
    m_1 = slope_1[1] / slope_1[0]
    a_1 = p_1[0][1] - m_0 * p_1[0][0] - c_0
    a_2 = p_1[1][1] - m_0 * p_1[1][0] - c_0
    c_1 = p_1[0][1] - m_1 * p_1[0][0]
    if ((a_1 * a_2) > 0):
        print("Line is excluded as it is not intersecting the angle" )
    else:
        point=[]
        point.append(p_1)
        return (calDist(m_1,c_1,p_1,m_0,c_0,origin))

def calDist(m_1,c_1,p_1,m_0,c_0,origin):
    dist={}
    X=(m_0-m_1)/(c_1-c_0)
    Y=m_0*(X)+c_0

    distance= math.sqrt((origin[0]-X)**2+(origin[1]-Y)**2)
    dist=[]
    dist.append(distance)
    return dist

allSegment=[]
allDist=[]
origin=[]
for j in range(2):
    z = int(input("Enter Points for Origin ", ))
    origin.append(z)
print("Origin is :",origin)

angle =int(input("Enter direction :"))
p1=[]
d1=[]

l = int(input("Enter number Line Segments:"))
for k in range(l):
    input_list = []
    for i in range(2):
        list1 = []
        for j in range(2):
            z = int(input("Enter Points for line",))
            list1.append(z)
        input_list.append(list1)
    p1=input_list
    d1=findPoint(p1,angle,origin)
    if(d1==None):
        d1=[100000000]
    allSegment.append(p1)
    allDist.append(d1)

print("All segment", allSegment)
print("All dist", allDist)

minDist=allDist.index(min(allDist))
print("the Closest line segment to ",origin,"is",allSegment[minDist])








