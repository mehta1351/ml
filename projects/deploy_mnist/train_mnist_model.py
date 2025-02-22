#from sklearn.datasets import fetch_mldata
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import joblib

np.random.seed(42)
#mnist = fetch_mldata("MNIST original")
mnist = fetch_openml('mnist_784', version=1, cache=True)
mnist.target = mnist.target.astype(np.int8)
X, y = mnist["data"], mnist["target"]

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]

# Train SGDClassifier
sgd_clf = SGDClassifier(random_state=42, max_iter=10)
sgd_clf.fit(X_train, y_train)

# Print the accuracy of SGDClassifier
y_train_predict = sgd_clf.predict(X_train)
sgd_accuracy = accuracy_score(y_train, y_train_predict)
print("Accuracy is %s " % sgd_accuracy)

# Dump the model to the file
joblib.dump(sgd_clf, "trained_models/mnist_model.pkl")
