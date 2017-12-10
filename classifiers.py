#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sklearn.metrics import mean_squared_error

def train_classifier(data, labels, clf):
    clf.fit(data, labels.values.ravel())

def score_classifier(data, labels, classifier):
    predictions = classifier.predict(data)
    RMSE = mean_squared_error(predictions, labels) ** 0.5
    return RMSE