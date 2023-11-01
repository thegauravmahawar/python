class ApiResponse:
    data = None


class ApiResponseSuccess(ApiResponse):
    status = 'ok'

    def __init__(self, data):
        self.data = data


class ApiResponseError(ApiResponse):
    status = 'error'

    def __init__(self, data):
        self.data = data
