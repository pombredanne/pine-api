from aiohttp import web

import version

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(version.routes)
    web.run_app(app, host="127.0.0.1", port=8080)
