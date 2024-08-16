from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
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
            
            # # Fetch team
            test_obj = Testimonial.objects.all()
            test_serializer = TestimonialSerializer(
                test_obj, context={'request': request}, many=True).data

            context = {
                'info': info_serializer,
                'banners': banner_serializer,
                'featured': featured_serializer,
                'team': team_serializer,
                'testimonial': test_serializer,
            }

            # Render home page with contact info and banners
            return render(request, 'pages/home.html', context)
        except ObjectDoesNotExist:
            return render(request, 'pages/home.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


class AboutView(APIView):
    def get(self, request):
        try:
            return render(request, 'pages/about.html')
        except ObjectDoesNotExist:
            return render(request, 'pages/about.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


class HeadinginfoView(APIView):
    def get(self, request):
        try:
            info_obj = Contactinfo.objects.all()
            if not info_obj:
                raise ObjectDoesNotExist("No contact info found")

            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data
            context = {'info': info_serializer}
            return render(request, 'header.html', context)
        except ObjectDoesNotExist as e:
            return render(request, 'header.html', {'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        #     return Response(info_serializer, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No Banner found"}, status=status.HTTP_404_NOT_FOUND)


class BannerView(APIView):
    def get(self, request):
        try:
            banner_obj = Banner.objects.all()
            banner_serializer = BannerSerializer(
                banner_obj, many=True, context={'request': request}).data
            context = {'banners': banner_serializer}
            return render(request, 'core/banner.html', context=context)
        except ObjectDoesNotExist:
            return render(request, 'core/banner.html', {'error': "No banner found"}, status=status.HTTP_404_NOT_FOUND)


class FeaturedView(APIView):
    def get(self, request):
        try:
            featured_obj = Featured.objects.all()
            featured_serializer = FeaturedSerializer(
                featured_obj, many=True, context={'request': request}).data
            context = {'featured': featured_serializer}
            return render(request, 'core/banner.html', context)
        except ObjectDoesNotExist:
            return render(request, 'core/banner.html', {'error': "No featured found"}, status=status.HTTP_404_NOT_FOUND)


class ServiceView(APIView):
    def get(self, request):
        try:
            service_obj = Service.objects.all()
            service_serializer = ServiceSerializer(
                service_obj, many=True, context={'request': request}).data
        #     return Response(service_serializer, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No services found"}, status=status.HTTP_404_NOT_FOUND)
            context = {'services': service_serializer}
            return render(request, 'core/banner.html', context)
        except ObjectDoesNotExist:
            return render(request, 'core/banner.html', {'error': "No services found"}, status=status.HTTP_404_NOT_FOUND)


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
                # Show all products
                products = Productitem.objects.all()
                products_data = ProductitemSerializer(products, many=True).data
                context = {'products': products_data}
                return render(request, 'products/product_page.html', context)
            else:
                # Show only the first 10 products
                products = Productitem.objects.all()[:10]
                products_data = ProductitemSerializer(products, many=True).data
                context = {'products': products_data}
                return render(request, 'products/products.html', context)


class TestimonialView(APIView):
    def get(self, request):
        try:
            test_obj = Testimonial.objects.all()
            test_serializer = TestimonialSerializer(
                test_obj, context={'request': request}, many=True).data
            data = []
            for clients in test_serializer:
                item_obj = Clients.objects.all()
                clients['item'] = ClientsSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(clients)
        #     return Response(data, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No testimonial found"}, status=status.HTTP_404_NOT_FOUND)
            context = {'testimonial': data}
            return render(request, 'core/testimonials.html', context)
        except ObjectDoesNotExist:
            return render(request, 'core/testimonials.html', {'error': "No testimonials found"}, status=status.HTTP_404_NOT_FOUND)


class TeamView(APIView):
    def get(self, request):
        try:
            team_obj = Team.objects.all()
            team_serializer = TeamSerializer(
                team_obj, context={'request': request}, many=True).data
        #     return Response(team_serializer, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No services found"}, status=status.HTTP_404_NOT_FOUND)
            context = {'team': team_serializer}
            return render(request, 'core/team.html', context=context)
        except ObjectDoesNotExist:
            return render(request, 'core/team.html', {'error': "No team found"}, status=status.HTTP_404_NOT_FOUND)


class ContactView(APIView):
    def get(self, request):
        try:
            return render(request, 'pages/contact.html')
        except ObjectDoesNotExist:
            return render(request, 'pages/contact.html', {'error': "No content found"}, status=status.HTTP_404_NOT_FOUND)


