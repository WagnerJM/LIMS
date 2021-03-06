from app.database import BaseMixin, db

class SystemSetting(BaseMixin, db.Model):
    __tablename__ = 'systemSettings'

    sysSettingID = db.Column(db.Integer, primary_key=True)
    system_email = db.Column(db.String)
    email_password = db.Column(db.String)
    smtp_port = db.Column(db.Integer, default=587)
    smtp_host = db.Column(db.String, default="smtp.gmail.com")
    email_tls = db.Column(db.Boolean, default=True)
    email_body = db.Column(db.Text)


    def __init__(self, system_email, email_password, smtp_port, smtp_host, email_tls ):
        self.system_email = system_email
        self.email_password = email_password
        self.smtp_port = smtp_port
        self.smtp_host = smtp_host
        self.email_tls = email_tls


    def json(self):
        return {
            "id": str(self.id),
            "system_email": self.sytem_email,
            "smtp_host": self.smtp_host,
            "smtp_port": self.smtp_port,
            "email_tls": self.email_tls,
            "email_body": self.email_body
        }

    @classmethod
    def get_setting(cls):
        return cls.query.get(1)
