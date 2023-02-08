def response(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def error_response(error, message):
    return {"error": error, "message": message}