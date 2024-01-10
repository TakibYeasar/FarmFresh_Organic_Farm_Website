from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryView(APIView):
    def get(self, request):
        try:
            cat_obj = Category.objects.all()
            cat_serializers = CategorySerializer(
                cat_obj, many=True, context={'request': request}).data
            return Response(cat_serializers, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No category found"}, status=status.HTTP_404_NOT_FOUND)
    
class GetProductView(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        if product_id:
            try:
                product = Productitem.objects.get(id=product_id)
                category = product.category.all().values_list('name', flat=True)
                reviews = Review.objects.filter(product=product)
                serializer = ProductitemSerializer(product)
                serializer.data['category'] = list(category)
                serializer.data['reviews'] = [{'comment': review.comment_field, 'rating': review.rating} for review in reviews]
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': "No product found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = Products.objects.all()
            products_data = ProductsSerializer(products, many=True).data
            return Response(data=products_data, status=status.HTTP_200_OK)


class ProductByCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category):
        try:
            products_in_category = Products.objects.filter(categories__name=category)
            if products_in_category.exists():
                serializer = ProductitemSerializer(products_in_category, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': 'No products found in this category'}, status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class CreateReviewProduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            product = Productitem.objects.get(id=product_id)
            serializer = ReviewProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, product=product)
                return Response({'message': 'Review created successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Productitem.DoesNotExist:
            return Response({'error': 'No product found'}, status=status.HTTP_404_NOT_FOUND)


class GetReviewProducts(APIView):
    def get(self, request, product_id):
        try:
            product = Productitem.objects.get(id=product_id)
            review_products = Review.objects.filter(product=product)
            serializer = ReviewProductSerializer(review_products, many=True)
            return Response(serializer.data)
        except Productitem.DoesNotExist:
            return Response({'error': 'No product found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateReviewProduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, review_product_id):
        try:
            review_product = Review.objects.get(id=review_product_id)
            if review_product.user.id != request.user.id:
                return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
            serializer = ReviewProductSerializer(
                review_product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Review updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error': 'No review found'}, status=status.HTTP_404_NOT_FOUND)


class DeleteReviewProduct(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, review_product_id):
        try:
            review_product = Review.objects.get(id=review_product_id)
            if review_product.user.id == request.user.id:
                review_product.delete()
                return Response({'msg': 'Review deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response({'error': 'No review found'}, status=status.HTTP_404_NOT_FOUND)
