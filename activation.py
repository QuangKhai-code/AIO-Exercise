#2. Viết function mô phỏng theo 3 activation function.
import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
def excercise2():
    x = input("Input x: ")
    if is_number(x) == False:
        print("x must be a number")
        return
    activation_name = input("Input activation Function ( sigmoid | relu | elu ) : ")
    if activation_name not in ["sigmoid","relu","elu"]:
        print(f"{activation_name} is not supported")
        return

    x=float(x)
    if activation_name == "sigmoid":
        value = 1 / (1+math.exp(-x))
        print(f"{activation_name} : f({x}) = {value}")
        return
    if activation_name == "relu":
        value = max (0,x)
        print(f"{activation_name} : f({x}) = {value}")
        return
    if activation_name == "elu":
        value=0
        if x>0:
            value=x
        else:
            value = math.exp(x)-1
        print(f"{activation_name} : f({x}) = {value}")
        return

if __name__=="__main__":
    excercise2()
    