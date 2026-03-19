def get_user_info(data:list, user_id:int):
    for i in data:
        if user_id == i['id']:
            return i
    return {"error":"User not found"}