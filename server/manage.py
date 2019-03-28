import logging
from flask.cli import FlaskGroup

from app import create_app
from app.database import db
from app.api.user.models import User
from app.api.system.models import SystemSetting

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('log/manage.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

prompt = "> "

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('create_admin')
def create_admin_user():
    logger.info("Creating admin")

    logger.info("Username: ?")

    username = input(prompt)
    logger.info("Email: ?")
    email = input(prompt)

    logger.info("Passwort")
    password = input(prompt)
    logger.info("Passwort wiederholen")
    password2 = input(prompt)

    if password != password2:
        logger.info("Passwörter stimmen nicht überein. Bitte den Vorgang wiederholen.")
    else:
        if user.find_by_username(username):
            logger.info("Username ist schon vergeben.")
            break


        user = User(username, password, email)

        try:
            user.is_admin = True
            user.save()
            logger.info("Admin erfolgreich angelegt.")
        except:
            logger.info("Etwas ist beim Speichern der Daten falsch gelaufen.")


@cli.command('system_settings')
def system_settings():
    logger.info("Creating System Settings")

    logger.info("system_email")
    system_email = input(prompt)

    logger.info("email_password")
    email_password = input(prompt)

    logger.info("smtp_port")
    smtp_port = input(prompt)

    logger.info("smtp_host")
    smtp_host = input(prompt)

    logger.info("system_email")
    system_email = input(prompt)

    # TODO: speichern in der Datenbank vorbereiten



if __name__ == '__main__':
    cli()
