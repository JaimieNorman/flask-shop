from pyapp import create_app
app = create_app()
from pyapp import db
app.app_context().push()
db.drop_all()
db.create_all()
print('SUCCESSFULLY CREATED DATABASE')