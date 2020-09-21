#decorators is the function where we can alter the other non-accssable/accessable function code and update according to desire  form.
def division(a,b):
    return a/b

def DecoratorsFun(num): #function inside function

    def inner_div(a,b): #customize function where numerator should be always grater than denominator
        if a<b:
            a,b=b,a #swap
        return num(a,b)
    return inner_div

newDivison = DecoratorsFun(division)
print(newDivison(5,10))
