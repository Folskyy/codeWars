def same_structure_as(original, other):
    def count(arr):
        aux = ''
        dim = 1
        res = {1: 0}
        for i in str(arr):
            if i == '[':
                res[dim] += 1

            if i == '[' and aux and aux[-1] == '[':
                dim += 1
                res[dim] = 0
            
            if i == ']':
                aux.pop()
                dim -= 1
            
                print(res)
            return res

    if count(original) == count(other):
        return True
    return False

print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]))
