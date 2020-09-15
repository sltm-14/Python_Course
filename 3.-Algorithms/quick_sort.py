def quicksort(array):

    toComp = 0

    if (len(array) > 1):
        pivot = len(array)-1
    else:
        return array

    if(len(array) <= 2 ):
        if (   array[toComp] > array[pivot]) :
            aux            = array[toComp]
            array[toComp]  = array[pivot-1]
            array[pivot-1] = array[pivot]
            array[pivot]   = aux

            pivot = pivot -1
        else:
            toComp += 1
        return array

    else:

        while(toComp < (pivot)):
            if (array[toComp] > array[pivot]   ) :
                aux            = array[toComp]
                array[toComp]  = array[pivot-1]
                array[pivot-1] = array[pivot]
                array[pivot]   = aux

                pivot = pivot -1
            else:
                toComp += 1
        return quicksort(array[0:pivot]) + [array[pivot]] + quicksort(array[pivot+1:len(array)])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print (quicksort(test))
