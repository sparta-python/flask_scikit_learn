import pickle
import numpy as np


def model(number):
    with open("predict_population.pickle", mode="rb") as fp:
        model = pickle.load(fp)
    return model.predict(np.array([[number]]))
