import requests


class LoginException(Exception):
    pass


class ConnectionErrorException(Exception):
    pass


url = 'https://www.1secmail.com/api/v1/'


def __get_json(params):
    r = requests.get(url, params=params)
    if r.status_code != 200:
        raise ConnectionErrorException(str(r.status_code))
    return r.json()


def __verify_login(login):
    forbidden = ['abuse', 'webmaster', 'contact', 'postmaster', 'hostmaster', 'admin']
    if login in forbidden:
        raise LoginException("Forbidden login")


def gen_random():
    params = {'action': 'genRandomMailbox'}
    return __get_json(params)[0]


def get_domains():
    params = {'action': 'getDomainList'}
    return __get_json(params)


def get_mailbox(login, domain):
    __verify_login(login)
    params = {'action': 'getMessages',
              'login': login,
              'domain': domain}
    return __get_json(params)


def fetch_msg(login, domain, msg_id):
    __verify_login(login)
    params = {'action': 'readMessage',
              'login': login,
              'domain': domain,
              'id': msg_id}
    return __get_json(params)
