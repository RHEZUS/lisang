from django.utils.deprecation import MiddlewareMixin

class JWTAuthCookieMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # If 'Authorization' header is not present but we have a cookie, set it
        if 'Authorization' not in request.headers and 'access_token' in request.COOKIES:
            access_token = request.COOKIES['access_token']
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
