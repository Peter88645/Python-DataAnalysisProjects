import pandas as pd
import numpy as np

d1 = pd.DataFrame( np.arange(12).reshape(3,4),index=list('abc'),columns=list('WXYZ'))

d2 = pd.DataFrame(np.zeros((2,3)), index=list('ab'),columns=list('ABC'))

print( d1.join(d2) )

print(d2.join(d1))