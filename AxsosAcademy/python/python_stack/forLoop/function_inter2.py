
# 1. Update Values

x = [[5, 2, 3], [10, 8, 9]]
students = [{‘first_name’: ‘Michael’, ‘last_name’: ‘Jordan’},{‘first_name’: ‘John’, ‘last_name’: ‘Rosales’}]
sports_directory = {‘basketball’: [‘Kobe’, ‘Jordan’, ‘James’, ‘Curry’],‘soccer’: [‘Messi’, ‘Ronaldo’, ‘Rooney’]}
z = [{‘x’: 10, ‘y’: 20}]

x[1][0] = 15                                    # 1. Change 10 to 15
students[0][‘last_name’] = ‘Bryant’             # 2. Jordan → Bryant
sports_directory[‘soccer’][0] = ‘Andres’        # 3. Messi → Andres
z[0][‘y’] = 30                                  # 4. Change 20 to 30

print(x)
print(students)
print(sports_directory)
print(z)

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for dictionary in some_list:    
    for key, value in dictionary.items():
print(f”{key} - {value}”)

students2 = [
{‘first_name’: ‘Michael’, ‘last_name’: ‘Jordan’},
{‘first_name’: ‘John’, ‘last_name’: ‘Rosales’},
{‘first_name’: ‘Mark’, ‘last_name’: ‘Guillen’},
{‘first_name’: ‘KB’, ‘last_name’: ‘Tonel’}
]
iterateDictionary(students2)

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
print(dictionary[key_name])

iterateDictionary2(‘first_name’, students2)
iterateDictionary2(‘last_name’, students2)

# 4. Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key, value in some_dict.items():
print(f”{len(value)} {key.upper()}”)
    for item in value:
print(item)

dojo = {
‘locations’: [‘San Jose’, ‘Seattle’, ‘Dallas’, ‘Chicago’, ‘Tulsa’, ‘DC’, ‘Burbank’],
‘instructors’: [‘Michael’, ‘Amy’, ‘Eduardo’, ‘Josh’, ‘Graham’, ‘Patrick’, ‘Minh’, ‘Devon’]
}
    
printInfo(dojo)