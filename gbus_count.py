t=int(input())    #no. of test cases 
for test in range(t):
    if test==0:
        n=int(input())
    else:
        input()     #to cover up the blank line after each test case
        n=int(input())
    l=list(map(int,input().split()))
    
    buses={}      # the route of each bus will be stored in this dictionary
    i=1
    
    for d in l:       # this loop is used to store the route of each bus in the buses dictionary
        if i not in buses:
            buses[i]=[d]
        elif len(buses[i])<2:
            buses[i].append(d)
        else:
            i=i+1
            buses[i]=[d]
    
    p=int(input())
    cities={}
             #this dictionary will contain the cities which need to be monitored
    for _ in range(p):     #first each city is initialized to zero
        cities[int(input())]=0
        
    for city in cities:       #Monitor all buses in each city if it falls in the route range than increment the city
        for bus in buses:
            if buses[bus][0]<=city<=buses[bus][1]:
                cities[city]+=1
    result=[]
    
    for city in cities:      #store all the cities in a list
        result.append(cities[city])
        
    print("Case #{}: {}".format(test+1, ' '.join(map(str,result))))
    