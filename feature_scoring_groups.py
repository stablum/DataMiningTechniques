
def get_group(number_of_features, group_nr, iteration):
    ret = []
    divisor = 2**iteration
    print("divisor", divisor)
    for i in range(0,(number_of_features)):
        tmp = int(i/divisor)
        #print("tmp",tmp)
        #print("tmp%2",tmp%2)
        if tmp % 2 == group_nr:
            ret.append(i)
    return ret

