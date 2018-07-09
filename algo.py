import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import csv
from sklearn import metrics
from sklearn.model_selection import cross_val_score
#reading in pandas
data_train=pd.read_csv('train.csv')
data_test=pd.read_csv('test.csv')
#splitting in features and labels
features_train=data_train.drop(['price','id1'],axis='columns')
features_test=data_test.drop(['price','id1'],axis='columns')
labels_train=data_train['price']
data=pd.read_csv('solution.csv')
labels_test=data['Golden Grains']
#Applying interpolation to fill nan values	
features_train.interpolate(method='akima',inplace=True)
features_test.interpolate(method='akima',inplace=True)
features_train['bathroom'][0]=2
features_train['bathroom'][1]=2
features_test['location'][0]=1
features_test['renovation'][0]=1
#Applying Pca
from sklearn.decomposition import PCA
pca=PCA(n_components=5)
pca.fit(features_train)
features_train_pca=pca.transform(features_train)
features_test_pca=pca.transform(features_test)
#Applying Linear regression model with pca
from sklearn import linear_model
print "Linear Regression"
reg1=linear_model.LinearRegression()
reg1.fit(features_train_pca,labels_train)
print "Cross_validation score"
scores=cross_val_score(reg1,features_train_pca,labels_train,cv=5,scoring='r2')
print scores.mean()
print "LinearRegression With pca"
print reg1.score(features_test_pca,labels_test)
#Applying LinearRegression model without pca
reg=linear_model.LinearRegression()
print "LinearRegression without pca"
reg.fit(features_train,labels_train)
print "Cross_validation score"
scores=cross_val_score(reg1,features_train,labels_train,cv=5,scoring='r2')
print scores.mean()
print "LinearRegression without pca"
print reg.score(features_test,labels_test)
# So we got to realise that pca is'nt giving good results
print "Pca result wasn't good"
#Applying Ridge regression
print "Ridge Regression"
reg1 = linear_model.Ridge (alpha = 0.5,max_iter=100,tol=0.00001,random_state=42)
reg1.fit(features_train,labels_train)
print "Cross_validation score"
scores=cross_val_score(reg1,features_train,labels_train,cv=5,scoring='r2')
print scores.mean()
print "Ridge regressions score"
print reg1.score(features_test,labels_test)
#Applying Lasso regression
from sklearn.linear_model import LassoCV
reg2=LassoCV(max_iter=1500,precompute=True,alphas=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10],selection='random',normalize=True)
reg2.fit(features_train,labels_train)
pred2=reg2.predict(features_test)
print "Lasso Regression"
print "Cross_validation score"
scores=cross_val_score(reg1,features_train,labels_train,cv=5,scoring='r2')
print scores.mean()
print "Lasso Regression score"
print reg2.score(features_train,labels_train)