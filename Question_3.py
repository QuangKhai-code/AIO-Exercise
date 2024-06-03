import math
import random
# Viết function lựa chọn regression loss function để tính loss:
def MAE(predict, target):
    result = 0
    for each_target, each_predict in zip(predict, target):
        result += abs(each_target - each_predict)
    return result / len(predict)

def MSE(predict, target):
    result = 0
    for each_target, each_predict in zip(predict, target):
        result += (each_target - each_predict) ** 2
    return result / len(predict)

def RMSE(predict, target):
    return math.sqrt(MSE(predict, target))

def exercise3():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)
    loss_name = input("Input loss name (MAE, MSE, RMSE): ")
    
    predict_list = []
    target_list = []
    for _ in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predict_list.append(predict)
        target_list.append(target)
        
    loss_each_sample = []
    if loss_name == "MAE":
        loss_each_sample = [abs(target_list[i] - predict_list[i]) for i in range(num_samples)]
        final_loss = MAE(predict_list, target_list)
    elif loss_name == "MSE":
        loss_each_sample = [(target_list[i] - predict_list[i]) ** 2 for i in range(num_samples)]
        final_loss = MSE(predict_list, target_list)
    elif loss_name == "RMSE":
        loss_each_sample = [(target_list[i] - predict_list[i]) ** 2 for i in range(num_samples)]
        final_loss = RMSE(predict_list, target_list)
    else:
        print("Invalid loss name")
        return

    for i in range(num_samples):
        print(f"loss name: {loss_name}, sample {i}, pred {predict_list[i]:.6f}, target {target_list[i]:.6f}, loss {loss_each_sample[i]:.6f}")

    print(f"final {loss_name} : {final_loss:.6f}")

if __name__=="__main__":
    exercise3()