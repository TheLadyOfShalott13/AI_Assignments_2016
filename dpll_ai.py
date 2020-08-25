#! /usr/bin/env

import sys, copy
from collections import Counter

ipFile= open("clause.txt")
clauseSet = []
solved= {}


def DPLL(set_c):
    if(len(set_c) == 0): #empty
        return True
    for clause in set_c: #empty clause
        if(len(clause) ==1):
            return False
        
    global solved
    for clause in set_c: #unit propogation
        i = 0
        if(len(clause) == 2):
            unit = clause[0]
            if unit<0:
                solved[-1*unit] =0
            else:
                solved[unit]=1
            set_c.pop(i)
            i=0;
            while(i!= len(set_c)):
                marked = False
                for term in set_c[i]:
                    if term == unit:
                        marked = True
                        break
                    elif(term == (-1*unit)):
                        set_c[i].remove(term)

                if marked:
                    set_c.pop(i)
                    i= i-1
                i= i + 1
            return DPLL(copy.deepcopy(set_c))
        
        #newClause= set_c[0]
        #for clause in set_c:
        #    if len(newClause) > len(clause):
        #        newClause = clause
        #item = newClause[0]
        #temp= copy.deepcopy(set_c)
        #temp.remove(newClause)
        
        flattened = []
        for sublist in set_c:
            for val in sublist:
                flattened.append(val)
        chain= Counter(flattened)
        i=0
        maxFreq=0
        flattened = list(set(flattened))
        while (i!= len(flattened)/2 +1):
                if -1*flattened[i] in flattened:
                        unit_freq = chain[-1*flattened[i]] + chain[flattened[i]]
                else:
                        unit_freq = chain[flattened[i]]
                if unit_freq > maxFreq:
                        maxFreq = unit_freq
                        index=i
                i = i + 1
        if chain[-1*flattened[index]] >chain[flattened[index]]:
            item =-1*flattened[index]
        else:
            item =flattened[index]
        temp= copy.deepcopy(set_c)
        i=0
        while(i !=len(temp)):
            marked= False
            for term in temp[i]:
                if term == item:
                    marked= True
                    break
                elif (term ==(-1* item)):
                    temp[i].remove(term)
            if marked:
                temp.pop(i)
                i = i-1
            i= i+1
        temp_solve = copy.deepcopy(solved)
        done= DPLL(temp)
        if done:
            if item < 0:
                solved[-1* item]=0
            else:
                solved[item] =1
            return done
        else:
            solved = copy.deepcopy(temp_solve)
            item = -1*item
            temp=  copy.deepcopy(set_c)
            i=0
            while(i !=len(temp)):
                marked= False
                for term in temp[i]:
                    if term==item:
                        marked= True
                        break
                    elif (term ==(-1* item)):
                        temp[i].remove(term)
                if marked:
                    temp.pop(i)
                    i = i-1
                i= i+1
            if item < 0:
                solved[-1*item] = 0
            else:
                solved[item] = 1
                
        return DPLL(temp)
             
for line in ipFile:
	if not line[0] == "c":
		clauseSet.append(map(int,line.split()))
print clauseSet
done = DPLL(clauseSet)
if done:
	for set in solved:
		print set, solved[set]
else:
	print "UNSATISFIABLE"

                    
