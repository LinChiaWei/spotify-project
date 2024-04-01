import datetime

def sort_data(list):
    return list[3]

def update_data(db_data,new_data):
    data_list = list(map(list,db_data))
    for i in new_data:
        if any(i[0] in (match := nested) for nested in data_list):
            match[2] = match[2]+i[2]
        else:
            data_list.append(i)

    data_list.sort(key=sort_data,reverse=True)
    return data_list

def check_duplicate(db_data,new_data):
    result = []
    flag = False
    
    for i in new_data:
        for j in db_data:
            print(i[3],str(j[4]))
            if i[3] == str(j[4]):
                flag = True
                break
        if flag == False:
            result.append(i)
    if(len(result) > 0):
        print("No data to update")
    return result

