from utils.brick import EV3ColorSensor
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

CS = EV3ColorSensor(1)

def train_model():
    model = KNeighborsClassifier(weights="distance")

    data = []
    labels = []

    for i, color in enumerate(["blue", "red", "green"]):
        with open(f"{color}.csv", "r") as f:
            for line in f.readlines():
                data.append(line.split(","))
                labels.append(i)
    
    model.fit(data, labels)
