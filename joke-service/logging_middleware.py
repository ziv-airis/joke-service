from typing import Callable
from fastapi import FastAPI, Request, Response
from logger import Logger, LoggingMode
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.concurrency import iterate_in_threadpool


LOGGER_CONFIG_PATH = "../config/logger_config.yaml"
my_logger = Logger(LOGGER_CONFIG_PATH, LoggingMode.DEV)


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        self._logger = my_logger.logger
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        await self.log_request(request)
        response = await call_next(request)
        await self.log_response(response)
        return await call_next(request)

    async def log_request(self, request: Request):
        path = request.url.path
        if request.query_params:
            path += f"?{request.query_params}"

        request_logging = {
            "method": request.method,
            "path": path,
            "ip": request.client.host,
            "headers": request.headers,
        }

        self._logger.info(f"Request: {request_logging}")

    async def log_response(self, response: Response):
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        response_logging = {
            "status_code": response.status_code,
            "body": response_body,
            "headers": response.headers,
        }
        self._logger.info(f"Rsponse: {response_logging}")
