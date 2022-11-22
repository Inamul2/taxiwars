# taxiwars

It has the following api's with corresponding input and output format.

- USER APP API'S

- http://127.0.0.1:8000/user/create/ :
- It's a Post Call
  input format = {"username" : "test", "password" : "123456789"}
  output format = {
    "Status": "Success",
    "Message": "User Created with username : testing"
}

- http://127.0.0.1:8000/user/update/
- It's a Post Call, It can be only accesses when the user is logged in , for now it can only change the current user password, it will log you out after changing the password, you need to loging again with the new password
  input format = {"new_password" : "1234"}
  output format = {
    "Status": "Success",
    "Message": "testing updated successfully"
}


- http://127.0.0.1:8000/user/login/
- It's a Post Call, which takes username and password
 input format = {"username" : "testing", "password":"1234"}
 output format = {
    "Status": "Success",
    "Message": "testing login successfully"
}

- http://127.0.0.1:8000/user/logout/
- It's a GET call, when ever it's been hit, current user will automatically log out.
output format = {
    "Status": "Success",
    "Message": "Logged Out Successfully"
}


- http://127.0.0.1:8000/user/delete/
- It's also a GET call, when hit it will delete the current user.
 output format = {
    "Status": "Success",
    "Message": "testing has been deleted Successfully"
}


- GAME APP API'S
It only works when user is logged in 

- http://127.0.0.1:8000/game/create/
- It's a GET call, which will create a game when hit.
  output = {
    "Status": "Success",
    "Message": "Game Created Successfully",
    "Game ID": 11
}


- http://127.0.0.1:8000/game/getBoard/
- It's a POST Call, it takes gameId for getting the status of game.
 input = {"gameId" : 6}
 output = {
    "Status": "Success",
    "Message": "Game data retrieved successfully",
    "Game ID": 6,
    "Value": "abbbba"
}
input = {"gameId" : "10"}
output = {
    "Status": "Success",
    "Message": "Game data retrieved successfully",
    "Game ID": 10,
    "Value": ""
}


- http://127.0.0.1:8000/game/updateBoard/
- It's a POST call, which takes gameId and also the value to be added
 input = {"gameId" : "10", "value" : "c"}
 output = {
    "Status": "Success",
    "Message": "Game board updated successfully",
    "Game ID": "10",
    "Value": "c"
}

input = {"gameId" : "6", "value" : "c"}
output = {
    "Status": "Success",
    "Message": "Value for game id 6 is palindrome : abbbba"
}


- http://127.0.0.1:8000/game/listBoards/
- It's a GET call, user can see all the games and there values
  output = {
    "Status": "Success",
    "Message": "List of Game retrieved Successfully",
    "Games": [
        {
            "ID": 1,
            "value": ""
        },
        {
            "ID": 2,
            "value": ""
        },
        {
            "ID": 3,
            "value": ""
        },
        {
            "ID": 4,
            "value": ""
        },
        {
            "ID": 5,
            "value": ""
        },
        {
            "ID": 6,
            "value": "abbbba"
        },
        {
            "ID": 7,
            "value": ""
        },
        {
            "ID": 8,
            "value": ""
        },
        {
            "ID": 9,
            "value": ""
        },
        {
            "ID": 10,
            "value": "c"
        },
        {
            "ID": 11,
            "value": ""
        }
    ]
}

