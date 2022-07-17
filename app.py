
from surveys import satisfaction_survey as survey
from flask import Flask, request, render_template, redirect, flash, session
app = Flask(__name__)

app.config['SECRET_KEY'] = "catsarethebest24321837"


@app.route('/')
def home_page():
    return render_template('start_page.html',survey = survey)

@app.route('/start')
def start_session():

    session['responses'] = []

    return redirect(f'/questions/{0}')




@app.route('/answer/<id>',methods=["POST"])
def answers_page(id):
    id = int(id)
    responses = session['responses']
    choice = request.form['question_choice']
    responses.append(choice)
    session['responses'] = responses

    return redirect(f'/questions/{id}')



@app.route('/questions/<id>', methods=["GET"])
def question_page(id):
    id = int(id)

    responses = session['responses']

    if id != len(responses):
        flash("Don't try to skip!")
        return redirect(f'/questions/{len(responses)}')
    id = len(responses)


    if id >= len(survey.questions):
        return redirect('/thanks')
    else:
        question = survey.questions[id]
        id = id+1

        return render_template('questions.html', question=question, id=id)


@app.route('/thanks')
def form_page():
    return render_template('thank_user.html')
