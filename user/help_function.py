import json

def getrequest(request):
    print(request)
    if request.content_type == "application/json":
        data = json.loads(request.body)
    else:
        data = request.POST
    return data