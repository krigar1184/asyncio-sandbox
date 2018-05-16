import asyncio
import functools
import tempfile


f = tempfile.NamedTemporaryFile(delete=False)


async def read():
    print('reading from {}'.format(f.name))
    f.seek(0)
    result = f.read().decode('utf8')
    print('read {}'.format(result))
    return result


async def write(i):
    print('writing {} to {}'.format(i, f.name))
    f.write(bytes(i))
    await asyncio.sleep(0)
    print('written {}'.format(i))
    return await read()


loop = asyncio.get_event_loop()
future = asyncio.gather(*[asyncio.ensure_future(write(i)) for i in range(10)])
future.add_done_callback(functools.partial(print, 'pewpew'))
loop.run_until_complete(future)
loop.close()
