def binary_search(input_array, value):
    low   = 0
    high  = len(input_array)-1

    index = -1

    while(low <= high):
        middle = int( (high + low) / 2 )
        if (input_array[middle] == value):
            index = middle
            break
        elif (input_array[middle] < value):
            low = middle + 1
        else:
            high = middle - 1

    return index

test_list = [1,3,9,11,15,19,29]

test_val1 = 25
test_val2 = 15

print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))