from flask import Flask, render_template

#wir legen app Objekt an mit dem wir die Webbanwendung kunfigurieren könnne
app = Flask(__name__)

counter = 0

#wir definieren eine route via dekorator das mit dem @
@app.route("/")
def index ():
    global counter
    counter += 1

    #Rendern von template(Vorlage) index.html im Verzeichniss templates
    return render_template("index.html", zaehler=counter)

@app.route("/about_me")
def about_me ():
    return render_template("about_me.html")

@app.route("/portfolio")
def portfolio ():
    return render_template("portfolio.html")

@app.route("/02_fakebook")
def fakebook ():
    return render_template("02_fakebook.html")

@app.route("/google")
def google ():
    return render_template("google.html")

@app.route("/hairdresser_hans")
def hairdersser_hans ():
    return render_template("hairdresser_hans.html")


#wenn dieses Modul das Hauptmodul ist, dann satrten wir flask
if __name__=="__main__":
    app.run()