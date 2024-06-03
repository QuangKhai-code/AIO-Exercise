def md_nre_single_sample(y, y_hat, n, p):
    root_y = y ** (1/n)
    root_y_hat = y_hat ** (1/n)
    difference = (root_y - root_y_hat)
    result = difference ** p
    return result

if __name__=="__main__":
    print(md_nre_single_sample ( y =100 , y_hat =99.5 , n =2 , p =1))
    print(md_nre_single_sample ( y =50 , y_hat =49.5 , n =2 , p =1))
    print(md_nre_single_sample ( y =20 , y_hat =19.5 , n =2 , p =1))
    print(md_nre_single_sample ( y =0.6 , y_hat =0.1 , n =2 , p =1))
    