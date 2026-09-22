import os
from flask import Flask, render_template, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    env_name = os.environ.get('FLASK_ENV', 'Production')
    azure_app_name = os.environ.get('WEBSITE_SITE_NAME', 'Local Environment')
    return render_template('index.html', env_name=env_name, azure_app_name=azure_app_name)
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'azure-flask-app',
        'environment': os.environ.get('WEBSITE_SITE_NAME', 'local')
    }), 200
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

    