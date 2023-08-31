from fastapi import Request


class MyMiddleware:
    def __init__(
            self,
            some_attribute: str,
    ):
        self.some_attribute = some_attribute

    async def __call__(self, request: Request, call_next):
        # do something with the request object
        content_type = request.headers.get('Content-Type')
        print(content_type)

        # process the request and get the response
        response = await call_next(request)

        return response
