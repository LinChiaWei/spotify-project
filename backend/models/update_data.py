def take_second(list):
    return list[2]

def update_data(db_data,new_data):
    data_list = list(map(list,db_data))
    for i in new_data:
        if any(i[0] in (match := nested) for nested in data_list):
            match[2] = match[2]+i[2]
        else:
            data_list.append(i)

    data_list.sort(key=take_second,reverse=True)
    return data_list

