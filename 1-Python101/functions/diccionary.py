

"""
To send the values to a function as a diccionary you can send them separetly and 
receivethem in the function with **
"""


def save_user_(**user):
    print(user)
    print(user["name"])


save_user_(id=32, name="Rosy")


""" 
Or you can simply send the m to the function as a diccionary
"""


def save_user_di(user):
    print(user)
    print(user["name"])


di = {'id': 24, 'name': "Katy"}
save_user_di(di)
