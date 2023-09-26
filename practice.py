'''
def remove_duplicate(union):

    final_list=[]
    for element in union:
        if element not in final_list : final_list.append(element)
    return final_list

# OR ....
    for element in union:
        if union.count(element) > 1 : union.remove(element)
    return union



def combine_list(list1,list2):
    union = []
    for list1_element in list1:
        union.append(list1_element)

    for list2_element in list2:
        union.append(list2_element)
    return remove_duplicate(union)


list1=["john","don","bon","kon","ron","hon"]
list2=["kon","ton","mon","john","fon"]

print("{list} this list is the union of list1 and list2.".format(list=combine_list(list1,list2)))
'''
'''


def is_divisible(list,result):
    i=0
    count=0
    while i< len(list):
        if result%list[i] ==0 : count+=1
        i+=1
    if count == len(list):
        return True
    else:
        return False



def multiple(list,multiplication):
    permenant_list=list
    result=multiplication/list[0]
    get_result=is_divisible(permenant_list,result)
    if get_result == True:
        list.remove(list[0])
        multiple(list,result)
    else:
        final_result=(result*list[0])/2
        print("the LCM for {} is {}.".format(permenant_list,final_result))



list=[]
i=0
total_input=int(input("How many number do you want to input:"))
print("Enter your numbers:\n")
while i< total_input:
    get_number=int(input())
    list.append(get_number)
    i+=1
multiplication=1
for i in range(len(list)):
    multiplication=multiplication*list[i]
#print("multiplication:{}".format(multiplication))
multiple(list,multiplication)
'''
'''Complete the body of the format_name function. 
This function receives the first_name and last_name parameters and then returns a properly formatted string.
Specifically:
'''
''' 
Use a dictionary to count the frequency of letters in the input string. Only letters 
should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. 
For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
'''

























