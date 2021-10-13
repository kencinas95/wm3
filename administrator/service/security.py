import time
import uuid
import hashlib
import logging


log = logging.getLogger('wm.admin.security')


def generate_sid(username: str, salt: str,  pepper: str) -> str:
    """
    Generates a new sid.

    :param username: username
    :param salt: salt
    :param pepper: pepper
    :return: session token
    """
    log.info(f"Generating session token for administrator {username}")

    ts_now = str(int(time.time())).encode('utf-8')

    sid = hashlib.sha512(username.encode('utf-8'))
    sid.update(salt.encode('utf-8'))
    sid.update(pepper.encode('utf-8'))
    sid.update(ts_now)

    return sid.hexdigest()


def generate_pepper_for_administrator(username: str) -> str:
    """
    Generates a pepper for a new administrator.

    :param username: username
    :return: pepper
    """
    log.info(f"Generating a pepper for new administrator: {username}")

    ts_now = str(int(time.time()))

    pepper = hashlib.sha256(username)
    pepper.update(ts_now)
    pepper.update(uuid.uuid4().hex)

    return pepper.hexdigest()


def generate_secure_password(raw_password: str, salt: str, pepper: str) -> str:
    """
    Generates a secure password.

    :param raw_password: plain text password
    :param salt: intern salt
    :param pepper: final pepper
    :return: secure password
    """
    log.info(f"Generating a secure password using salt: {salt}, pepper: {pepper}")

    password = hashlib.sha512(raw_password.encode('utf-8'))
    password.update(salt.encode('utf-8'))
    password.update(pepper.encode('utf-8'))

    return password.hexdigest()

