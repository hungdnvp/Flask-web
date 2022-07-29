from my_information_Flask import app,db
from my_information_Flask.models import Admin, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Admin':Admin, 'Post': Post}
