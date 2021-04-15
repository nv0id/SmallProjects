import random as rand

def random_numbers(n,size):
    unsorted = [rand.randrange(1,n,1) for i in range(1,size)]
    return unsorted

def sort(array,method):
    print("Unsorted list: ",array)
    if method=="bubble":
        not_swapped=False
        while not_swapped==False:
            not_swapped=True
            for index in range(0,len(array)-1,1):
                if array[index] > array[index+1]:
                    get = array[index], array[index+1]
                    array[index+1],array[index] = get
                    not_swapped=False
        return array
    else:
        return "no or incorrect method specified"

print(sort(random_numbers(10,5),"bubble"))
