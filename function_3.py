def apply_operation(lst,operation):
    res=[]
    for i in lst:
        res.append(operation(i))
    return res

print(apply_operation([1,2,3],lambda x: x**2))