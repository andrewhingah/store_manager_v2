from flask_restful import Api
from flask import Blueprint

from .views.product_view import AllProducts, SingleProduct
from .views.user_views import UserRegistration, UserLogin

version2 = Blueprint('api version1', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(AllProducts, '/products')
api.add_resource(SingleProduct, '/products/<int:id>')
api.add_resource(UserRegistration, '/auth/signup')
api.add_resource(UserLogin, '/auth/login')