def take_second(list):
    return list[2]

def update_data(db_data,new_data):
    data_list = list(db_data)
    # print(type(db_data))
    for i in new_data:
        # print(type(i))
        if any(i[0] in (match := nested) for nested in data_list):
            # print((match[2]))
            # print(type(i[2]))
            # print(match[2])
            # print(i[2])
            match[2] = match[2]+i[2]
            # print(ans)
        else:
            data_list.append(i)

    data_list.sort(key=take_second,reverse=True)
    return data_list

