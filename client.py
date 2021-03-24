import socket, random, threading, sys, time

if len(sys.argv) != 3:
    print("Incorrect command: script, IP adress, port number.\nExample: python3 client.py 127.0.0.1 8888")
    exit()    
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
name = input('Enter your name: ')
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((IP, PORT)) 
    
def announceClient():
    while True:
        try:
            message = c.recv(8760).decode('ascii')
            if message == "name?":
                c.send(name.encode('ascii'))
            else:
                print(message)
        except:
            print('Something went wrong!')
            c.close()
            break

def grantClient():
    while True:
        message = f'{name}: {input("")}'
        c.send(message.encode('ascii'))
        time.sleep(2) #Stops the chat from being flooded by delaying with 2 seconds
        
action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])

def adam(a, b = None):
 return "I think {} sounds great!".format(a + "ing")


def ali(a, b = None):
 if b is None:
    return "Not sure about {}. Don't I get a choice?".format(a + "ing")

 return "Sure, both {} and {} seems ok to me".format(a, b + "ing")


def mohammed(a, b = None):
 action = a + "ing"
 bad_things = ["fighting", "bickering", "yelling", "complaining"]
 good_things = ["singing", "hugging", "playing", "working"]

 if action in bad_things:
    return "YESS! Time for {}".format(action)

 elif action in good_things:
    return "What? {} sucks. Not doing that.".format(action)
 return "I don't care!"

print("\nMe: Do you guys want to {}? \n".format(action))
print("Adam: {}".format(adam(action)))
print("Ali: {}".format(ali(action)))
print("Mohammed: {}".format(mohammed(action)))

send_thread = threading.Thread(target=grantClient)
send_thread.start()

receive_thread = threading.Thread(target=announceClient)
receive_thread.start()
