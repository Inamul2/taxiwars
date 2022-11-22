import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GameData
from .serializers import GameDataSerializer


class createBoard(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                game = GameData.objects.create(value="")
                serialize = GameDataSerializer(game)
                return Response({'Status': 'Success', "Message": "Game Created Successfully", "Game ID": serialize.data['ID']},
                                status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"Warning": "Please Login first to access the API"}, status=status.HTTP_403_FORBIDDEN)


class getBoard(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                if request.data.get("gameId"):
                    gameId = request.data["gameId"]
                    value = list(GameData.objects.filter(ID=gameId).values())
                    if value:
                        return Response({'Status': 'Success', "Message": "Game data retrieved successfully", "Game ID": value[0]['ID'], "Value": value[0]['value']},
                                        status=status.HTTP_200_OK)
                    return Response({'Status': 'Failed', "Message": "Invalid Game Id"},
                                    status=status.HTTP_404_NOT_FOUND)
                return Response({'Status': 'Failed', "Message": "Game Id needed"},
                                status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"Warning": "Please Login first to access the API"}, status=status.HTTP_403_FORBIDDEN)


class updateBoard(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                if request.data.get("gameId"):
                    if not request.data.get("value"):
                        return Response({'Status': 'Failed', "Error": "Value is required for updating the board"}, status=status.HTTP_404_NOT_FOUND)
                    gameId = request.data["gameId"]
                    value = request.data["value"]
                    query = GameData.objects.get(ID=gameId)
                    if query:
                        if len(query.value) < 6:
                            k = query.value + value
                            query.value += value
                            query.save()
                            if len(k) == 6:
                                if query.value == query.value[::-1]:
                                    return Response({'Status': 'Success', "Message": f"Value for game id {gameId} is palindrome : {query.value}"},
                                                    status=status.HTTP_200_OK)
                                return Response({'Status': 'Success', "Message": f"Value for game id {gameId} is not palindrome : {query.value}"},
                                                status=status.HTTP_200_OK)
                            return Response({'Status': 'Success', "Message": "Game board updated successfully", "Game ID": gameId, "Value": k},
                                            status=status.HTTP_200_OK)
                        else:
                            if query.value == query.value[::-1]:
                                return Response({'Status': 'Success', "Message": f"Value for game id {gameId} is palindrome : {query.value}"},
                                                status=status.HTTP_200_OK)
                            return Response({'Status': 'Success', "Message": f"Value for game id {gameId} is not palindrome : {query.value}"},
                                            status=status.HTTP_200_OK)
                    return Response({'Status': 'Failed', "Message": "Invalid Game Id"},
                                    status=status.HTTP_404_NOT_FOUND)
                return Response({'Status': 'Failed', "Message": "Game Id needed"},
                                status=status.HTTP_400_BAD_REQUEST)

            except:
                return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"Warning": "Please Login first to access the API"}, status=status.HTTP_403_FORBIDDEN)


class listBoard(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                data = GameData.objects.all().order_by('ID')
                serialize = GameDataSerializer(data, many=True)
                return Response({'Status': 'Success', "Message": "List of Game retrieved Successfully",
                                "Games": serialize.data}, status=status.HTTP_200_OK)
            except:
                return Response({'Status': 'Failed', "Message": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"Warning": "Please Login first to access the API"}, status=status.HTTP_403_FORBIDDEN)
