# Example 021: Python modules

import addition
import math as math_library

result = addition.add(3, 4, 5)
print(result)

print('Number pi: {}'.format(math_library.pi))
print('Definitions inside addition module: {}'.format(dir(addition)))
