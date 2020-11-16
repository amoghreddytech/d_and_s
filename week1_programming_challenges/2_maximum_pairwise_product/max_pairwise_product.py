# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def get_max(numbers,index_list = [None]):
    #returns max_number and index
    #index_list holds numbers to skip
    max  = -1
    ind = -1
    for index,value in enumerate(numbers):
        if index not in index_list:
            if value > max:
                max = value
                ind = index

    if max == -1:
        return ("numbers has no non negative elements")

    return (max,ind)






def max_pairwise_product_optimized(numbers):
    number_one,index = get_max(numbers)
    number_two,_ = get_max(numbers,[index])
    return (number_one * number_two)





if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product_optimized(input_numbers))
    print(357%234)
    print(234%123)
    print(123 % 111)
    print(111 % 12)
    print(12 % 3)
