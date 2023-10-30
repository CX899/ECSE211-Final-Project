from utils.brick import EV3ColorSensor
from sklearn.neighbors import KNeighborsClassifier

#### GLOBAL VARIABLES ####

CS = EV3ColorSensor(1)
model = KNeighborsClassifier(weights="distance")
distance_cap = 0.9 # Limit on model certainty. Subject to change during testing.

def train_model():
    data = []
    labels = []

    for i, color in enumerate(["blue", "red", "green"]):
        with open(f"{color}.csv", "r") as f:
            for line in f.readlines():
                data.append(line.split(","))
                labels.append(i)
    
    model.fit(data, labels)

def classify(point):
    """ Classifies an rgb point as blue, red, or green. Classifies as other if confidence on that
    point is beyond the threshold given by distance_cap.

    Params
    ------
        point: list<int>
            red, green, and blue values

    Returns
    -------
        color: int
            0 for blue, 1 for red, 2 for green, or 3 for other.
    """
    probabilities = model.predict_proba([point])
    confidence = max(probabilities)
    if confidence < distance_cap:
        return 3
    return probabilities.index(confidence)