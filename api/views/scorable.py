from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from django.db.models import ObjectDoesNotExist
from api.permissions import IsAuthenticatedAndNotOwner
from api.serializers.dish.dish_score import DishScoreSerializer
from api.error import Error


class Scorable:
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticatedAndNotOwner])
    def rate(self, request, pk=None):
        obj = self.get_object()
        new_score = request.data.get('score')

        if obj is None or new_score is None:
            return HttpResponseBadRequest(Error.DataNotValid)

        try:
            score = obj.scores.get(user_id=request.user.id)

            data = {
                'value': new_score
            }

            serializer = self.score_serializer(score, data=data, partial=True)
        except ObjectDoesNotExist:
            data = {
                'user': request.user.id,
                'value': new_score,
                'object': obj.id
            }

            serializer = self.score_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(self.get_serializer(obj).data)
