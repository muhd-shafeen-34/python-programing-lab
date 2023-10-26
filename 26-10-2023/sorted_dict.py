#sort a dictionary in accending and descending order

import operator
dict = {1:2,2:3,3:4}
print("orginal dict ",dict)
sorted_dict = sorted(dict.items(),key = operator.itemgetter(1))
print("ascending order is ",sorted_dict)
sort_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order is : ",sort_dict)
