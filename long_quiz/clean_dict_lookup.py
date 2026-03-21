def get_user_info(data:list, user_id:int):return [i if user_id == i['id'] else {"error":"User not found"} for i in data][0]

users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]
print(get_user_info(users, 1) )