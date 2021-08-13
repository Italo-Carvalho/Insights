from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import viewsets

app_name = "api"

urlpatterns = [ 
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tags/', viewsets.TagsViewsetsC.as_view(), name='tags_c'),
    path('tags/<int:pk>/', viewsets.TagsViewsetsRUD.as_view(), name='tags_rud'),
    path('card/<int:pk>/', viewsets.CardViewsetsRUD.as_view(), name='card_rud'),
    path('card/', viewsets.CardViewsetsLC.as_view(), name='card_lc'),
    path('user/', viewsets.UserCreateAPIView.as_view(), name='user'),

]
