def userEntity(item)->dict:
    return {
        "id" : str( item["_id"]),
        "name" : item["name"],
        "isactive" : item["isactive"],
        "age" : item["age"],
        }

def UsersEntity(entity)->list:
    return [userEntity(item) for item in entity]