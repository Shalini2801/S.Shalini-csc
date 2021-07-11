import json
a ={"name":"John","age":21,"Salary":27000}
b = json.dumps(a)
print(b)

import json
 # list conversion to Array
print(json.dumps(['Hi,', "Hello!","Learners"]))
print(json.dumps(("Hi,", "Hello!", "I'm John")))
print(json.dumps("Hi"))
print(json.dumps(123))
 # float conversion to Number
print(json.dumps(23.572))
 # Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))
 
# None value to null
print(json.dumps(None))