from Auth import Auth
import Conf

def test1():
    test1 = Auth(Conf.User_email, Conf.User_password)
    test1.Citadel_auth()
    assert Auth.CheckTrecker

