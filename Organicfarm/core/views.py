from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from articles.models import *
from articles.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        try:
            # Fetch contact information
            info_obj = Contactinfo.objects.all()
            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data

            # Fetch banners
            featured_obj = Featured.objects.all()
            featured_serializer = FeaturedSerializer(
                featured_obj, many=True, context={'request': request}).data
            
            # Fetch featured
            banner_obj = Banner.objects.all()
            banner_serializer = BannerSerializer(
                banner_obj, many=True, context={'request': request}).data
            
            # # Fetch team
            team_obj = Team.objects.all()
            team_serializer = TeamSerializer(
                team_obj, context={'request': request}, many=True).data
            
            # # Fetch testimonial
            test_obj = Testimonial.objects.all()
            test_serializer = TestimonialSerializer(
                test_obj, context={'request': request}, many=True).data
            
            # # Fetch products
            products = Productitem.objects.all()[:5]
            products_data = ProductitemSerializer(products, many=True).data
            
            # # Fetch products
            articles = Article.objects.all()[:5]
            articles_data = ArticlesSerializer(articles, many=True).data

            context = {
                'info': info_serializer,
                'banners': banner_serializer,
                'featured': featured_serializer,
                'team': team_serializer,
                'testimonial': test_serializer,
                'products': products_data,
                'articles': articles_data,
            }
            
            return render(request, 'pages/home.html', context)
        except ObjectDoesNotExist:
            return render(request, 'pages/home.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


class AboutView(APIView):
    def get(self, request):
        try:
            # Fetch contact information
            info_obj = Contactinfo.objects.all()
            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data

            # # Fetch team
            team_obj = Team.objects.all()
            team_serializer = TeamSerializer(
                team_obj, context={'request': request}, many=True).data

            
            context = {
                'info': info_serializer,
                'team': team_serializer,
            }

            return render(request, 'pages/about.html', context)
        except ObjectDoesNotExist:
            return render(request, 'pages/about.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


class GetProductView(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')

        if product_id:
            try:
                product = Productitem.objects.get(id=product_id)
                product_serializer = ProductitemSerializer(product).data
                context = {'product': product_serializer}
                return render(request, 'products/product_details.html', context)
            except Productitem.DoesNotExist:
                return render(request, 'products/product_details.html', {'error': "No product found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Check if the user wants to see all products
            show_all = request.GET.get('show_all', False)

            if show_all:
                
                # fetch heading info
                info_obj = Contactinfo.objects.all()
                info_serializer = ContactinfoSerializer(
                    info_obj, many=True, context={'request': request}).data
                
                # Show all products
                products = Productitem.objects.all()
                products_data = ProductitemSerializer(products, many=True).data
                
                
                context = {
                    'info': info_serializer,
                    'products': products_data,
                    }
                
                
                return render(request, 'products/product_page.html', context)

class ContactView(APIView):
    def get(self, request):
        try:
            # Fetch contact information
            info_obj = Contactinfo.objects.all()
            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data
            
            context = {
                'info': info_serializer,
            }
            
            
            return render(request, 'pages/contact.html', context)
        except ObjectDoesNotExist:
            return render(request, 'pages/contact.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


