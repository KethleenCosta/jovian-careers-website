from flask import Flask, render_template, template_rendered, jsonify
from load_jobs import load_jobs_from_db

app = Flask(__name__)


#HTML endpoint
@app.route('/')
def hello_jovian():  #sending data to the html file via argument
    jobs = load_jobs_from_db()
    return render_template(
        'home.html',  #template language
        jobs=jobs,
        company_name='Jovian')


#JSON endpoint
@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
