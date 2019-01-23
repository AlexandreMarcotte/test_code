import io
import sys

# somewhere to store output
out = io.StringIO()

# set stdout to our StringIO instance
sys.stdout = out

# print something (nothing will print)
print('herp derp')

# restore stdout so we can really print (__stdout__ stores the original stdout)
sys.stdout = sys.__stdout__

# print the stored value from previous print
print(out.getvalue())