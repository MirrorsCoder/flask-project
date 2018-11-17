# #encoding: utf-8
#
# from flask4 import db
#
# class database(db.Model):
#     gender = db.Column(db.String(3))
#     university = db.Column(db.String(15))
#     year = db.Column(db.String(10))
#     JID = db.Column(db.String(20),primary_key=True)
#
#     def __init__(self,gender,university,year,JID):
#         self.gender = gender
#         self.university = university
#         self.year = year
#         self.JID = JID
#
#     # def __repr__(self):
#     #     return