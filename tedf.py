from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Todo(db.Model):
    sRo = db.Column(db.Integer, primary_key=True)
    MATERIAL=db.Column(db.String(200), nullable=False)
    Description = db.Column(db.String(500), nullable=False)
    case_pack = db.Column(db.String(200), nullable=False)
    Rack = db.Column(db.String(200), nullable=False)
    PILLER = db.Column(db.String(200), nullable=False)
    Level = db.Column(db.String(200), nullable=False)
    Pallet = db.Column(db.String(200), nullable=False)
    Present_Count = db.Column(db.String(200), nullable=False)

    # data_created= db.Column(db.DateTime,default=datetime.utcnow)




def __repr__(self) -> str:
    return f"{self.sno}- {self.MATERIAL}"
with app.app_context():
    db.create_all()

@app.route('/',methods=['GET', 'POST'])
def product():
    if request.method=='POST':
        print("pos")

    todo = Todo(MATERIAL="Email1 ", Description="Start investing")
    db.session.add(todo)
    db.session.commit()
    allTodo=Todo.query.all() 
    return render_template("login.html", allTodos=allTodo)
@app.route('/sho')
def pro():
    allTodo= Todo.query.all()
    return "how are you"
    
if __name__=="__main__":
    app.run(debug=True)



