from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return None
    data = response.data if isinstance(response.data, dict) else {"detail": response.data}
    response.data = {"success": False, "error": data, "status_code": response.status_code}
    return response
