from core.user.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


@api_view(['POST'])
def reset_password(request):
    if not IsAdminUser().has_permission(request, reset_password):
        return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    user_id = request.data.get('user_id')
    new_password = request.data.get('new_password')
    if new_password is not None and user_id is not None:
        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'detail': 'Unknown user'}, status=status.HTTP_400_BAD_REQUEST)