import pandas as pd
import numpy as np

a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})
print(a)


b = a.set_index(['c','d'])['a']


# c = a.set_index(['d','c'])['a']
# print(c)
# print(c.swaplevel()['one'])

print(b)
print(b.loc['one'].loc['h'])
