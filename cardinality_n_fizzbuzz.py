import itertools
import operator
#1.
l = [('ak',2),("glock",3),("adar",5)]

#yes this is a more understandable way to do this problem.
#i could've just work through the original list of tuples itself. 
def fizzbuzz_maker(list):
    l.sort(key=operator.itemgetter(1),reverse=True)
    low = []
    lon = []
    str = ''

    for i in range(0, len(l)):
        low.append(l[i][0])
        lon.append(l[i][1])
    
    for i in range (1,101):
        if any(i % x == 0 for x in lon) == False:
            print(i)
        else:
            for j in range(0, len(lon)):
                if i % lon[j] == 0:
                    print(low[j])


fizzbuzz_maker(l)


#2.
#use combinations cos order doesn't matter
s = {1,2,3,4,5}
def half_pset(set):
    list_of_half_psets = []
    if len(set) < 2:
        print(set)
    else:
        for i in range(0, int(len(set)/2 +1)):
            list_of_half_psets.append(list(itertools.combinations(set,i)))
    return list_of_half_psets

print(half_pset(s))



