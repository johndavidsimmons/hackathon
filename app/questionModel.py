
from sqlalchemy import Column, Integer, String, Boolean, Date,\
    ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
# from . import db


# ################################################################################
engine = create_engine('sqlite:///./masterDB.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
# ################################################################################


assocation_table = Table('assocation', Base.metadata,
    Column('questionID', Integer, ForeignKey('questions.questionID')),
    Column('surveyID', Integer, ForeignKey('surveys.surveyID')))


class QuestionModel(Base):
    __tablename__ = 'questions'

    questionID = Column(Integer(), primary_key=True)
    creatorID = Column(Integer())  # foreign key to userDim
    text = Column(String(255))
    publicOrPrivate = Column(Boolean())
    createDt = Column(Date())
    survey = relationship(
        'SurveysModel', 
        secondary=assocation_table,
        back_populates='question')


class ResponsesModel(Base):
    __tablename__ = 'responses'

    responseID = Column(Integer(), primary_key=True)
    response = Column(Integer())
    surveyID = Column(Integer())
    questionID = Column(Integer())
    bridgeID = Column(Integer())
    userID = Column(Integer())


class SurveysModel(Base):
    __tablename__ = 'surveys'

    surveyID = Column(Integer(), primary_key=True)
    creatorID = Column(Integer())
    surveyName = Column(String(255))
    createDt = Column(Date())
    question = relationship(
        'QuestionModel',
        secondary=assocation_table,
        back_populates='survey')
