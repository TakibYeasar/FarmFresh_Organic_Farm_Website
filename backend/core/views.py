from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

# Create your views here.

class BannerView(APIView):
    def get(self, request):
        banner_obj = Banner.objects.all()
        banner_serializers = BannerSerializer(banner_obj, many=True, context={'request':request}).data
        return Response(banner_serializers)


class FeaturedView(APIView):
    def get(self, request):
        featured_obj = Featured.objects.all()
        featured_serializers = FeaturedSerializer(featured_obj, many=True, context={'request':request}).data
        return Response(featured_serializers)



class AboutView(APIView):
    def get(self, request):
        about_obj = About.objects.all()
        about_serializers = AboutSerializer(about_obj, many=True, context={'request':request}).data
        return Response(about_serializers)



class ServiceView(APIView):
    def get(self, request):
        service_obj = Service.objects.all()
        service_serializers = ServiceSerializer(service_obj, many=True, context={'request':request}).data
        return Response(service_serializers)



class WhychooseView(APIView):
    def get(self, request):
        service_obj = Whychoose.objects.all()
        service_serializers = WhychooseSerializer(service_obj, many=True, context={'request':request}).data
        return Response(service_serializers)



class ProductView(APIView):
    def get(self, request):
        service_obj = Product.objects.all()
        service_serializers = ProductSerializer(service_obj, many=True, context={'request':request}).data
        return Response(service_serializers)


class TestimonialView(APIView):
    def get(self, request):
        test_obj = Testimonial.objects.all()
        test_serializers = TestimonialSerializer(test_obj, many=True, context={'request':request}).data
        return Response(test_serializers)
    


class TeamView(APIView):
    def get(self, request):
        team_obj = Team.objects.all()
        team_serializers = TeamSerializer(team_obj, many=True, context={'request':request}).data
        return Response(team_serializers)





class ArticlescategoryView(APIView):
    def get(self, request):
        category_obj = Articlescategory.objects.all()
        category_serializers = ArticlescategorySerializer(category_obj, many=True, context={'request':request}).data
        return Response(category_serializers)



class ArticlestagView(APIView):
    def get(self, request):
        tag_obj = Articlestag.objects.all()
        tag_serializers = ArticlestagSerializer(tag_obj, many=True, context={'request':request}).data
        return Response(tag_serializers)


class ArticlesView(APIView):
    def get(self, request, pk):
        item_obj = Articles.objects.filter(id=pk)
        item_serializer = ArticlesSerializer(item_obj, many=True, context={'request':request}).data
        return Response(item_serializer)



class ArticleReviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        review_serializer = ArticleReviewSerializer(data=request.data)
        if review_serializer.is_valid():
            article = Articles.objects.filter(pk=id).first()
            if article:
                review_serializer.save(customer=request.customer, article=article)
                return Response(review_serializer.data , status=status.HTTP_200_OK)
            else:
                return Response({'error': "No product found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplayArticleReviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        review_serializer = ReplayArticleReviewSerializer(data=request.data)
        if review_serializer.is_valid():
            review = ArticleReview.objects.filter(pk=id).first()
            if review:
                review_serializer.save(customer=request.customer, review=review)
                return Response(review_serializer.data , status=status.HTTP_200_OK)
            else:
                return Response({'error': "No product found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ContactView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, format=None):
        data = self.request.data
        response = 'You will be contacted shortly.'

        try:
            send_mail(data['subject'],
                      'Name: ' + data['name'] + '\nEmail: ' + data['email'] +
                      '\n\nMessage:\n' + data['message'] + '\n\n' + response,
                      '19bcp101.nepal@gmail.com',
                      [data['email'], 'nothing3669@gmail.com'],
                      fail_silently=False)

            contact = Contact(name=data['name'],
                              email=data['email'],
                              subject=data['subject'],
                              message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'Message failed to send'})






