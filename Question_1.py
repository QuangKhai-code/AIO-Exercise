#Viết function thực hiện đánh giá classification model bằng F1-Score.
def exercise1(tp, fp, fn):
    # Kiểm tra đầu vào phải là int
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return
    if  tp <= 0 or fp <= 0 or fn <=0:
        print("tp and fp and fn must be greater than zero")
        return
    precision = tp / (tp+fp)
    recall = tp / (tp+fn)
    f1_score= 2* (precision*recall)/ (precision+recall)
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")
    return

if __name__ == "__main__":
    exercise1 ( tp =2 , fp =3 , fn =4)
    exercise1 ( tp ='a', fp =3 , fn =4)
    exercise1 ( tp =2 , fp ='a', fn =4)
    exercise1 ( tp =2 , fp =3 , fn ='a')
    exercise1 ( tp =2 , fp =3 , fn =0)
    exercise1 ( tp =2.1 , fp =3 , fn =0)