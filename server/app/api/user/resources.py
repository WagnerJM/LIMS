import logging
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt, get_jwt_identity

from app.api.user.models import User
from app.api.system.models import SystemSetting
from app.security import TokenBlacklist

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('../../log/user.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


class UserRegisterApi(Resource):

    def  post(self):

        data = request.get_json()
        logger.info(data)

        if User.find_by_username(data.get('username')):
            logger.info("User not found.")
            return {
                "msg": "Dieser Username ist bereits vergeben."
            }, 500

        user = User(**data)
        try:
            logger.info("Saving user data {}".format(data))
            user.save()
            return {
                "msg": "User wurde erfolgreich angelegt."
            }
        except:
            logger.info("ERROR while saving user data.")
            return {
                "msg": "Der User konnte nicht angelegt werden. Ein Fehler ist auftreten."
            }

class UserLoginApi(Resource):

    def post(self):
        user = User.find_by_username(data.get('username'))

        if user and user.check_password(data.get('password'), user._password):
            logger.info("Creating access_token")
            access_token = create_access_token(identity=str(user.id), fresh=True)
            return {
                "access_token": access_token,
                "username": user.username
            }, 200

        return {
            "msg": "Invalid credentials"
        }, 401

class UserLogoutApi(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        token = TokenBlacklist(jti=jti)

        try:
            token.save()
            return {
                "msg": "Sie wurden erfolgreich ausgeloggt."
            }, 200
        except:
            return {
                "msg": "Es ist ein Fehler beim Ausloggen aufteten."
            }, 500


class UserApi(Resource):

    @jwt_required
    def get(self):
        user = User.find_by_id(get_jwt_identity())

        if not user:
            return {
                "msg": "User nicht gefunden."
            }, 404
        return {
            "user": user.json()
        }, 200


    @jwt_required
    def put(self):
        user = User.find_by_id(get_jwt_identity())
        data = request.get_json()

        if not user:
            return {
                "msg": "Kein User gefunden."
            }, 404

        else:
            for key, value in data.items():
                user[key] = data[key]


        try:
            user.save()
            return {
                "msg": "Daten wurden gespeichert."
            }, 201
        except:
            return {
                "msg": "Etwas ist beim Speichern der User-Daten schief gelaufen."
            }, 500



class AdminUserApi(Resource):

    @jwt_required
    def get(self):
        admin = User.find_by_id(get_jwt_identity())

        if not user.is_admin:
            return {
                "msg": "Sie haben nicht die notwendigen Rechte."
            }, 403
        users = User.get_all()

        return {
            "users": [ user.json() for user in users ]
        }

    @jwt_required
    def put(self):
        admin = User.find_by_id(get_jwt_identity())
        data = request.get_json()

        user = User.find_by_id(data['user_id'])

        if not user.is_admin:
            return {
                "msg": "Sie haben nicht die notwendigen Rechte."
            }, 403

        if not user:
            return {
                "msg": "User konnte nicht gefunden werden."
            }, 404

        else:
            for key, value in data.items():
                user[key] = data[key]

        try:
            user.save()
            return {
                "msg": "User {username}/{vorname} wurde geupdatet.".format(username=user.username, vorname=user.vorname)
            }
        except:
            return {
                "msg": "Ein Fehler ist beim Speichern aufgetreten."
            }, 500

class AdminSysSettingApi(Resource):
    @jwt_required
    def get(self):
        systemSetting = SystemSetting.get_setting()
        admin = User.find_by_id(get_jwt_identity())

        if not user.is_admin:
            return {
                "msg": "Sie haben nicht die notwendigen Rechte."
            }, 403

        if not sysSetting:
            return {
                "msg": "Etwas ist schief gelaufen."
            }, 500

        return {
            "sysSetting": systemSetting.json()
        }

    @jwt_required
    def put(self):
        admin = User.find_by_id(get_jwt_identity())
        systemSetting = SystemSetting.get_setting()

        if not admin.is_admin:
            return {
                "msg": "Sie haben nicht die notwendigen Rechte."
            }, 403

        if not sysSetting:
            return {
                "msg": "Etwas ist schief gelaufen."
            }, 500

        data = request.get_json()

        for key, value in data.items():
            systemSetting[key] = data[key]

        try:
            sysSetting.save()
            return {
                "msg": "System Einstellungen wurden erfolgreich gespeichert."
            }, 201
        except:
            return {
                "msg": "Etwas ist beim Speichern der System Einstellungen schief gelaufen"
            }, 500
            
