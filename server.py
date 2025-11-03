import contextlib
from fastapi import FastAPI
import os
from math_server import mcp as math_mcp
from jack import mcp2 as jack_mcp
from web import mcp_web as web_mcp
from weather import mcp_weather as weather_mcp
from people import mcp_people as people_mcp


# Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(math_mcp.session_manager.run())
        await stack.enter_async_context(jack_mcp.session_manager.run())
        await stack.enter_async_context(web_mcp.session_manager.run())
        await stack.enter_async_context(weather_mcp.session_manager.run())
        await stack.enter_async_context(people_mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/math", math_mcp.streamable_http_app())
app.mount("/jack", jack_mcp.streamable_http_app())
app.mount("/web", web_mcp.streamable_http_app())
app.mount("/weather", weather_mcp.streamable_http_app())
app.mount("/people", people_mcp.streamable_http_app())

PORT = os.environ.get("PORT", 10000)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)