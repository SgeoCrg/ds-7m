import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Python:', sys.version)
print('NumPy:', np.__version__)
print('Pandas:', pd.__version__)

df = pd.DataFrame({
    'producto':['A','B','C'],
    'precio':[10.0,20.0,15.0],
    'unidades':[2,1,3]
})

df['total'] = df['precio'] * df['unidades']
df

df.plot(kind='bar', x='producto', y='total')
plt.title('Total por producto')
plt.show()