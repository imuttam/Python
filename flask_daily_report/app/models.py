from app import db

class Report(db.Model):
    id =        db.Column("id",db.Integer, primary_key=True)
    date =      db.Column('date', db.DateTime)
    voice_2G  = db.Column('voice_2G' ,db.Integer,  nullable=False)
    voice_3G  = db.Column('voice_3G' ,db.Integer, nullable=False)
    volte =     db.Column('volte', db.Float, nullable=False)
    data_2G =   db.Column('data_2G', db.Float, nullable=False)
    data_3G =   db.Column('data_3G', db.Float, nullable=False)
    data_4G =   db.Column('data_4G', db.Float, nullable=False)
    vlrcount =   db.Column('vlrcount' ,db.Integer,  nullable=False)
    total_voice = db.Column('total_voice' ,db.Integer,  nullable=False)
    total_data = db.Column('total_data', db.Float, nullable=False)


    def __repr__(self):
        return f"Report('{self.date}', '{self.total_voice}', {self.total_data})"
