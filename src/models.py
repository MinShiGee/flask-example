from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class tb_user(db.Model):
    
    user_id:int
    name:str
    adult:str
    email:str
    last_login_time:str

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    adult = db.Column(db.String(40))
    email = db.Column(db.String(40), unique=True)
    last_login_time = db.Column(db.String(40))

    def __init__(self, name:str, adult:str, email:str, last_login_time:str = ''):
        self.name = name
        self.adult = adult
        self.email = email
        self.last_login_time = last_login_time

@dataclass
class tb_purchase(db.Model):

    purchase_id:int
    user_id:int
    product_id:int
    purchase_time:str

    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('tb_user.user_id'), 
        nullable=False
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('tb_episode.episode_id'),
        nullable=False
    )
    purchase_time = db.Column(
        db.String(40),
        nullable=False
    )

    def __init__(self, user_id:int, product_id:int, purchase_time:str):
        self.user_id = user_id
        self.product_id = product_id
        self.purchase_time = purchase_time

@dataclass
class tb_program(db.Model):

    program_id:int
    title:str
    description:str
    
    program_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), unique=True)
    description = db.Column(db.String(40))

    def __init__(self, title:str, description:str = ''):
        self.title = title
        self.description = description

@dataclass
class tb_season(db.Model):

    season_id:int
    program_id:int
    title:str
    member:str
    director:str
    season_cnt:int
    genre:str

    season_id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(
        db.Integer, 
        db.ForeignKey('tb_program.program_id'), 
        nullable=False
    )
    title = db.Column(db.String(40))
    member = db.Column(db.String(40))
    director = db.Column(db.String(40))
    season_cnt = db.Column(db.Integer)
    genre = db.Column(db.String(40))

    def __init__(self, program_id:int, title:str, member:str, director:str, season_cnt:int, genre:str):
        self.program_id = program_id
        self.title = title
        self.member = member
        self.director = director
        self.season_cnt = season_cnt
        self.genre = genre

@dataclass
class tb_episode(db.Model):

    episode_id:int
    season_id:int
    number:int
    guest:str
    date:str
    grade:int

    episode_id = db.Column(db.Integer, primary_key=True)
    season_id = db.Column(
        db.Integer, 
        db.ForeignKey('tb_season.season_id'), 
        nullable=False
    )
    number = db.Column(db.Integer)
    guest = db.Column(db.String(40))
    date = db.Column(db.String(40))
    grade = db.Column(db.Integer)

    def __init__(self, season_id:int, number:int, guest:str, date:str, grade:int):
        self.season_id = season_id
        self.number = number
        self.guest = guest
        self.date = date
        self.grade = grade