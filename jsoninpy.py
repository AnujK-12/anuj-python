import json
x='{"name":"John","age":"30","city":"New York"}'

print(type(x))
y=json.loads(x)

print(type(y))
print(x)
print(y)

# z=json.dump(y)
# print(type(z))