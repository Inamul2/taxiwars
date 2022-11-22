import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class createUser(APIView):
    def post(self, request):
        try:
            if request.user.is_authenticated:
                return Response({'Status': 'Failed',"Message": "Please logout before creating new user"}, status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get("username")
            password = request.data.get("password")        
            if not username or not password:
                return Response({'Status': 'Failed',"Message": "Please ensure that you are sending username and password"}, status=status.HTTP_403_FORBIDDEN)
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'Status': 'Success',"Message": f"User Created with username : {username}"}, status=status.HTTP_200_OK)
            else:
                return Response({'Status': 'Failed',"Message": "User wasn't authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except:
                return Response({'Status': 'Failed', "Message": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class updateUser(APIView):
    def post(self, request):
        try:
            if not request.user.is_authenticated:
                return Response({'Status': 'Failed',"Message": "Please login before updating user"}, status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get("username")
            u = User.objects.get(username=username)
            if not u:
                return Response({'Status': 'Failed',"Message": f"{username} doesn't exists"}, status=status.HTTP_403_FORBIDDEN)
            u.set_password('new password')
            u.save()
            return Response({'Status': 'Success',"Message": f"{username} updated successfully"}, status=status.HTTP_200_OK)
            
        except:
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class loginUser(APIView):
    def post(self, request):
        try:
            if request.user.is_authenticated:
                return Response({'Status': 'Failed',"Message": "Please logout before login to new user"}, status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get("username")
            password = request.data.get("password")        
            if not username or not password:
                return Response({'Status': 'Failed',"Message": "Please ensure that you are sending username and password"}, status=status.HTTP_403_FORBIDDEN)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'Status': 'Success',"Message": f"{username} login successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({'Status': 'Failed',"Message": "User wasn't authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        except:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class logoutUser(APIView):
    def get(self, request):
        try:
            if request.user.is_authenticated:
                logout(request)
                return Response({'Status': 'Success',"Message": "Logged Out Successfully"}, status=status.HTTP_200_OK)
            return Response({'Status': 'Failed',"Message": "Please login before accessing logout"}, status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class deleteUser(APIView):
    def post(self, request):
        try:
            if request.user.is_authenticated:
                u = User.objects.get(username = request.user.username)
                logout(request)
                u.delete()
                return Response({'Status': 'Success',"Message": "User Deleted Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({'Status': 'Failed',"Message": "Please login before deleting user"}, status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
