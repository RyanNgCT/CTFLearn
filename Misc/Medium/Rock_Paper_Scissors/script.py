import socket
import random

# Define the IP address and port
IP_ADDRESS = '138.197.193.132'
PORT = 5001

# default options for the game
options = ["R", "P", "S"]
answerList = []
counter = 11 # skip the header reply
curr_answer = None

try:
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    answer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((IP_ADDRESS, PORT))
    print(f"Connected to {IP_ADDRESS} on port {PORT}")

    # Receive data from the server
    header = client_socket.recv(1024)

    while counter:
        prompt = client_socket.recv(1024)

        prompt_list = str(prompt.decode()).split() ## split by whitespace

        # state = 0
        # for ele in prompt_list:
        #     try:
        #         ele = int(ele)
        #     except:
        #         pass
        #     else:
        #         state = ele

        if counter == 11:
            pass
        else:
            curr_answer = str(prompt_list[2])
            answerList.append(curr_answer)
        
        chosen_option = random.choice(options)
        counter -= 1

        ## print("Client chose the option: ", chosen_option)
        client_socket.send(chosen_option.encode())

        ## can discard this data (garbage collection)
        review = client_socket.recv(1024)
    
    client_socket.close()

    print(f"Answer List: {answerList}\nSending answers now...")

    answer_socket.connect((IP_ADDRESS, PORT))
    header = answer_socket.recv(1024)

    newans = None
    for i in range(10):
        prompt = answer_socket.recv(1024)
        # print(prompt)

        ## gameplay logic to beat the robot
        if answerList[i] == "R":
            newans = "P"
        elif answerList[i] == "P":
            newans = "S"
        elif answerList[i] == "S":
            newans = "R"
        answer_socket.send(newans.encode())
        print("Sending ", newans)

        ## can discard this data (garbage collection)
        review = answer_socket.recv(1024)
        # print(review)

    flag = answer_socket.recv(1024)
    print(flag.decode())

    answer_socket.close()

except socket.error as e:
    print(f"Error: {e}")

finally:
    # Close the socket connection
    client_socket.close()
