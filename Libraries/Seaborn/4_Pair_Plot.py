import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

np.random.seed(42)

df = pd.DataFrame({
    'marks':       np.random.randint(40,100,100),
    'study_hours': np.random.uniform(2,10,100),
    'city':        np.random.choice(['Jakarta', 'Qualalampur', 'Quwait'],100),
    'gender':      np.random.choice(['Male','Female'],100)
})


#  Pair Plot - all relationship at once
sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
plt.show()