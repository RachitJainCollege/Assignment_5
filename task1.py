str=input("Enter the name of the student: ")
dict={'Ram':'10','Ravi':'20','Raj':'30','Alice':'40','Lucky':'50','Prerna':'60','Sam':'70','King':'80','Big':'90','Rach':'100'}
if str in dict:
    print("{}'s marks: ".format(str),dict[str])
else:
    print("Student not found")