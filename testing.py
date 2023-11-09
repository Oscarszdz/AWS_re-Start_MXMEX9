import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)

def log_user_age(age):
    assert age >=0,"Invalid age was supplied"
    print(age)


