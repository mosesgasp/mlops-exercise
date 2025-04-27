import json
import os
import app

def test_model_file_created():
    app.main()  # Assuming the main function encapsulates the training logic
    assert os.path.exists('models/model.pkl')

def test_model_score():
    score = app.main()  # Assuming the main function returns the score
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0 
    
    # Load the model scores
    scores_file = 'scores/model_scores.json'
    assert os.path.exists(scores_file), "Model scores file not found"
    
    with open(scores_file, 'r') as f:
        model_scores = json.load(f)
    
    # Get the latest model score
    assert len(model_scores) > 0, "No model scores found"
    latest_score = model_scores[-1]['score']
    
    # Compare the latest score with the current score
    assert score == latest_score, "Current model score doesn't match saved score"