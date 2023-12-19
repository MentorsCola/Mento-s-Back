from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nicknames.models import Nicknames


class NicknameView(APIView):
    def get(self, request):
        all_nickname = Nicknames.objects.all()
        print(len(all_nickname))
        list = []
        for i in all_nickname:
            list.append({"id": i.id, "name": i.names})
        return Response(list, status=status.HTTP_200_OK)