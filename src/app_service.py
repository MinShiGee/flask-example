from datetime import datetime
from re import split
from flask import json, request
import flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
import jwt
from .models import tb_user, tb_purchase, tb_program, tb_season, tb_episode

db = SQLAlchemy()

class appService():

####################################################
# Parse Code
####################################################
    def parse_request(self, request:flask.request):
        if request.is_json:
            return request.json
        return request.form.deepcopy()

    def parse_request_key(self, request:flask.request, key:str = None):
        try:
            return request.form[key]
        except:
            pass
        try:
            return request.json[key]
        except:
            pass
        return None

####################################################
# User Code
####################################################

    def create_user(self, args:dict):
        name = args['name']
        adult = args['adult']
        email = args['email']
        last_login_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        db.session.add(tb_user(name,adult,email,last_login_time))
        self.commit()

    def fetch_user(self, id:int):
        user = db.session.query(tb_user).get(id)
        return user
    
    def get_user_by_name(self, name:str):
        return tb_user.query.filter_by(name=name).first()
    
####################################################
# Purchase Code
####################################################

    def create_purchase(self, current_user:tb_user, args:dict):
        product_id = args['episode_id']
        purchase_time = 'now()'
        db.session.add(tb_purchase(current_user.user_id, product_id, purchase_time))
    
    def fetch_user_purchases(self, current_user:tb_user):
        purchases = db.session.query(tb_purchase).filter(tb_purchase.user_id == current_user.user_id).all()
        return purchases

####################################################
# Program Code
####################################################

    def create_program(self, args:dict):
        title = args['title']
        des = ""
        if 'description' in args:
            des = args['description']
        db.session.add(tb_program(title,des))
        self.commit()
    
    def fetch_all_program(self):
        return db.session.query(tb_program).all()
    
    def fetch_program(self, id:int):
        program = db.session.query(tb_program).get(id)
        return program
    
####################################################
# Season Code
####################################################

    def create_season(self, args:dict):
        program_id = args['program_id']
        title = args['title']
        member = args['member']
        director = args['director']
        season_cnt = args['season_cnt']
        genre = args['genre']
        db.session.add(tb_season(program_id,title,member,director,season_cnt,genre))
        self.commit()

    def fetch_all_season(self):
        return db.session.query(tb_season).all()
    
    def fetch_program_season(self, program_id:int):
        if program_id == None:
            return []
        return db.session.query(tb_season).filter_by(program_id=program_id).all()

    def fetch_season(self, id:int):
        season = db.session.query(tb_season).get(id)
        return season

####################################################
# Episode Code
####################################################

    def create_episode(self, args:dict):
        season_id = args['season_id']
        number = args['number']
        guest = args['guest']
        date = args['date']
        grade = args['grade']
        db.session.add(tb_episode(season_id,number,guest,date,grade))
        self.commit()

    def fetch_all_episode(self):
        return db.session.query(tb_episode).all()

    def fetch_episode(self, id:int):
        episode = db.session.query(tb_episode).get(id)
        return episode

    def filter_season_episodes(self, current_user:tb_user, season_id:int):
        if season_id == None:
            return []
        if not current_user.adult.startswith('adult'):
            return db.session.query(tb_episode).filter(tb_episode.grade.startswith('adult') == False).filter_by(season_id=season_id).all()
        return db.session.query(tb_episode).filter_by(season_id=season_id).all()

####################################################
# Login Code
####################################################

    def check_login(self, id:str):
        user = None
        try:
            user = db.session.query(tb_user).filter_by(name=id).first()
            user.last_login_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            self.commit()
        except:
            pass
        return user

####################################################
# Search Code
####################################################

    def search_content(self, current_user:tb_user, args:dict):
        content = []
        scnt = 0
        seasons = db.session.query(tb_season)
        if 'genre' in args.keys():
            val = args['genre']
            seasons = seasons.filter(tb_season.genre == val)
            scnt += 1
        if 'member' in args.keys():
            val = args['member']
            seasons = seasons.filter(tb_season.member == val)
            scnt += 1
        if 'title' in args.keys():
            val = args['title']
            seasons = seasons.filter(tb_season.title == val)
            scnt += 1
        if scnt > 0:
            seasons = seasons.all()
            seasons = [season for season in seasons]
            content += seasons

        ecnt = 0
        episodes = db.session.query(tb_episode)
        if 'guest' in args.keys():
            val = args['guest']
            episodes = episodes.filter(tb_episode.guest == val)
            ecnt += 1
        if ecnt > 0:
            if not current_user.adult.startswith('adult'):
                episodes = episodes.filter(tb_episode.grade < 19)
            episodes = episodes.all()
            episodes = [episode for episode in episodes]
            content += episodes

        if ecnt == 0 and scnt == 0:
            if not current_user.adult.startswith('adult'):
                episodes = episodes.filter(tb_episode.grade < 19)
            episodes = episodes.all()
            episodes = [episode for episode in episodes]
            content += episodes
            seasons = seasons.all()
            seasons = [season for season in seasons]
            content += seasons

        return content

    def commit(self):
        db.session.commit()