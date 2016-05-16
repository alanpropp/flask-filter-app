<<<<<<< HEAD
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
    _sortby =  reqargs.get('sortby')
    _zipcode = reqargs.get('zipcode')
    _state = reqargs.get('state')


    # return an error if there is no state or zipcode
    if not _zipcode and not _state:
        return """
            <h1>Error</h1>
            <p>Please enter in a search value!</p>
        """


    elif request.args.get('zipcode'):
        search_type = 'zipcode'
        search_val = request.args.get('zipcode')
        peeps = just_do_it(zipcode=search_val, sortby=_sortby)
    elif request.args.get('state'):
        search_type = 'state'
        search_val = request.args.get('state')
        peeps = just_do_it(state=search_val, sortby=_sortby)

    html = render_template('results.html', legislators=peeps, sortby=_sortby,
                            search_type=search_type, search_value=search_val)
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
=======
from flask import Flask
from string import Template
app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello ${place_name}!</h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")

@app.route('/')
def homepage():
    return """<h1>Hello world!</h1>"""

@app.route('/<some_place>')
def some_place_page(some_place):
    return(HTML_TEMPLATE.substitute(place_name=some_place))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
>>>>>>> 34c86b09ea789cd68530791c66fe42ac37dc6203
