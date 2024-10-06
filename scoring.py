def calculate_score(evaluations):
    # Define weights for each type of response
    weights = {
        'technical': 0.6,
        'problem_solving': 0.3,
        'soft_skills': 0.1
    }
    
    total_score = 0
    for skill, score in evaluations.items():
        total_score += weights[skill] * score
    
    # Normalize the score out of 100
    normalized_score = total_score * 20  # Scores were initially between 0-1

    # Assign role based on the score
    if normalized_score >= 80:
        role = 'Senior AI Engineer'
    elif normalized_score >= 60:
        role = 'AI Engineer'
    elif normalized_score >= 40:
        role = 'Junior AI Engineer'
    else:
        role = 'Intern'
    
    return {'total_score': round(normalized_score, 2), 'role': role}
