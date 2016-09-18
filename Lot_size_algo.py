# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 17:43:38 2016

@author: Dylan
"""

# Wagner-whitin algorithm draft

# Define week as namedtuple
from collections import namedtuple
Week = namedtuple( "Week", [ 'index', 'demand' ] )

# Define inputs
setup_cost = 50.0
holding_cost = 0.5 # per unit demand per week
#weeks = [ Week( 1, 120), Week( 2, 80 ), Week( 3, 94 ), Week( 4, 78 ), Week( 5, 86 ),Week(6,110) ]
#[120,	80,	94,	78,	86, 110
weeks = [ Week( 1, 100), Week( 2, 100 ), Week( 3, 50 ), Week( 4, 50 ), Week( 5, 210 ) ]
print weeks

# Prepare an empty matrix to store c_kj
c = []
for i in xrange( 1, len(weeks) + 1 ):
    new_row = []
    for j in xrange( 1, len(weeks) + 2 ):
        new_row.append( 0 )
    c.append( new_row )

print c

# Double loop to fill this matrix
for i in xrange( 0, len(weeks) ):
    c[i][i+1] = setup_cost
    print 'i= ', i
    for j in xrange( i + 2, len(weeks) + 1 ):
        print 'j= ', j
        c[i][j] = c[i][j-1] + holding_cost * weeks[ j-1 ].demand * ( j - (i+1) )
    
print c ,len(c), len(c[0])
f=[]

for i in xrange(0,len(weeks)+1):
    f.append(0)
print f
for i in xrange(len(weeks)-1,-1,-1):
    temp=[]
   
    
    for l in range(len(weeks),0,-1):
        if c[i][l]==0:
            break
  
        temp.append(c[i][l]+f[l])
    f[i]=min(temp)
print f
k=[]

        

for i in range (len(f)-1,0,-1):
    val=0
#    print i
    val=f[i-1]-f[i]
    k.append(val)
k.reverse()
print k
ans=[]
for i in xrange(0,len(weeks)):
    ans.append(0)
print ans    


for i in xrange( 0, len(weeks) ):
    c[i][i+1] = c[i][i+1]+f[i+1]
    print 'i= ', i
    for j in xrange( i + 2, len(weeks) + 1 ):
        print 'j= ', j
        c[i][j] = c[i][j]+f[j]
coded_ans=[]

for i in xrange(0,len(c)):
    print i
    print c[i]
    print f[i]
    value=c[i].index(f[i])
    coded_ans.append(value)
print coded_ans
#lets build the answer now
answer=[]
for i in xrange(0,len(weeks)):
    answer.append(0)
 
completed = 0
for i in range(len(coded_ans)):
    if completed!= i:
        continue
    value = coded_ans[i]
    total_demand = 0
    for j in range(completed,value):
        total_demand += weeks[j].demand
        completed += 1
        
        
    answer[i] = total_demand
        
print answer

#for i in range (len(k)-1,-1,-1):
#    print "i is", i
#    if k[i]==0:
#        break
#    if k[i]==setup_cost:
#        ans[i]=ans[i]+weeks[i].demand
#    else:
#        flag=True
#        p=1
#        j=i
#        
#        while flag:
#           print "here j is" 
#           print j 
#           print "k[i] is ",k[i]
#           print weeks[j]
##           print ans[j]
#           if k[i]== weeks[j].demand*holding_cost*p:
#               ans[j-1]=ans[j]+weeks[i].demand
#               flag=False
#           else:
#               j=j-1
#               p=p+1
#    print ans

#weeks = [ Week( 1, 100 ), Week( 2, 100 ), Week( 3, 50 ), Week( 4, 50 ), Week( 5, 210 ) ]
    
    
# Loop to find all the "f"s, beginning with f_6 = 0, proceeding to f_5, then to f_4, etc., to f_1

# Recover the optimal solution from the knowledge of the "f"s


