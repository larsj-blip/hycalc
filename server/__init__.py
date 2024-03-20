import os

from flask import Flask, render_template, request, jsonify, send_from_directory

from server import calculations
from server.calculations.fueling import refuel_data
from server.calculations.price_calculation import total_cost_of_driving_your_vehicle


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,
                static_folder="static/static", template_folder="static")
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/calculate/truck', methods=['POST'])
    def calculate_data_for_truck():
        form_data = request.json
        distance_traveled = form_data['distance_traveled']
        refuel_data_object = refuel_data(distance_traveled)
        print(refuel_data_object)
        return jsonify(refuel_data_object)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

    @app.route('/help')
    def help():
        return f'{os.getcwd()}'

    return app
