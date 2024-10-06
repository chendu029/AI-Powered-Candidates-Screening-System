from flask import Flask, request, render_template, jsonify
from models import evaluate_response
from scoring import calculate_score

app = Flask(__name__)

# Define mock interview questions
questions = {
    'technical': "Explain the concept of overfitting in machine learning and how to prevent it.",
    'problem_solving': "Given a dataset, explain how you would approach building a machine learning model.",
    'soft_skills': "How do you handle collaboration in a team where members have different skill levels?"
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    responses = {
        'technical': request.form['technical'],
        'problem_solving': request.form['problem_solving'],
        'soft_skills': request.form['soft_skills']
    }
    
    evaluations = evaluate_response(responses)
    score_info = calculate_score(evaluations)
    
    return jsonify(score_info)

if __name__ == '__main__':
    app.run(debug=True)
