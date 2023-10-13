#wrie a program to concatenate the dictionaries to create a new one

dict_1={1:"aa",2:"bb",3:"cc"}
dict_2 ={"a":11,"b":22,"c":33}
dict_3 = {"w":"ee","e":"cc"}
dict_4 = {}
for d in (dict_1,dict_2,dict_3):
    dict_4.update(d)
print(dict_4)
