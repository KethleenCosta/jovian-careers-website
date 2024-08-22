from flask import Flask, render_template, template_rendered, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengalaru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Data Enginner',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Enginner',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    },
]


#HTML endpoint
@app.route('/')
def hello_jovian():  #sending data to the html file via argument
    return render_template(
        'home.html',  #template language
        jobs=JOBS,
        company_name='Jovian')


#JSON endpoint
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
