# def hello():
#     return 'Hi Jose'

# def other(func):
#     print('Hello')
#     print(func())

# other(hello)

def new_decorator(func):
    
    def wrap_func():
        print('Code Here before executing the func')
        func()
        print('func() has been called before')
    
    return wrap_func

@new_decorator
def func_needs_decorator():
    print('This function is in need of decorator')

# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

