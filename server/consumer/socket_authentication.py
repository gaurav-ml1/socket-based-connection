import jwt
import uuid


class EquipmentAuthenticationMiddleware:
    """
    Custom middleware that takes token from the query string.
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):
        # Look up user from query string (you should also do things like
        # check it's a valid user ID, or if scope["user"] is already populated)
        # You can manage accordingly you.
        valid_data = None
        try:
            for header in set(scope.get("headers")):
                if b'authorization' in header:
                    valid_data = jwt.decode(header[1].decode("utf-8"), 'secret', algorithms=['HS256'])
                    break
            print(valid_data)
        except:
            # closed connection.
            self.close()

        # Return the inner application directly and let it run everything else
        return self.inner(dict(scope, user="backpack_agent"))
