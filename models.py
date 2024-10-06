from transformers import pipeline

# Load a pre-trained model for sentiment analysis
nlp_model = pipeline("sentiment-analysis")

def evaluate_response(responses):
    evaluations = {}

    for key, response in responses.items():
        # Use the NLP model to process each response
        evaluation = nlp_model(response)
        evaluations[key] = evaluation[0]['score']
        
    return evaluations
