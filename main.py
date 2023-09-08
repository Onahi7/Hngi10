from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api')
def api():
    slack_name = request.args.get('slack_name') 
    track = request.args.get('track')

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    today = days[datetime.datetime.today().weekday()]

    time = datetime.datetime.utcnow().isoformat()

    response = {
        'slack_name': slack_name,
        'current_day': today,
        'utc_time': time, 
        'track': track,
        'github_file_url': 'hhttps://github.com/Onahi7/Hngi10.git/main.py',
        'github_repo_url': 'https://github.com/Onahi7/Hngi10.git',
        'status_code': 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()
