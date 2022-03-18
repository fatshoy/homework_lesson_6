from functools import wraps

def inspect(func):

    @wraps(func)
    def wrap (*args, **kwargs):
        print('Args: ', args)
        print('Kwargs: ', kwargs)
        print('Retvalue: ',end=''); func (*args, **kwargs)
        func (*args, **kwargs)

    return wrap

@inspect
def concat (*args, reversed=False):
    result = str()
    if reversed == True:
        returned_args = []
        returned_args = args[::-1]
        for arg in returned_args:
            result += arg
        print(result)
    else:
        for arg in args:
            result += arg
        print(result)

concat('good', ' ', 'bye', ' ', 'my', ' ', 'love', reversed=True)