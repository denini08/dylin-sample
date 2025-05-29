import pytest
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def test_multiple_transformed_inputs():
    # Create sample data
    X1 = np.array([[1, 2], [3, 4]])
    X2 = np.array([[5, 6], [7, 8]])
    y = np.array([0, 1])

    # Initialize transformer and model
    scaler = StandardScaler()
    model = LogisticRegression()

    # Transform both datasets (marked as "transformed")
    X1_transformed = scaler.fit_transform(X1)
    X2_transformed = scaler.transform(X2)

    # Fit the model
    model.fit(X1_transformed, y)

    # Predict with concatenated transformed data
    X_combined = np.vstack([X1_transformed, X2_transformed])
    predictions = model.predict(X_combined)

    # Expected: No violation, but false positive due to _self
    assert predictions is not None



def test_multiple_args_all_transformed_bug():
    """
    Test with multiple transformed arguments + _self bug

    in_args = [X1_transformed, X2_transformed, _self] # size = 3
    initial count = 3
    X1_transformed is transformed → count = 2
    X2_transformed is transformed → count = 1
    _self is NOT transformed → count = 1

    1 != 0 and 1 != 3 → FALSE POSITIVE
    """
    X1 = np.array([[1, 2], [3, 4]])
    X2 = np.array([[5, 6], [7, 8]]) 
    y = np.array([0, 1])
    
    scaler = StandardScaler()
    model = LogisticRegression()
    
    # Both datasets are transformed
    X1_transformed = scaler.fit_transform(X1)
    X2_transformed = scaler.transform(X2)
    
    model.fit(X1_transformed, y)
    
    # Call that should be valid but generates false positive
    # Assuming the model accepts multiple positional arguments
    try:
        predictions = model.predict(X1_transformed, sample_weight=None)
    except:
        # If it doesn't accept multiple args, use concatenation
        X_combined = np.vstack([X1_transformed, X2_transformed])
        predictions = model.predict(X_combined)
