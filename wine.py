import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
data = load_wine()
data

from sklearn.model_selection import train_test_split
x = pd.DataFrame(data.data,columns=data.feature_names)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state=42)

x.shape

from sklearn.linear_model import LogisticRegression
mlog_reg = LogisticRegression()
mlog_reg.fit(X_train,y_train)

test_prediction = mlog_reg.predict(X_test)
test_prediction

from sklearn.metrics import confusion_matrix
c=confusion_matrix(y_test,test_prediction)
c

data.keys()

data = pd.DataFrame(data=np.c_[data['data'],data['target']],
           columns=data['feature_names']+['target'])

data

data.groupby('target').mean()

from scipy import stats
class1= data[data.target==0]
class2= data[data.target==1]
stats.ttest_ind(class1,class2)
print(stats.ttest_ind(class1,class2).pvalue)



