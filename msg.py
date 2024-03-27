def getMsg (msg, mode=None):
    if not mode:
        mode = "Success"
    
    return {
        "msg" : msg,
        "mode": mode
    }  