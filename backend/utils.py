import hashlib
from typing import Optional, Callable

from starlette.requests import Request
from starlette.responses import Response


def fixed_api_key_builder(
    func: Callable,
    namespace: Optional[str] = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple] = None,
    kwargs: Optional[dict] = None,
) -> str:
    print("kwargs.items():", kwargs.items())
    arguments = {}
    for key, value in kwargs.items():
        if key != "db":
            arguments[key] = value
    arguments["url"] = request.url

    prefix = f"{namespace}:"
    cache_key = (
        prefix
        + hashlib.md5(
            f"{func.__module__}:{func.__name__}:{args}:{arguments}".encode()
        ).hexdigest()
    )
    return cache_key