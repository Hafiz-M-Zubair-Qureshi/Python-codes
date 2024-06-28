# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106



def compute_series(a):
    n_str = str(a)
    m1 = int(n_str)
    m2 = int(n_str * 2)
    m3 = int(n_str * 3)
    m4 = int(n_str * 4)
    result = m1 + m2 + m3 + m4
    return result


a = int(input("Enter a digit: "))
print(compute_series(a))
