#SCIKIT-LEARN CHEATSHEET


#Import the library
from sklearn import *

#Training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

#Fit the model to the data
###Supervised Learning###
lr.fit(X, y)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)

###Unsupervised Learning####
k_means.fit(X_train)
pca_model = pca.fit_transform(X_train)

#Make predictions with the data
###Supervised Estimators###
y_prediction = svc.predict(np.random.random((2,5)))
y_prediction = lr.predict(X_test)
y_prediction = knn.predict_proba(X_test)

###Unsupervised Estimators####
y_prediction = k_means.predict(X_test)

#Doing standarization to data
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

#Doing normalization to data
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

#Doing binarization to data
binarizer = Binarizer(threshold = 0.0).fit(X)
binary_X = binarizer.transform(X)

#Calculating the mean absolute error (mae)
y_true = []
mean_absolute_error(y_true, y_prediction)

#Calculating the adjusted rand index
adjusted_rand_score(y_true, y_prediction)

#Calculating the homogeneity
homogeneity_score(y_true, y_prediction)

#Calculating the V-measure
metric.v_measure_score(y_true, y_prediction)

#Do the cross-validation of your model
print(cross_val_score(knn, X_train, y_train, cv=4),'\n')
print(cross_val_score(lr, X, y, cv=2))
