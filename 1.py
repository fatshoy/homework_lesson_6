def concat (*args, reversed=False):
    if reversed == True:
        returned_args = []
        returned_args = args[::-1]
        for arg in returned_args:
            print(arg,end='')
    else:
        for arg in args:
            print(arg,end='')

concat('good', 'bye', 'my', 'love', reversed=True)