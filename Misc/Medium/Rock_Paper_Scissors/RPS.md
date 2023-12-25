# Rock-Paper-Scissors

Do you think you're lucky enough to win 10 games of Rock Paper Scissors in a row? Connect to the server and find out. `nc 138.197.193.132 5001`

## Approach

Since I had to beat the "robot" 10 times as per the prompt, I figured putting my python skills to the test.
```
----------- Let's play rock, paper, scissors!
----------- Beat me 10 times in a row to win the flag!

Please choose: R / P / S
>>>
```

Entering a correct option gives:
```
You won! Consecutive wins: 1
I chose S based on 139951793
```

While entering an incorrect one gives this:
```
You didn't win!
I chose R based on 2454155475
```

At first I thought the number has something to do with an initialized random state (thus the commented state code in script.py) or that it meant something when I tried to obtain the remainder of the first two digits by `2` or `3`... but this wasn't the pattern.

After further investigation, I realised the random state was just to trick you, and that the moves used by the "robot" were exactly the same when the game was replayed.

```
Please choose: R / P / S
>>>s
You didn't win!
I chose R based on 2454155475
Please choose: R / P / S     
>>>r
You won! Consecutive wins: 1
I chose S based on 139951793
Please choose: R / P / S    
>>>p
You won! Consecutive wins: 2
I chose R based on 1842064464
Please choose: R / P / S     
>>>s
You won! Consecutive wins: 3
I chose P based on 2072586604
Please choose: R / P / S
>>>s
You didn't win!
I chose R based on 2482883256
Please choose: R / P / S
```

`R -> S -> R -> P -> R ...`, so we could technically script out a script based on the "robot's" input and play against it (since we can also scrap and save the original moves that the "robot" plays). The main logic which defeats it being:

```python

## codes to play a "test" round and save the moves of the robot
# ...

## actually defeating the robot by replaying the moves and using gameplay logic to defeat it
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
        print(review)
```

Feel free to check out [the script](./script.py) I put together to obtain the flag: `CTFlearn{r0ck_p4per_skiss0rs}`