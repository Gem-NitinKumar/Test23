from app.code import square

def get(request_object):
    num = int(request_object)
    request_object = {
        "method" : "GET",
        "header": {"application/json"},
        "query_string": { "num": num, "pow": 2},
        "payload": {}
    }
    return square.get(request_object)
    # return render_template("square.html")

    # return response_object

def put(request_object):
    pass
    # return response_object

def post(request_object):
    pass
    # return response_object

def delete(request_object):
    pass
    # return response_object