import time

class ExeTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # one time configuration and initialization

    def __call__(self, request):
        # code to be executed for each request before
        # the view (later middleware) are called

        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"Total time : {duration}")

        # Code to be executed for each request/response after
        # the view is called

        return response
