from aiohttp import web

from lib import version

routes = web.RouteTableDef()


@routes.get("/version")
async def get_version(request):
    return web.json_response(version.version_info)
