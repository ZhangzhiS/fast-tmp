#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.core.config import settings
from app.core.err import BaseError
from app.api.v1.user import user_route


def create_app() -> FastAPI:
    fast_app = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    register_middleware(fast_app)
    register_route(fast_app)
    rewrite_err(fast_app)
    return fast_app


def register_middleware(fast_app):
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_route(fast_app):
    fast_app.include_router(user_route, prefix=settings.API_V1_STR, tags=["user"])


def err_handler(request: Request, exc: BaseError):
    return JSONResponse(
        status_code=200,
        content={"code": exc.code, "msg": exc.msg, "data": exc.data}
    )


def rewrite_err(fast_app: FastAPI):

    fast_app.add_exception_handler(BaseError, err_handler)


app = create_app()


if __name__ == '__main__':
    import uvicorn
    a = create_app()
    uvicorn.run(a)
