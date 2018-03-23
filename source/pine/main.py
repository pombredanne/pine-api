import multiprocessing

from sanic import Sanic
from sanic.response import json

from version import version_info

app = Sanic()


@app.get("/version")
async def get_version(request):
    return json(version_info())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6666, workers=multiprocessing.cpu_count())
