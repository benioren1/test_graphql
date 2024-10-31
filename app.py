# pip install -r requirements.txt
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from data_base.db_connaction import db_session, init_db, connection_url
from gql.query import Query
from models.cities import CityModel
from models.contries import CountryModel

app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# with app.app_context():
#     init_db()


schema = Schema(query=Query)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":

    app.run(host='0.0.0.0',
            # debug=True, #todo: maybe remove because we declared before.
            port=5001)