employee = {
    "name" : "zoro",
    "id" : 201,
    "join_date" : 18

}


# adding a new key-value pair
employee["age"] = 24
print(employee)

#updating an existing value
employee["id"] = 12
print(employee)

#using update() method
employee.update({"salary" : 30000})
print(employee)