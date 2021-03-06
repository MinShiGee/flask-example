from src.app import create_app

app = create_app({
    'SECRET_KEY': 'inisoftassignmentsecretkey',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'postgresql+psycopg2://<sqlid>:<sqlpassword>@<server>/<dbname>',
})
app.run()