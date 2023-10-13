#write a program to merge two dictionaries using copy and update functions

dict_1={1:"aa",2:"bb",3:"cc"}
dict_2 ={"a":11,"b":22,"c":33}
dict_3=dict_1.copy()
dict_3.update(dict_2)
print(dict_3)
