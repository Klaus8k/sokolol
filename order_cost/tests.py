# Create your tests here.


def dec_x2(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)

        return result
    return wrap

    
# def dec_x2(x):
#     return x * 2

@dec_x2
def summm(a,b):
    return a+b


# @dec_x2
# def summm(a,b):
#     return a+b

if '__main__' == __name__:
    print(summm(3,2))
    # print(dec_x2(summm(3,2)))
