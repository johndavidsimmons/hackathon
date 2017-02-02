from . import db
from flask import current_app, request

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	office = db.Column(db.String(128))
	division = db.Column(db.String(128))
	teamLeaderEmail = db.Column(db.String(128))
	sipAddress = db.Column(db.String(128))
	string_id = db.Column(db.String(128))
	isRemote = db.Column(db.String(128))
	title = db.Column(db.String(128))
	location = db.Column(db.String(128))
	email = db.Column(db.String(128))
	subTeam = db.Column(db.String(128))
	companyName = db.Column(db.String(128))
	team = db.Column(db.String(128))
	teamLeader = db.Column(db.String(128))
	phone = db.Column(db.String(128))
	pictureUrl = db.Column(db.String(128))
	anniversaryDate = db.Column(db.String(128))
	displayName = db.Column(db.String(128))
	firstName = db.Column(db.String(128))
	extension = db.Column(db.Integer)
	lastName = db.Column(db.String(128))
	rockworldProfileURL = db.Column(db.String(128))
	trsName = db.Column(db.String(128), index=True)

	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)

	def __repr__(self):
		return '<User: {}>'.format(self.displayName)	


# db.create_all()
# d = json.loads(open("wewlad.json").read())
# tms = d['results']
# for i in tms:
# 	try:
# 		db.session.add(User(office=i.get('office', "NA"), 
# 			division=i.get('division', "NA"), 
# 			teamLeaderEmail=i.get("teamLeaderEmail", "N/A"), 
# 			sipAddress = i.get("sipAddress", "NA"), 
# 			string_id=i.get("id", "NA"), 
# 			isRemote=i.get("isRemote", "NA"), 
# 			title=i.get("title", "NA"), 
# 			location = i.get("location", "NA"), 
# 			email = i.get("email", "NA"), 
# 			subTeam = i.get("subTeam", "NA"), 
# 			companyName = i.get("companyName", "NA"), 
# 			team = i.get("team", "NA"), 
# 			teamLeader = i.get("teamLeader", "NA"), 
# 			phone = i.get("phone", "NA"), 
# 			pictureUrl = i.get("pictureUrl", "NA"), 
# 			anniversaryDate = i.get("anniversaryDate", "NA"), 
# 			displayName = i.get("displayName", "NA"), 
# 			firstName = i.get("firstName", "NA"), 
# 			extension = i.get("extension", "NA"), 
# 			lastName = i.get("lastName", "NA"), 
# 			rockworldProfileURL = i.get("rockworldProfileURL", "NA"), 
# 			trsName = i.get("trsName", "NA") ))
# 	except Exception as e:
# 		print e



