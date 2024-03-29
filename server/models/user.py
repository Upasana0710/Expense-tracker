from sqlalchemy.orm import relationship
from app import app, db
from sqlalchemy import Enum
from sqlalchemy import inspect

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200))
    age = db.Column(db.Integer,default=14)
    image = db.Column(db.String) 
    financialKnowledge = db.Column(Enum('BEGINNER', 'INTERMEDIATE', 'ADVANCED',name='financial_knowledge_enum',default='BEGINNER'))
    monthlyIncome = db.Column(db.Float,default=0.0)
    riskTolerance = db.Column(Enum('CONSERVATIVE', 'MODERATE', 'AGGRESSIVE', name='risk_tolerance_enum',default='CONSERVATIVE'))
    googleAuth = db.Column(db.Boolean, nullable=False, default=False)

    @staticmethod
    def createTable():
        try:
            with app.app_context():
                db.create_all()
            print("Created table")
        except:
            print("Error")
    
    @staticmethod
    def dropTable():
        try:
            with app.app_context():
                db.metadata.drop_all(bind=app)
            print("Dropped table")
        except Exception as e:
            print(f"Error: {e}")
