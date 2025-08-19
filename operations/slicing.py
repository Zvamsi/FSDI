a='hello world'
data=[1,2,3,4,5]

NOTE : 'The slicing only works on collection but not on single value datatype...'

#   1.WITH ALL THREE VALUES
print(a[3:5:1])  #lo
print(data[5:6])  #[]
print(data[0::-1])

#   2.WITH NO VALUES
print(a[:])  #hello world
print(a[::-1]) #dlrow olleh

#   3.WITH ONLY POSITIVE STEP
print(a[::3]) #hlwl

#   4.WITH ONLY NEGATIVE STEP
print(a[::-2]) #drwolh
print(a[::-5]) #Takes the first element first and next 5th element and so on..."d h"


#   5.WITH ONLY STARTING INDEX
print(a[4:]) #o world
print(a[5:0]) #EMPTY


#   6.WITH ONLY END INDEX
print(a[:5:]) #hello
print(a[:5:-1]) #dlrow

# QUESTION : 1
company = {
'about': {
'details': (
"NextGenCorp",
{"HQ": "Bangalore", "founded": 2005},
["TechDivision", "AI-Lab"]
),
'industry': {"main": "Software", "sub": {"type": "AI"}}
},
'employees': {
'e1': ["Ramesh", 32, {"city": "Mysore", "dept": "AI"}],
'e2': ("Divya", 29, {"city": "Hyderabad", "skills": {"Python", "ML"}}),
'e3': ["Kiran", 28, {"city": "Chennai"}]
},
'partners': {("IBM", "Cloud"), ("Amazon", "AWS")}
}

ONE=company