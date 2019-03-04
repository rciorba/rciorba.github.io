from sanic import Sanic
from sanic.response import json

app = Sanic("pytim")
@app.listener("before_server_start")
def init_mongo(sanic, loop):
    # setup db ...

@app.route("svc_vt_info/search", methods=["POST"])
async def handle(request):
    _id = request.json.get("id")
    if _id is None:
        return json({"status": "error"}, status=400)
    result = await db.info.find({"_id": {"$in": _id}})\
      .to_list(length=None)
    if result is None:
        return json(None, status=404)
    return json({"data": result})

app.run(host="0.0.0.0", port=9090)
