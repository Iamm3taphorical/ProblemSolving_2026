t_var = int(input())
i_var = 0
while i_var < t_var:
    n_var = int(input())
    if n_var % 2 == 0:
        print(str(n_var) + " is an Even number.")
    else:
        print(str(n_var) + " is an Odd number.")
    i_var = i_var + 1