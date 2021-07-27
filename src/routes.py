from datetime import datetime, timedelta
from src.models import tb_user
from flask.globals import current_app
import jwt
from flask import Blueprint, request
from flask import redirect, jsonify
from flask.helpers import make_response
from .app_service import appService
from functools import wraps

bp = Blueprint('home', __name__)
service = appService()
token_dic = {}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        token = request.args.get('token')
        if 'access_token' in service.parse_request(request).keys():
            token = service.parse_request_key(request, 'access_token')
        if not token:
            return jsonify({'message':'need token'}), 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_user = service.get_user_by_name(data['user'])
            if token != token_dic[current_user.name]:
                return jsonify({'messge':'use new token'}), 403
        except:
            return jsonify({'message':'token error'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

####################################################
# Oauth Route
####################################################

@bp.route('/oauth/login', methods= ['POST'])
def login():
    name = service.parse_request_key(request, 'id')
    user = service.check_login(name)
    if(user == None):
        return make_response('auth error','401')

    token = jwt.encode({'user':user.name, 'exp': datetime.utcnow() + timedelta(minutes=30)}, current_app.config['SECRET_KEY']).decode('UTF-8')
    token_dic[user.name] = token
    return jsonify({'access_token':token})

@bp.route('/oauth/logout', methods= ['GET'])
@token_required
def logout(current_user):
    token_dic.pop(current_user.name)
    return jsonify({'message':'token removed'}), 200

@bp.route('/oauth/signup', methods= ['POST'])
def signup():
    form = service.parse_request(request)
    service.create_user(form)
    return jsonify({'message':'success'}), 200

####################################################
# User Route
####################################################

@bp.route('/api/user', methods= ['GET'])
@token_required
def get_user(current_user:tb_user):
    user = service.fetch_user(current_user.user_id)
    return jsonify(user)

####################################################
# Purchase Route
####################################################

@bp.route('/api/purchase', methods= ['GET'])
@token_required
def get_purchase(current_user:tb_user):
    purchases = service.fetch_user_purchases(current_user)
    return jsonify(purchases)

@bp.route('/api/purchase', methods= ['POST'])
@token_required
def create_purchase(current_user:tb_user):
    form = service.parse_request(request)
    service.create_purchase(current_user, form)
    return jsonify({'message':'success'}), 200

####################################################
# Program Route
####################################################

@bp.route('/api/program', methods= ['GET'])
def get_all_program():
    all_program = service.fetch_all_program()
    return jsonify(all_program)

@bp.route('/api/program', methods= ['POST'])
@token_required
def post_program(current_user:tb_user):
    form = service.parse_request(request)
    service.create_program(form)
    return jsonify({'message':'success'}), 200

####################################################
# Season Route
####################################################

@bp.route('/api/season', methods= ['GET'])
def get_season_by_program():
    program_id = service.parse_request_key(request, 'program_id')
    seasons = service.fetch_program_season(program_id)
    return jsonify(seasons)

@bp.route('/api/season', methods= ['POST'])
@token_required
def post_season(current_user:tb_user):
    form = service.parse_request(request)
    service.create_season(form)
    return redirect('/home')

####################################################
# Episode Route
####################################################

@bp.route('/api/episode', methods= ['GET'])
@token_required
def get_episode_by_season(current_user):
    season_id = service.parse_request_key(request, 'season_id')
    all_episode = service.filter_season_episodes(current_user, season_id)
    return jsonify(all_episode)

@bp.route('/api/episode', methods= ['POST'])
@token_required
def post_episode(current_user:tb_user):
    form = service.parse_request(request)
    service.create_episode(form)
    return jsonify({'message':'success'}), 200

####################################################
# Search Route
####################################################

@bp.route('/api/search', methods= ['GET'])
@token_required
def search_content(current_user):
    args = service.parse_request(request)
    data = service.search_content(current_user, args)
    return jsonify(data)
    