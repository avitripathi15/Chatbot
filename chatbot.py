import openai
from flask import Flask, render_template, request

# Set up your OpenAI API credentials
openai.api_key = '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'

app = Flask(__name__)

def generate_answer(question, context):
    # Prepare the prompt for the API call
    prompt = f'Question: {question}\nContext: {context}\nAnswer:'

    # Generate the answer using OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the model to use
        prompt=prompt,
        max_tokens=100,  # Adjust the value based on desired answer length
        n=1,  # Generate a single answer
        stop=None,  # Let the model determine when to stop generating
        temperature=0.6,  # Control the randomness of the generated answer
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated answer from the API response
    answer = response.choices[0].text.strip()

    return answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    topic = request.form['topic']
    question = request.form['question']

    # Generate the answer for the question
    answer = generate_answer(question, topic)

    return render_template('answer.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run()
