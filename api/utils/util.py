from ..models.users import User
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from functools import wraps
from http import HTTPStatus

BLACKLIST = set()


def get_user_type(id:int):
    """
    Get authorized user type
    """
    user = User.query.filter_by(id=id).first()
    if user:
        return user.user_type
    else:
        return None


def admin_required():
    """
    Decorator to allow only users with admin access
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if get_user_type(claims["sub"]) == "admin":
                return fn(*args, **kwargs)
            else:
                return {"message": "Admin access only"}, HTTPStatus.FORBIDDEN
        return decorator
    return wrapper