def digital_root(n):
    # ASSUMPTIONS: n is non-negative
    # integers?
    
    # Split into seperate number
    str_num = str(n)
    num_list = [int(num) for num in str_num]
    return sum(num_list)
    
print(digital_root(12))
