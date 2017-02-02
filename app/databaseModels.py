
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
    Base.metadata.create_all(bind=engine)
# ################################################################################


class surveyModel(Base):
    __tablename__ = 'surveymodel'

    surveyID = Column(Integer(), primary_key=True)
    surveyName = Column(String(255))
    surveyCreateDt = Column(String(10))
    responseLimit = Column(Integer())
    creatorID = Column(Integer())
    publicSurvey = Column(Boolean())

    # check this
    question = relationship('questionModel', back_populates='survey')

    def __init__(self, **kwargs):
        super(surveyModel, self).__init__(**kwargs)

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.surveyName, self.surveyCreateDt,
            self.responseLimit, self.creatorID, self.publicSurvey)


class questionModel(Base):
    __tablename__ = 'questionmodel'

    questionID = Column(Integer(), primary_key=True)
    survey_ID = Column(Integer(), ForeignKey('surveymodel.surveyID'))
    questionText = Column(String(255))
    #
    survey = relationship('surveyModel', back_populates='question')
    choice = relationship('choiceModel', back_populates='questionChoice')

    def __init__(self, **kwargs):
        super(questionModel, self).__init__(**kwargs)

    def __repr__(self):
        return '{} {}'.format(self.surveyID, self.questionText)


class choiceModel(Base):
    __tablename__ = 'choicemodel'

    choiceID = Column(Integer(), primary_key=True)
    question_ID = Column(Integer(), ForeignKey('questionmodel.questionID'))
    surveyID = Column(Integer())
    choiceText = Column(String())
    #
    questionChoice = relationship('questionModel', back_populates='choice')
    user = relationship('userResponse', back_populates='userchoice')

    def __init__(self, **kwargs):
        super(choiceModel, self).__init__(**kwargs)

    def __repr__(self):
        return '{} {} {}'.format(self.questionID, self.surveyID, self.choiceText)


class userResponse(Base):
    __tablename__ = 'userresponse'

    userResponseID = Column(Integer(), primary_key=True)
    personId = Column(Integer())
    choice_ID = Column(Integer(), ForeignKey('choicemodel.choiceID'))
    #
    userchoice = relationship('choiceModel', back_populates='user')

    def __repr__(self):
        return '{} {} {}'.format(self.userResponseID, self.personID, self.choiceID)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    office = Column(String(128))
    division = Column(String(128))
    teamLeaderEmail = Column(String(128))
    sipAddress = Column(String(128))
    string_id = Column(String(128))
    isRemote = Column(String(128))
    title = Column(String(128))
    location = Column(String(128))
    email = Column(String(128))
    subTeam = Column(String(128))
    companyName = Column(String(128))
    team = Column(String(128))
    teamLeader = Column(String(128))
    phone = Column(String(128))
    pictureUrl = Column(String(128))
    anniversaryDate = Column(String(128))
    displayName = Column(String(128))
    firstName = Column(String(128))
    extension = Column(Integer())
    lastName = Column(String(128))
    rockworldProfileURL = Column(String(128))
    trsName = Column(String(128), index=True)

    def __init__(self, **kwargs):
            super(User, self).__init__(**kwargs)

    def __repr__(self):
            return '<User: {}>'.format(self.displayName)
