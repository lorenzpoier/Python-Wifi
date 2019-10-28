'''



'''
h = { 4: 7,
      5: 2,
      2: 8,
      6: 1, 
      12: 2,
    }
#Iteration über Keys beim Dictionary
for k in h:
    print(k, h[k])
    
print('#######')    
    
for k,v in h.items():
    print(k, v)
    
print('#######')    
    
h_keys = list(h.keys())
h_keys.sort()
for k in h_keys:
    print(k, h[k])
    
print('####### nach Häufigkeit sortieren ###########')    
    
h_rev = {}
for k,v  in h.items():
    h_rev[v] = k  
h_rev_keys = list(h_rev.keys())
h_rev_keys.sort()
for k in h_rev_keys: 
    print(k, h_rev[k])
    
print('####### OrderedDict ###########')      
from collections import OrderedDict

h_sorted_by_val = OrderedDict(sorted(h.items(), key = lambda x: x[1]))
for k,v in h_sorted_by_val.items():
    print(k,v)
    
print('####### nach Häufigkeit manuell ###########')      

h_as_list = []
for k,v in h.items():
    h_as_list.append([v,k])
    h_as_list.sort()
print(h_as_list)

