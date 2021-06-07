from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)


    @app.route('/')
    def hello():
        return render_template('base.html',msg='')

    return app


    @app.route('/predict', methods=['POST'])
    def predict():
        if request.method == 'GET':
            # forward to home page
            return render_template('base.html', msg='please send the data using defined methods')
        else:
            age = request.form['age']
            exp = request.form['experience']
            domain = request.form['domain']


            # predict the salary
            salary = 1000

            return render_template('predict.html', age=age, exp=exp,domain=domain,salary=salary)
