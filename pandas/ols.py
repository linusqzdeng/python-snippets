import statsmodels.formula.api as sm
import pandas as pd

df = pd.DataFrame({'A': [0.05, 0.07, 0.09, 0.04, 0.03, 0.08], 
            'B': [0.021, 0.03, 0.09, 0.05, 0.07, 0.04], 'C': [1, 2, 3, 4, 5, 6]})

res = sm.ols(formula='A ~ B + C', data=df).fit()
print(res.summary)