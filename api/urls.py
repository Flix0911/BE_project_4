from django.urls import path
from . import views

urlpatterns = [
    # view plates
    path("plates/", views.PlateListCreate.as_view(), name="plate-list"),  
    # delete plates
    path("plates/delete/<int:pk>/", views.PlateDelete.as_view(), name="delete-plate"),
    # view 1 plate by id
    path("plates/show/<int:pk>/", views.PlateView.as_view(), name="view-plate"),

    # view cups
    path("cups/", views.CupListCreate.as_view(), name="cup-list"),
    # delete cups
    path("cups/delete/<int:pk>/", views.CupDelete.as_view(), name="delete=cup"),
    # view 1 cup by id
    path("cups/show/<int:pk>/", views.CupView.as_view(), name="view-cup"),
]
