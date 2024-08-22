import math
def function_1(shape, *args):
    print('Function 1')
    if shape=='circle':
        element=args[0]
        area=math.pi*float(element**2)

    else:
        area=args[0]*args[1]

    return area

print('The area :',function_1('circle',3))
print('The area :',function_1('rectangle',3,4))
 