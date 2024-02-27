# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def MyFunction(arg1,arg2,*,my_required_keyword=False):
    pass


# try to call the function without the keyword
# myFunction(1, 2, True)
def MyFunction2(arg1,arg2,my_required_keyword=False):
    pass
# Too many positional arguments error because after * must be a keyword arg
MyFunction(1,2,False)
# MyFuntion2 works as no keyword arguments are mandatory
MyFunction2(1,2,False)


