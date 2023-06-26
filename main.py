from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def startseite():
    return render_template('startseite.html')

@app.route('/kuenstler')
def kuenstler():
    return render_template('kuenstler.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/chatbot', methods=['POST', 'GET'])
def chatbot():
    user_message = request.form['message']

    # Hier kannst du den Benutzereingabe verarbeiten und eine Antwort generieren.
    # Für dieses Beispiel verwenden wir eine einfache statische Antwort.
    bot_response = "This is a sample response from the chatbot."

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)