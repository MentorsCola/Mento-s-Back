
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Nicknames

class NicknameView(APIView):
    def get(self, request):
        all_nickname = Nicknames.objects.all()
        print(len(all_nickname))
        list = []
        for i in all_nickname:
            # print(i)
            list.append({"id": i.id, "names": i.names})
        # if all_nickname:
        #     return Response(all_nickname, status=status.HTTP_200_OK)
        return Response(list, status=status.HTTP_200_OK)