import logging
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseNotFound, HttpResponseServerError


class LoggerMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response
        self.logger = self.init_access_logger()

    def __call__(self, request):
        response = self.get_response(request)
        status_code = response.status_code
        if (request.user.is_anonymous and status_code in  [301,302] and hasattr(response,'url') and reverse('login') in response.url):
            self.logger.info("access security page!")
        provided_path = request.path
        if status_code == 404:

            self.logger.info(f"ERROR {status_code}.Page does not exist. {provided_path}")

        if status_code == 500:
            self.logger.info(f"ERROR {status_code}. Internal server error. Path {provided_path}")
        return response

    def init_access_logger(self) -> object:
        access_logger = logging.getLogger(f"main_logger")
        access_logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        main_logger_handler = logging.FileHandler(f"access.log", mode="a", encoding="utf-8")
        main_logger_handler.setFormatter(formatter)
        access_logger.addHandler(main_logger_handler)
        return access_logger


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception:
            return HttpResponseServerError("Server error")

    def process_exception(self, request, exception):
        return HttpResponseNotFound("Page not found")
