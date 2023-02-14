def take_second(list):
    return list[2]

def update_data(db_data,new_data):
    for i in new_data:
        if any(i[0] in (match := nested) for nested in db_data):
            match[2] = str(match[2]+i[2])
        else:
            db_data.append(i)

    db_data.sort(key=take_second,reverse=True)

