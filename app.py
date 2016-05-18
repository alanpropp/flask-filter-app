from flask import Flask, render_template, request
from foo import just_do_it
app = Flask(__name__)

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results")
def results():
    reqargs = request.args
    argument =  reqargs.get('current')


    # return an error if there is no entry
    if not argument:
        return """
            <h1>Error</h1>
            <p>Please enter in a search value!</p>
        """

    elif argument == "smallest":
        search_type = 'smallest'
        results = just_do_it(current = "smallest")
    elif argument == "middle":
        search_type = 'middle'
        results = just_do_it(current = "middle")
    elif argument == "largest":
        search_type = 'largest'
        results = just_do_it(current = "largest")

    html = render_template('results.html', schools=results,
                            search_type=search_type)
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


