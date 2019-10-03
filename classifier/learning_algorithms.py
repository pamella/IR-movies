import json
import nlp
import time
import pandas as pd
import numpy as np

from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


with open('classifier/train_sets/X_train.json') as f:
    X_train = json.load(f)

with open('classifier/train_sets/Y_train.json') as f:
    Y_train = json.load(f)

words_freq = nlp.get_words_frequency(X_train)
with open('classifier/vocab/words_freq.json', 'w') as f:
    json.dump(words_freq, f)

most_freq_tokens = nlp.get_most_freq_tokens(words_freq, 200)
with open(f'classifier/vocab/most_freq_tokens_{200}.json', 'w') as f:
    json.dump(most_freq_tokens, f)

X_train_vec = nlp.vectorize(X_train, most_freq_tokens)
X_train = X_train_vec

def stats(skf, X_train, Y_train):
    nb = GaussianNB()
    dt = DecisionTreeClassifier()
    svm = SVC()
    lr = LogisticRegression()
    mlp = MLPClassifier()
    classifiers = [nb, dt, svm, lr, mlp]
    accuracies = []
    precisions = []
    recalls = []
    train_times = []

    for train, test in skf.split(X_train, Y_train):
        trainX = list(map(lambda x: X_train[x], train))
        trainY = list(map(lambda x: Y_train[x], train))
        testX = list(map(lambda x: X_train[x], test))
        testY = list(map(lambda x: Y_train[x], test))
        local_accuracies = []
        local_precisions = []
        local_recalls = []
        local_time = []

        for classifier in classifiers:
            time_initial = time.time()
            classifier.fit(trainX, trainY)
            time_final = time.time()
            predY = classifier.predict(testX)
            local_accuracies.append(classifier.score(testX, testY))
            local_precisions.append(precision_score(testY, predY))
            local_recalls.append(recall_score(testY, predY))
            local_time.append(time_final - time_initial)

        accuracies.append(local_accuracies)
        precisions.append(local_precisions)
        recalls.append(local_recalls)
        train_times.append(local_time)
    stats_result = {
        'accuracies': accuracies,
        'precisions': precisions,
        'recalls': recalls,
        'train_times': train_times,
    }
    return stats_result

def print_full_stats(classifiers, metrics, stats):
    classifiers = [classifier.upper() for classifier in classifiers]
    for metric in metrics:
        df = pd.DataFrame(stats[metric], columns=classifiers)
        print(f'-- STATS {metric.upper()}--\n{df}\n')

def print_mean_stats(classifiers, metrics, stats):
    classifiers = [classifier.upper() for classifier in classifiers]
    metrics_mean = []
    for metric in metrics:
        mean = np.mean(pd.DataFrame(stats[metric], columns=classifiers))
        metrics_mean.append(mean)
    df_metrics_mean = pd.DataFrame(metrics_mean, index=metrics)
    print(f'-- STATS MEAN --\n{df_metrics_mean}')
    return df_metrics_mean


# Testing 
classifiers = ['naive bayes', 'decision tree', 'svm', 'logistic regression', 'mlp']
metrics = ['accuracies', 'precisions', 'recalls', 'train_times']

# Stratified K-Folds cross-validator
# Provides train/test indices to split data in train/test sets.
# The folds are made by preserving the percentage of samples for each class.

# 1
skf = StratifiedKFold(n_splits = 10)
stats1 = stats(skf, X_train_vec, Y_train)

print(f'-- STATS USING SKF = 10 --\n')
# print_full_stats(classifiers, metrics, stats1)
print_mean_stats(classifiers, metrics, stats1)

# 2
skf2 = StratifiedKFold(n_splits = 20)
stats2 = stats(skf2, X_train_vec, Y_train)

print(f'-- STATS USING SKF = 20 --\n')
print_mean_stats(classifiers, metrics, stats2)

# 3
skf3 = StratifiedKFold(n_splits = 50)
stats3 = stats(skf3, X_train_vec, Y_train)

print(f'-- STATS USING SKF = 50 --\n')
mean_stats_3 = print_mean_stats(classifiers, metrics, stats3)

# Saving csv
with open(f'classifier/csv/mean_stats_{50}.csv', 'w') as f:
    mean_stats_3.to_csv(f, sep=';', index=False)