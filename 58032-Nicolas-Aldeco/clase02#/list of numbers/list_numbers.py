def find_max(list_of_numbers):

    if not isinstance(list_of_numbers, list):
       raise Exception('not a number')

    if not list_of_numbers :
        return None
    max = 0
    i = 0
    for i in range(len(list_of_numbers)):

        if list_of_numbers[i] > max:
            max = list_of_numbers [i]
        

    return max