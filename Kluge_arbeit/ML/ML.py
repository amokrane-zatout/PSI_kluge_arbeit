# Load libraries


import pandas

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
print('chargement des donnees .... ')
url = "profit.csv"
dataset = pandas.read_csv(url)
print('chargement termine')

# shape
print('***')
print('****** structure de donnees ')
print(dataset.shape)

# head
print('***')
print('*********  les 10 premier ligne')
print(dataset.head(10))

# descriptions
# print('***')
# print('********* description')
# print(dataset.describe())


# class distribution
print('***')
print('********* disribution')
print(dataset.groupby('classe').size())

# histograms
# dataset.hist()
# plt.show()


print('**************')
print('*******')
print('********  Devision de donnees  80% de donnees d apprentissage et 20% donnees de validation ')
print('*** X_train,Y_train  /  Y_train,X_train')
# Split-out validation dataset
array = dataset.values
X = array[:, 0:7]
Y = array[:, 7]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)
X_test = X_validation[1:2]

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

print('***************')
print('********')
print('*** execution et comparaison des 5 algorithmes ')
print('********')

# Spot Check Algorithms
models = []
models.append(('Regression logistique', LogisticRegression()))
models.append(('Analyse discriminante lineaire', LinearDiscriminantAnalysis()))
models.append(('K-Plus proches voisins', KNeighborsClassifier()))
models.append(('Gaussian Naive Bayes', GaussianNB()))
models.append(('Machines a vecteurs de suppor', SVC()))
# evaluate each model in turn
results = []
names = []

for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f " % (name, cv_results.mean())
    print(msg)

print('***')
print('*** Choix de K plus proche voisin ')
print('*** prediction sur les donnees de validation ')

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
pred = knn.predict(X_test)

print(X_validation)

print(X_test)

print(predictions)
print('prediction de profit ')
print(pred)

print('La precision : ')
print(accuracy_score(Y_validation, predictions))

print('Matrice de confusion : ')
print(confusion_matrix(Y_validation, predictions))

