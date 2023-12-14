from flask import Flask, request, render_template,redirect,session
from sudopy import Sudoku, Generate
import sqlite3
app = Flask(__name__)
app.secret_key='sud@123'
# the 2D list of the starting numbers in the sudoku 
play_list = []

# boolean that is True if a Sudoku has been generated using
#   the Generate object, False otherwise
has_gen = False

@app.route("/")# this will take to home page when we click it
def home():
    return render_template("loginpage.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" :
        
        user = str(request.form["name"])
        password=str(request.form["password"])

        conn=sqlite3.connect('mydb1.db')
        cursor=conn.cursor()
        cursor.execute("select user_name,password from credentials where user_name=? and password=?;",(user,password))
        row=cursor.fetchall()
        if len(row)==1:
            session['loggedin']=True
            session['user_name']=row[0][0]
            return redirect("/menu")
        
            #return render_template()
        # if user=="arun2110763@ssn.edu.in" and password=="a": # Replace this line with the code that checks details from a database.
        #     return redirect("/menu")
        else:
            return render_template("loginpage.html") 
    else:
        return render_template('reg.html')   

@app.route('/reg',methods=["POST","GET"])
def reg():
    if request.method == "POST":
        user_e=str(request.form["new_e"])
        pass_e=str(request.form["new_p"])
        conn=sqlite3.connect('mydb1.db')
        cursor=conn.cursor()
        cursor.execute("insert into credentials values(?,?,?);",(user_e,pass_e,10))
        conn.commit()
        conn.close()
        session['loggedin']=True
        return redirect("/menu")
    
@app.route('/menu')
def menu():
    global has_gen
    has_gen = False
    return render_template('menu.html')


@app.route('/input_play')
def input_play():
    return render_template('input_play.html')


@app.route('/input_solve')
def input_solve():
    return render_template('input_solve.html')


@app.route('/play', methods=['POST', 'GET'])
def play():
    global play_list
    global has_gen
    sudoku_grid_list = []
    if request.method == 'POST':

        # if the POST request is from '/input_play' or '/play'
        if 'play' in request.referrer:

            # build 2D list in order to initialize Sudoku object
            for i in range(9):
                row_list = []
                for j in range(9):
                    id = "" + str(i*9 + j)
                    content = request.form[id]
                    if content == "":
                        row_list.append(0)
                    else:
                        row_list.append(int(content))
                sudoku_grid_list.append(row_list)
            s = Sudoku(sudoku_grid_list)

            # if the POST request is from '/input_play"
            if '/input_play' in request.referrer:
                play_list = s.return_array()

                # renders the play.html file
                # is_solved will be "None" since the sudoku is not completed
                # input_array is initialized to play_list, which contains the starting numbers of a sudoku
                # play_array refers to the compiled 2D list after a user has finished playing a sudoku; in this case, play_array will be None
                return render_template('play.html', is_solved = "None", input_array = play_list, play_array = None)

            # if the POST request is from '/play" (when the user checks their sudoku)
            elif '/play' in request.referrer:
                # renders the play.html file
                # is_solved is initialized to a boolean of whether the completed sudoku is valid
                # check_array is initialized to a 2D list of booleans that signify if each cell is valid
                # input_array is initialized to play_list, which contains the starting numbers of a sudoku
                # play_array refers to the compiled 2D list after a user has finished playing the sudoku
                return render_template('play.html', is_solved = s.check_grid(), check_array = s.check_grid_items(), input_array = play_list, play_array = s.return_array())

        # if the POST request is from the menu page
        elif '/' in request.referrer:

            # obtain the user specified difficulty
            if request.form.get('easy') != None:
                content = request.form.get('easy')
            elif request.form.get('medium') != None:
                content = request.form.get('medium')
            elif request.form.get('hard') != None:
                content = request.form.get('hard')
            else:
                content = request.form.get('expert')
            
            # if a Sudoku hasn't already been generated, create one of the specified difficulty
            if not has_gen:
                g = Generate(content)
                play_list = g.generate_sudoku()
                has_gen = True
            return render_template('play.html', is_solved = "None", input_array = play_list, play_array=None)
    else:
        return render_template('play.html', is_solved="None", input_array = play_list, play_array = None)


@app.route('/solution', methods=['POST', 'GET'])
def solution():
    sudoku_grid_list = []
    if request.method == 'POST':

        # build 2D list from inputted numbers in order to initialize Sudoku object
        for i in range(9):
            row_list = []
            for j in range(9):
                id = "" + str(i*9 + j)
                content = request.form[id]
                if content == "":
                    row_list.append(0)
                else:
                    row_list.append(int(content))
            sudoku_grid_list.append(row_list)

        # Create the solved Sudoku based off of the numbers inputted by the user in '/input_solve'
        s = Sudoku(sudoku_grid_list)
        s.solve()

        return render_template('solution.html', solved_array = s.return_array())
    else:
        return render_template('menu.html')


if __name__ == "__main__":
    app.run(debug=True, port=7650)