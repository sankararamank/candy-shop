from rest_framework import viewsets
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()

        user = self.request.query_params.get("user", None)
        product = self.request.query_params.get("product", None)

        if user is not None:
            queryset = queryset.filter(user=user)

        if product is not None:
            queryset = queryset.filter(product=product)

        return queryset
