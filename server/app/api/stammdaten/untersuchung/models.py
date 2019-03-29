from app.database import BaseMixin, db

class Untersuchung(BaseMixin, db.Model):
    __tablename__ = "untersuchungen"

    untersID = db.Column(db.Integer, primary_key=True)
    unters_name = db.Column(db.String, nullable=False)
    unters_kbz = db.Column(db.String, nullable=False)



    def json(self):
        return {
            
        }
