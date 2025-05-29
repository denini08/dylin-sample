import pytest
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def test_multiple_transformed_inputs():
    # create sample data
    X1 = np.array([[1, 2], [3, 4]])
    X2 = np.array([[5, 6], [7, 8]])
    y = np.array([0, 1])

    # initialize transformer and model
    scaler = StandardScaler()
    model = LogisticRegression()

    # transform both datasets (marked as "transformed")
    X1_transformed = scaler.fit_transform(X1)
    X2_transformed = scaler.transform(X2)

    # fit the model
    model.fit(X1_transformed, y)

    # predict with concatenated transformed data
    X_combined = np.vstack([X1_transformed, X2_transformed])
    predictions = model.predict(X_combined)

    # expected: No violation, but false positive
    assert predictions is not None
