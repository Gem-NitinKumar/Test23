def get(request_object):
    num = int(request_object["query_string"]['num'])
    return _square_impl(num)

def put(request_object):
    pass
    # return response_object

def post(request_object):
    num = int(request_object["payload"]['num'])
    return _square_impl(num)
    # return response_object

def delete(request_object):
    pass
    # return response_object


def _square_impl(num):
    square = num * num
    response = {
        "num": num,
        "square": square
    }
    return response
