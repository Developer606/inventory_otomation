from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from picking_data import show_location,picking
from datetime import datetime
app = Flask(__name__)
app1 =app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)





class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)



def __repr__(self) -> str:
    return f"{self.sno}- {self.title}"
with app.app_context():
    db.create_all()

@app.route('/',methods=['GET', 'POST'])
def Login():
    if request.method=='POST':

        title= request.form["title"]
        desc= request.form["Password1"]
        print(title,desc)
            # print(request.form.get('Password1'))
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo=Todo.query.all()

    return render_template("index.html", allTodos=allTodo)
Location= " "
@app.route('/enter_location',methods=['GET', 'POST'])
def location():
    
    if request.method=='POST':
        location= request.form['Location1']
        Location=str(location)
        ass= open("hallo.txt",'w')
        ass.write(Location)
        ass.close()
        print(location)
        
        return redirect("/Update")
    return render_template("show.html")



@app.route('/Update',methods=['GET', 'POST'])
def Update():
   
    if request.method=='POST':
        qunity= int(request.form['Quantity2'])
        # picking(location,qunity)
        er = open("hallo.txt",'r')
        asr= er.read()
        picking(asr,qunity)

        print(asr,qunity)
        
        return redirect("/enter_location")
    asse= open("hallo.txt",'r')
    ts= asse.read()
    asse.close()
    pR=(show_location(ts))

    scores = "1"
    MATERIAL=str(pR[0])
    Description=str(pR[1])
    case_pack=str(pR[2])
    Present_Count=str(pR[10])
    exp={"MATERIAL":MATERIAL,"Description":Description,"case pack":case_pack,"Present Count":Present_Count}
   

    return render_template("picked.html", result=exp )

@app.route('/sho')
def pro():
    Todo.query.all()
    return "how are you"
    
if __name__=="__main__":
    app.run(debug=True)
