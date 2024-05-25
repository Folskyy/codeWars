def sum_of_intervals(intervals): 
    def sum_of_interval(interval):
        sum = 0
        for i in range(interval[0], interval[1]):
            sum += 1
        return sum
    
    sum = 0

    for element in intervals:
        sum += sum_of_interval(element)

    return sum


elements = [[[1, 2],
            [6, 10],
            [11, 15]],
            [[1, 4],
            [7, 10],
            [3, 5]],
            [[1, 5],
            [10, 20],
            [1, 6],
            [16, 19],
            [5, 11]],
            [[0, 20],
            [-100000000, 10],
            [30, 40]]]




for element in elements:
    print(sum_of_intervals(element))