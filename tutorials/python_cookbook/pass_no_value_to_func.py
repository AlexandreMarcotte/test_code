_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value
        print('No b value supplied')

spam(1)
# spam(1, None)
