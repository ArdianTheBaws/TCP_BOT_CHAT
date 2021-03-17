import socket, random, threading, time
import sys
import errno
name = input('Enter your name: ')
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8888))

def announceClient():
    while True:
        try:
            message = c.recv(1024).decode('utf-8')
            if message == "name?":
                c.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('Something went wrong!')
            c.close()
            break

    

def grantClient():
    while True:
        message = f'{name}: {input("")}'
        c.send(message.encode('utf-8'))

action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
def alice(a, b = None):

 return "I think {} sounds great!".format(a + "ing")



def bob(a, b = None):

 if b is None:

    return "Not sure about {}. Don't I get a choice?".format(a + "ing")

 return "Sure, both {} and {} seems ok to me".format(a, b + "ing")



def dora(a, b = None):

 alternatives = ["coding", "singing", "sleeping", "fighting"]

 b = random.choice(alternatives)

 res = "Yea, {} is an option. Or we could do some {}.".format(a, b)

 return res, b



def chuck(a, b = None):

 action = a + "ing"

 bad_things = ["fighting", "bickering", "yelling", "complaining"]

 good_things = ["singing", "hugging", "playing", "working"]

 if action in bad_things:

    return "YESS! Time for {}".format(action)

 elif action in good_things:

    return "What? {} sucks. Not doing that.".format(action)

 return "I don't care!"



action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])



print("\nMe: Do you guys want to {}? \n".format(action))

print("Alice: {}".format(alice(action)))

print("Bob: {}".format(bob(action)))

print("Dora: {}".format(dora(action)))

print("Chuck: {}".format(chuck(action)))


send_thread = threading.Thread(target=grantClient)
send_thread.start()

receive_thread = threading.Thread(target=announceClient)
receive_thread.start()
