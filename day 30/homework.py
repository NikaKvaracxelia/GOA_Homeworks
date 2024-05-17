def modify_string(input_string):
    reversed_string = ''.join(reversed(input_string))
    uppercased_string = reversed_string.upper()
    return uppercased_string

test_case = "Nika Kvaracxelia"
result = modify_string(test_case)
print(result) 



def classify_strings(string_list):
    odd = []
    even = []
    for string in string_list:
        if len(string) % 2 == 0:  # ლუწი ან კენტის დადგენა
            even.append(string.upper())  # ლუწი სიისთვის დამატება
        else:
            odd.append(string.upper())  # კენტი სიისთვის დამატება

    return odd, even

test_case = ["nika", "davit", "zuka", "giorg"]

odd, even = classify_strings(test_case)

print("odd =", odd)
print("even =", even)



def process_strings(string_list):
    new_list = []
    for string in string_list:
        if len(string) % 2 == 0:  # ლუწი ან კენტის დადგენვა
            new_string = string.upper()
        else:
            new_string = string.capitalize()
        new_list.append(new_string)

    return new_list

test_case = ["goa_best", "nika", "nesvi", "ShOnIa"]
result = process_strings(test_case)
print(result)



def process_strings(string_list):
    result_list = []
    for string in string_list:
        if string.isupper(): 
            result_list.append(string.lower())  
            result_list.append(string.upper()) 

    return result_list

test_case = ["vano", "DAVIT", "LUKA", "nika"]
result_list = process_strings(test_case)
print(result_list)



def process_string(input_string):
    index = input_string.find("n") 
    if index % 2 == 0: 
        return input_string.upper()  
    else:
        return input_string.capitalize() 

test_case = "nika kvaracxelia"
result_1 = process_string(test_case)
print(result_1) 

test_case = "kvaracxelia nika"
result_2 = process_string(test_case)

