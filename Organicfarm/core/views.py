from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        return render(request, 'home.html')


class HeadinginfoView(APIView):
    def get(self, request):
        try:
            info_obj = Contactinfo.objects.all()
            if not info_obj:
                raise ObjectDoesNotExist("No contact info found")

            info_serializer = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data
        #     return Response(info_serializer, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No contact info found"}, status=status.HTTP_404_NOT_FOUND)
            context = {'info': info_serializer}
            return render(request, 'core/header.html', context)
        except ObjectDoesNotExist as e:
            return render(request, 'core/header.html', {'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


class BannerView(APIView):
    def get(self, request):
        try:
            banner_obj = Banner.objects.all()
            banner_serializer = BannerSerializer(
                banner_obj, many=True, context={'request': request}).data
        #     return Response(banner_serializer, status=status.HTTP_200_OK)
        # except ObjectDoesNotExist:
        #     return Response({'error': "No banner found"}, status=status.HTTP_404_NOT_FOUND)
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
            return Response(featured_serializer, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No featured found"}, status=status.HTTP_404_NOT_FOUND)
        #     context = {'featured': featured_serializer}
        #     return render(request, 'core/banner.html', context)
        # except ObjectDoesNotExist:
        #     return render(request, 'core/banner.html', {'error': "No featured found"}, status=status.HTTP_404_NOT_FOUND)


class AboutView(APIView):
    def get(self, request):
        try:
            about_obj = About.objects.all()
            about_serializer = AboutSerializer(
                about_obj, context={'request': request}, many=True).data
            data = []
            for items in about_serializer:
                item_obj = Aboutitem.objects.all()
                items['item'] = AboutitemSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(items)
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No about info found"}, status=status.HTTP_404_NOT_FOUND)
        #     context = {'about': data}
        #     return render(request, 'core/about.html', context)
        # except ObjectDoesNotExist:
        #     return render(request, 'core/about.html', {'error': "No about found"}, status=status.HTTP_404_NOT_FOUND)


class ServiceView(APIView):
    def get(self, request):
        try:
            service_obj = Service.objects.all()
            service_serializer = ServiceSerializer(
                service_obj, context={'request': request}, many=True).data
            data = []
            for items in service_serializer:
                item_obj = Serviceitem.objects.all()
                items['item'] = ServiceitemSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(items)
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No service found"}, status=status.HTTP_404_NOT_FOUND)


class WhychooseView(APIView):
    def get(self, request):
        try:
            whychoose_obj = Whychoose.objects.all()
            whychoose_serializer = WhychooseSerializer(
                whychoose_obj, context={'request': request}, many=True).data
            data = []
            for whychoose in whychoose_serializer:
                item_obj = Whychooseitem.objects.all()
                whychoose['item'] = WhychooseitemSerializer(
                    item_obj, context={'request': request}, many=True).data
                data.append(whychoose)
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No why choose found"}, status=status.HTTP_404_NOT_FOUND)
        #     context = {'whychoose': data}
        #     return render(request, 'core/features.html', context)
        # except ObjectDoesNotExist:
        #     return render(request, 'core/features.html', {'error': "No features found"}, status=status.HTTP_404_NOT_FOUND)


class GetProductView(APIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        if product_id:
            try:
                product = Productitem.objects.get(id=product_id)
                serializer = ProductitemSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': "No product found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = Productitem.objects.all()
            products_data = ProductitemSerializer(products, many=True).data
            return Response(data=products_data, status=status.HTTP_200_OK)


class ProductsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            products = Products.objects.all()
            products_serializer = ProductsSerializer(products, many=True).data
            # data = []
            # for product in products_serializer:
            #     item_obj = Productitem.objects.all()
            #     product['item'] = ProductitemSerializer(
            #         item_obj, context={'request': request}, many=True).data
            #     data.append(product)
            return Response(products_serializer, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No service found"}, status=status.HTTP_404_NOT_FOUND)


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
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No testimonial found"}, status=status.HTTP_404_NOT_FOUND)
        #     context = {'testimonial': data}
        #     return render(request, 'core/testimonials.html', context)
        # except ObjectDoesNotExist:
        #     return render(request, 'core/testimonials.html', {'error': "No testimonials found"}, status=status.HTTP_404_NOT_FOUND)


class TeamView(APIView):
    def get(self, request):
        try:
            team_obj = Team.objects.all()
            team_serializer = TeamSerializer(
                team_obj, context={'request': request}, many=True).data
            # context = {'team': team_serializer}
            return Response(team_serializer, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No testimonial found"}, status=status.HTTP_404_NOT_FOUND)
        #     return render(request, 'core/team.html', context=context)
        # except ObjectDoesNotExist:
        #     return render(request, 'core/team.html', {'error': "No team found"}, status=status.HTTP_404_NOT_FOUND)
