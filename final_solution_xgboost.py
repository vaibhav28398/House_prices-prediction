from xgboost import XGBRegressor
import pandas as pd
import csv
import xgboost
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
data_train=pd.read_csv('train.csv')
data_test=pd.read_csv('test.csv')
features_train=data_train.drop('price',axis='columns')
features_test=data_test.drop('price',axis='columns')
labels_train=data_train['price']
data=pd.read_csv('solution.csv')
labels_test=data['Golden Grains']
model1=XGBRegressor()
model1.fit(features_train,labels_train)
print "Seeing the cross validation score to avoid overfitting"
scores=cross_val_score(model1,features_train,labels_train,cv=5,scoring='r2')
print scores.mean()
print "Applying xgboost without tuning parameters"
print "Feature importances"
print model1.feature_importances_
xgboost.plot_importance(model1)
plt.show()
print "score"
from sklearn.metrics import r2_score
pred=model1.predict(features_test)
print r2_score(pred,labels_test)
print "Tuning parameters"
model=XGBRegressor(max_depth=3,n_estimators=350,learning_rate=0.1)
model.fit(features_train,labels_train)
xgboost.plot_importance(model)
plt.show()
pred=model.predict(features_test)
print "score"
print r2_score(pred,labels_test)
print "feature importances"
print model.feature_importances_
print "Seeing the importances of features like kingvisit blessing and renovation are very less so dropping these"
model=XGBRegressor(max_depth=3,n_estimators=350,learning_rate=0.1)
features_train2=features_train.drop(['kingvisit','blessing','renovation'],axis='columns')
features_test2=features_test.drop(['kingvisit','blessing','renovation'],axis='columns')
model.fit(features_train2,labels_train)
pred=model.predict(features_test2)
print "score after dropping the above features"
print r2_score(pred,labels_test)
