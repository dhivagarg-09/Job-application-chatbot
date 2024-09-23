from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').strip().lower()
    
    if not hasattr(chat, 'step'):
        chat.step = 0
        chat.user_data = {}
        chat.mode = None

    if chat.step == 0:
        if 'recruiter' in user_message:
            chat.mode = 'recruiter'
            chat.step += 1
            response = "Great! Let's start by getting the company name."
        elif 'candidate' in user_message:
            chat.mode = 'candidate'
            chat.step += 1
            response = "Awesome! Let's start by getting your name."
        else:
            response = "Please specify if you're a recruiter or a candidate."
    elif chat.mode == 'recruiter':
        response = handle_recruiter_chat(user_message)
    elif chat.mode == 'candidate':
        response = handle_candidate_chat(user_message)

    return jsonify({'response': response})

def handle_recruiter_chat(message):
    if chat.step == 1:
        chat.user_data['company_name'] = message
        chat.step += 1
        return "Thank you! What's your email address?"
    elif chat.step == 2:
        chat.user_data['email'] = message
        chat.step += 1
        return "Got it. How many years of experience are you looking for?"
    elif chat.step == 3:
        chat.user_data['experience'] = message
        chat.step += 1
        return "Please provide the LinkedIn profile URL of the company or recruiter."
    elif chat.step == 4:
        chat.user_data['linkedin'] = message
        chat.step += 1
        return "Could you briefly describe the job role?"
    elif chat.step == 5:
        chat.user_data['job_description'] = message
        chat.step += 1
        return ("Thank you! Here's the summary of the job listing:<br>"
                f"Company Name: {chat.user_data['company_name']}<br>"
                f"Email: {chat.user_data['email']}<br>"
                f"Experience Required: {chat.user_data['experience']}<br>"
                f"LinkedIn: {chat.user_data['linkedin']}<br>"
                f"Job Description: {chat.user_data['job_description']}<br>"
                "If everything looks good, we will proceed with the next steps!")
    else:
        return "Thank you!"

def handle_candidate_chat(message):
    if chat.step == 1:
        chat.user_data['name'] = message
        chat.step += 1
        return "Nice to meet you! What's your phone number?"
    elif chat.step == 2:
        chat.user_data['phone'] = message
        chat.step += 1
        return "Thank you! What's your email address?"
    elif chat.step == 3:
        chat.user_data['email'] = message
        chat.step += 1
        return "Great! Can you provide your LinkedIn profile URL?"
    elif chat.step == 4:
        chat.user_data['linkedin'] = message
        chat.step += 1
        return "Could you describe the kind of job role you're looking for?"
    elif chat.step == 5:
        chat.user_data['job_description'] = message
        chat.step += 1
        return ("Thank you! Here's the summary of your application:<br>"
                f"Name: {chat.user_data['name']}<br>"
                f"Phone: {chat.user_data['phone']}<br>"
                f"Email: {chat.user_data['email']}<br>"
                f"LinkedIn: {chat.user_data['linkedin']}<br>"
                f"Job Description: {chat.user_data['job_description']}<br>"
                "We will proceed with your application!")
    else:
        return "Thank you!"

if __name__ == '__main__':
    app.run(debug=True)
