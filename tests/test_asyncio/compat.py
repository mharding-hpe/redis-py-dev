import asyncio

try:
    from contextlib import aclosing
except ImportError:
    import contextlib

    @contextlib.asynccontextmanager
    async def aclosing(thing):
        try:
            yield thing
        finally:
            await thing.aclose()


def create_task(coroutine):
    return asyncio.create_task(coroutine)
