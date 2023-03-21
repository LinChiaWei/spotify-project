import datetime

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

def check_duplicate(db_data,new_data):
    result = []

    for i in new_data:
        flag = False
        for j in db_data:
            if i[2] == str(j[2]):
                flag = True
                break
        if flag == False:
            result.append(i)

    # for i in db_data:
        # print(i[2])
    return result

