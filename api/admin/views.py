from flask_restx import Namespace, Resource, fields
from ..models.admin import Admin
from ..utils.util import admin_required
from werkzeug.security import generate_password_hash
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity

admin_ns = Namespace("admin", description="Namespace for Admin Operations")

signup_model = admin_ns.model(
    "AdminSignup", {
        "full_name": fields.String(required=True, description="Admin's First & Last Name"),
        "email": fields.String(required=True, description="Admin's Email"),
        "password": fields.String(required=True, description="Admin's Password")
    }
)

admin_model = admin_ns.model(
    "Admin", {
        "id": fields.Integer(description="Admin's User ID"),
        "full_name": fields.String(required=True, description="First & Last Name"),
        # "last_name": fields.String(required=True, description="Last Name"),
        "email": fields.String(required=True, description="Admin's Email"),
        "user_type": fields.String(required=True, description="Type of User")
    }
)

@admin_ns.route("")
class GetAllAdmins(Resource):

    @admin_ns.marshal_with(admin_model)
    @admin_ns.doc(
        description="Get all admin users"
    )
    @admin_required()
    def get(self):
        """
            Get all admin users
        """
        admins = Admin.query.all()

        return admins, HTTPStatus.OK

@admin_ns.route("/signup")
class AdminSignUp(Resource):

    @admin_ns.expect(signup_model)
    # Uncomment the @admin_required() decorator below after registering the first admin
    # This ensures that only an existing admin can register a new admin account on the app
    # @admin_required()
    @admin_ns.doc(
        description = "Register an Admin , after First Admin"
    )
    def post(self):
        """
            Register an Admin , after First Admin
        """        
        data = admin_ns.payload

        # Check if the admin account already exists
        admin = Admin.query.filter_by(email=data["email"]).first()
        if admin:
            return {"message": "Admin Account Already Exists"}, HTTPStatus.CONFLICT

        # Register new admin
        new_admin = Admin(
            full_name = data["full_name"],
            email = data["email"],
            password_hash = generate_password_hash(data["password"]),
            user_type = "admin"
        )

        new_admin.save()

        admin_resp = {}
        admin_resp["id"] = new_admin.id
        admin_resp["full_name"] = new_admin.full_name
        admin_resp["email"] = new_admin.email
        admin_resp["user_type"] = new_admin.user_type

        return admin_resp, HTTPStatus.CREATED

@admin_ns.route("/<int:admin_id>")
class GetUpdateDeleteAdmins(Resource):
    
    @admin_ns.marshal_with(admin_model)
    @admin_ns.doc(
        description = "Get an Admin's Details by ID ",
        params = {
            "admin_id": "The Admin's ID"
        }
    )
    @admin_required()
    def get(self, admin_id):
        """
            Get an Admin's Details by ID 
        """
        admin = Admin.get_by_id(admin_id)
        
        return admin, HTTPStatus.OK
    
    @admin_ns.expect(signup_model)
    @admin_ns.doc(
        description = "Update an Admin's Details by ID",
        params = {
            "admin_id": "The Admin's ID"
        }
    )
    @admin_required()
    def put(self, admin_id):
        """
            Update an Admin's Details by ID 
        """
        admin = Admin.get_by_id(admin_id)
        active_admin = get_jwt_identity()
        if active_admin != admin_id:
            return {"message": "You don't have access to this resource"}, HTTPStatus.FORBIDDEN

        data = admin_ns.payload

        admin.full_name = data["full_name"]
        admin.email = data["email"]
        admin.password_hash = generate_password_hash(data["password"])

        admin.update()

        admin_resp = {}
        admin_resp["id"] = admin.id
        admin_resp["full_name"] = admin.full_name
        admin_resp["email"] = admin.email
        admin_resp["user_type"] = admin.user_type

        return admin_resp, HTTPStatus.OK
    
    @admin_ns.doc(
        description = "Delete an Admin by ID ",
        params = {
            "admin_id": "The Admin's ID"
        }
    )
    @admin_required()
    def delete(self, admin_id):
        """
            Delete an Admin by ID 
        """
        admin = Admin.get_by_id(admin_id)

        admin.delete()

        return {"message": "Admin Successfully Deleted"}, HTTPStatus.OK