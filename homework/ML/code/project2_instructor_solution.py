"""
This module provides the requested output for Project 6.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


class MyClassifier:
    """
    This class is a wrapper for sk-learn classifiers.
    It incorperates basic decision plotting in an
    object oriented way.
    """

    def __init__(self, scikit_classifier):
        self._internal_classifier = scikit_classifier
        self.predictors_used_for_training = None
        self.observations_used_for_training = None

    def train(self, predictors, observations):
        """
        Trains the classifier passed to the constructor.
        :param predictors: The predictors, given in an array form.
        :param observations: The observation associated with a row of predictors.
        :return: Nothing
        """
        self.predictors_used_for_training = predictors
        self.observations_used_for_training = observations
        self._internal_classifier.fit(predictors, observations)

    def predict(self, predictors):
        """
        Predicts the classes of an array of predictors.
        :param predictors: The array of predictors to utilize.
        :return: The classes predicted by the classifier passed in the constructor.
        """
        return self._internal_classifier.predict(predictors)

    def plot_decision_areas(self, x_label="X", y_label="Y", show_training_data=True):
        """
        Plots the decision areas based on the first and second predictors.
        :param x_label: What the x-axis should be labeled.
        :param y_label: What the y-axis should be labeled.
        :param show_training_data: Overlay the training data on the decision boundary.
        :return: Nothing.
        """
        x_coordinates, y_coordinates = self._get_background_points()
        colors = self._get_background_point_colors(x_coordinates, y_coordinates)
        plt.scatter(x_coordinates, y_coordinates, alpha=0.1, c=colors)

        if show_training_data:
            plt.scatter(x=self.predictors_used_for_training[:, 0],
                        y=self.predictors_used_for_training[:, 1],
                        alpha=1,
                        c=self._get_training_point_colors(), )

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def _get_training_point_colors(self):
        colors = [self._get_color(obs) for obs in self.observations_used_for_training]
        return colors

    def _get_background_point_colors(self, x_coordinates, y_coordinates):
        coordinates_as_predictors = np.array((x_coordinates, y_coordinates)).transpose()
        predictions = self.predict(coordinates_as_predictors)
        colors = [self._get_color(prediction) for prediction in predictions]
        return colors

    @staticmethod
    def _get_color(prediction):
        value = int(prediction)

        colors = ["#1B9E77",
                  "#D95F02",
                  "#7570B3",
                  "#E7298A",
                  "#66A61E",
                  "#E6AB02",
                  "#A6761D",
                  "#666666"]

        return colors[value - 1]

    @staticmethod
    def _get_axis_window(predictor):
        predictor_min = min(predictor)
        predictor_max = max(predictor)
        predictor_sd = np.std(predictor)

        return predictor_min - predictor_sd, predictor_max + predictor_sd

    def _get_background_points(self, density=100):
        x_min, x_max = self._get_axis_window(self.predictors_used_for_training[:, 0])
        y_min, y_max = self._get_axis_window(self.predictors_used_for_training[:, 1])
        x_axis = np.linspace(x_min, x_max, density)
        y_axis = np.linspace(y_min, y_max, density)
        grid = np.meshgrid(x_axis, y_axis)
        x_coordinates = grid[0].reshape(1, -1)[0]
        y_coordinates = grid[1].reshape(1, -1)[0]

        return x_coordinates, y_coordinates


CSV_FILE_NAME = "data.csv"
DATA = np.genfromtxt(CSV_FILE_NAME, delimiter=",", skip_header=1)

OBSERVATIONS = DATA[:, 0]
PREDICTORS = DATA[:, 1:]

MY_NN_CLASSIFIER = MyClassifier(KNeighborsClassifier())
MY_NN_CLASSIFIER.train(PREDICTORS, OBSERVATIONS)
MY_NN_CLASSIFIER.plot_decision_areas("Sepal Area", "Petal Area")

MY_TREE_CLASSIFIER = MyClassifier(DecisionTreeClassifier())
MY_TREE_CLASSIFIER.train(PREDICTORS, OBSERVATIONS)
MY_TREE_CLASSIFIER.plot_decision_areas("Sepal Area", "Petal Area")
