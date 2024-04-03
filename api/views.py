# import user from django
from django.contrib.auth.models import User
# from rest
from rest_framework import generics
# import serializer
from .serializers import UserSerializer, PlateSerializer, CupSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Plate, Cup

# view for creating new Plate
class PlateListCreate(generics.ListCreateAPIView):
    serializer_class = PlateSerializer
    # to hit this view, you must be authenticated
    permission_classes = [IsAuthenticated]
    
    # get the user in the view ~ get user object and then get those plates
    def get_queryset(self):
        user = self.request.user
        # filter by the user
        return Plate.objects.filter(owner=user)
    
    # perform create ~ need to override certain methods
    # when we pass serializer data, will check if valid or note
    def perform_create(self, serializer):
        # manually check if valid
        if serializer.is_valid():
            # save serializer, and will make a new version of the plate, and add the owner which is read only
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)
            
# delete a plate
class PlateDelete(generics.DestroyAPIView):
    serializer_class = PlateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Plate.objects.filter(owner=user)

# view a plate by :id
class PlateView(generics.RetrieveAPIView):
    # serialize
    serializer_class = PlateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Plate.objects.filter(owner=user)

# update a plate by :id
class UpdatePlateView(generics.UpdateAPIView):
    # serialize
    serializer_class = PlateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Plate.objects.filter(owner=user)

# ---------------CUP
    
# view for Cup
class CupListCreate(generics.ListCreateAPIView):
    # use the serializer
    serializer_class = CupSerializer
    # to get to this, must be authenticated
    permission_classes = [IsAuthenticated]
    
    # get the cups tied to the user
    def get_queryset(self):
        # get the request object
        user = self.request.user
        # filter by the user
        return Cup.objects.filter(owner=user)
    
    # perform create ~ override certain methods
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            print(serializer.errors)

# Delete a cup
class CupDelete(generics.DestroyAPIView):
    serializer_class = CupSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Cup.objects.filter(owner=user)
    
# view a cup by id
class CupView(generics.RetrieveAPIView):
    serializer_class = CupSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Cup.objects.filter(owner=user)
    
# update a cup by id
class UpdateCupView(generics.UpdateAPIView):
    serializer_class = CupSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Cup.objects.filter(owner=user)
    


# --------------USER

# create user view
# Below is built into django 
class CreateUserView(generics.CreateAPIView):
    # list of all the different objects that we'll look at
    queryset = User.objects.all()
    # tells view to accept certain data
    serializer_class = UserSerializer
    # who can call this, and anyone can do it
    permission_classes = [AllowAny]
