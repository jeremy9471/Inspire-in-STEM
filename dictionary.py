CC


# Initializing dictionaries
# key value pairs(the keys and values are in quotations and separated by commas, 'key':'value')
colors = {'color':'red'}
vehicle = {'type':'toyota','plateNumber':'KCB17C'}
# dictionary of a person
person = {
    'name':'Jeremy',
    'address':'langata',
    'number':'0799365556',
    'gender':'male',
    'age':'18'}
#print(colors)
# print(type(colors)) used to read class of a string,dictionary,list etc

# accessing values in dictionaries using the key
print(vehicle['plateNumber'],vehicle['type'])
print(type(person))
print(person)
person['favColor']='green'
print(person['favColor'],person['name'],person['age'])
del(person['number'])
print(person)

# looping over dictionaries(for loop)
#for key, value in person.items():
 #   print(f"{key}:{value}")

# using get method to access values in a dictionary
print(person.get('gender'))
print(person.get('password',"The \'password\' is non existent"))

