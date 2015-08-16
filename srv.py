#!/usr/bin/env python3.4
import asyncio
from aiohttp import web


@asyncio.coroutine
def count_endpoint(request, storage=dict()):
    key = request.match_info['key']
    count = storage[key] = storage.get(key, 0) + 1
    return web.Response(text=str(count))


app = web.Application()
app.router.add_route('GET', '/count/{key}', count_endpoint)

loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, '0.0.0.0', 8080)
srv = loop.run_until_complete(f)
print('serving on', srv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.run_until_complete(app.finish())
loop.close()
