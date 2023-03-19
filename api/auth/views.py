from flask import request
from flask_restx import Namespace, Resource, fields
from ..models.users import User
from ..utils.util import BLACKLIST, admin_required
from werkzeug.security import check_password_hash
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

auth_ns = Namespace("auth", description=" Authentication Operations")

user_model = auth_ns.model(
    "User", {
        "id": fields.Integer(description="User ID"),
        "full_name": fields.String(required=True, description="Full Name"),
        "email": fields.String(required=True, description="User's Email"),
        "password_hash": fields.String(required=True, description="User's Password"),
        "user_type": fields.String(required=True, description="Type of User")  
    }
)

login_model = auth_ns.model(
    "Login", {
        "email": fields.String(required=True, description="User's Email"),
        "password": fields.String(required=True, description="User's Password")
    }
)

@auth_ns.route("/users")
class GetAllUsers(Resource):
    @auth_ns.marshal_with(user_model)
    @auth_ns.doc(
        description="Retrieve all users"
    )
    @admin_required()
    def get(self):
        """
            Retrieve all Users
        """
        users = User.query.all()

        return users, HTTPStatus.OK

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """
            Generate JWT Token
        """
        data = auth_ns.payload

        email = data["email"]
        password = data["password"]

        user = User.query.filter_by(email=email).first()

        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)

            response = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

            return response, HTTPStatus.CREATED


@auth_ns.route("/refresh")
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
            Refresh Access Token
        """
        user = get_jwt_identity()

        access_token = create_access_token(identity=user)

        return {"access_token": access_token}, HTTPStatus.OK


@auth_ns.route("/logout")
class Logout(Resource):
    @jwt_required(verify_type=False)
    def post(self):
        """
            Logout and Revoke Access/Refresh Token
        """
        token = get_jwt()
        jti = token["jti"]
        token_type = token["type"]
        BLACKLIST.add(jti)
        return {"message": f"{token_type.capitalize()} token revoked!"}, HTTPStatus.OK