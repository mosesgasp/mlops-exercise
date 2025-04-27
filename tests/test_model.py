import os
import joblib
import pandas as pd
from app import load_data, preprocess_data, split_data, train_model, evaluate_model

def test_model_training_and_saving():
    # Load and preprocess data
    data = load_data('data/credit_card_records.csv')
    data = preprocess_data(data)
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(data, 'Fraudulent')
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Test model
    score = evaluate_model(model, X_test, y_test)
    
    # Check if model file was created
    assert os.path.exists('models/model.pkl'), "Model file was not created"
    
    # Load saved model
    saved_model = joblib.load('models/model.pkl')
    
    # Check if saved model gives same score
    saved_score = evaluate_model(saved_model, X_test, y_test)
    assert abs(score - saved_score) < 0.0001, "Saved model score differs from original model"
    
    # Check if score is within reasonable range
    assert 0 <= score <= 1, "Model score is not between 0 and 1" 