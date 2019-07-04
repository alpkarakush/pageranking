from bottle import get, post, request, Bottle, run  # or route

from scripts import searchEngine

app = Bottle()

@app.route('/search')
def search():
    return '''
        <form action="/search" method="post">
            Search: <input name="search" type="text" />
           
            <input value="Submit" type="submit" />
        </form>
    '''

@app.route('/search', method='POST')
def search():
    query = request.forms.get('search')

    se = searchEngine.SearchEngine()

    result = se.query(query)



    htmlOutput = ''
    for i in result:
        htmlOutput += "<a href=\"" + str(i) + "\">" + "Link</a>" + "<br />"



    return htmlOutput




run(app, host='localhost', port=8080)