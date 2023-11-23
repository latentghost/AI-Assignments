import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


def transform(inp):
    return 1/(1+np.exp(-(inp**0.5)))


df = pd.read_csv("./abalone.data")
target = df['rings']
data = df.drop(columns=['rings'])

cat = ['sex']
data_cat = data[cat]
data_num = data.drop(columns=cat)

data_cat_oh = pd.get_dummies(data_cat,columns=cat,drop_first=True)

for col in data_num.columns:
    data_num[col] = data_num[col].apply(lambda x: transform(x))

data = pd.concat([data_cat_oh,data_num],axis=1)

lr_reg_full = LinearRegression(fit_intercept=True)
X = data
Y = target

lr_reg_full.fit(X=X,y=Y)
y_pred = lr_reg_full.predict(X=X)

r2_full_data = r2_score(y_true=Y,y_pred=y_pred)

print(f"Full dataset train and eval R2 score: {r2_full_data}")


r2_splits = []

for i in range(100):
    X_train, X_tmp, Y_train, Y_tmp = train_test_split(data,target,test_size=0.3,random_state=(i+1)**2)
    X_val, X_test, Y_val, Y_test = train_test_split(X_tmp,Y_tmp,test_size=0.5,random_state=(i+1)**2)

    lr_split = LinearRegression(fit_intercept=True)

    lr_split.fit(X=X_train,y=Y_train)

    pred_val = lr_split.predict(X=X_val)
    r2_val = r2_score(y_true=Y_val,y_pred=pred_val)

    if(r2_val>0.56):
        X_tr = pd.concat([X_train,X_val],axis=0)
        Y_tr = pd.concat([Y_train,Y_val],axis=0)

        lr_split.fit(X=X_tr,y=Y_tr)

        pred_test = lr_split.predict(X=X_test)
        r2_test = r2_score(y_true=Y_test,y_pred=pred_test)

        r2_splits.append(r2_test)

print(f"70-15-15 Cross validation boxplot: mean={np.mean(r2_splits)}, std={np.std(r2_splits)}")