from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.renderers import TemplateHTMLRenderer


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response()

class ContactinfoView(APIView):
    def get(self, request):
        try:
            info_obj = Contactinfo.objects.all()
            info_serializers = ContactinfoSerializer(
                info_obj, many=True, context={'request': request}).data
            return Response(info_serializers, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No contact info found"}, status=status.HTTP_404_NOT_FOUND)


class BannerView(APIView):
    def get(self, request):
        try:
            banner_obj = Banner.objects.all()
            banner_serializers = BannerSerializer(
                banner_obj, many=True, context={'request': request}).data
            return Response(banner_serializers, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No banner found"}, status=status.HTTP_404_NOT_FOUND)


class FeaturedView(APIView):
    def get(self, request):
        try:
            Featured_obj = Featured.objects.all()
            Featured_serializers = FeaturedSerializer(
                Featured_obj, many=True, context={'request': request}).data
            return Response(Featured_serializers, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No service found"}, status=status.HTTP_404_NOT_FOUND)


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
            return Response({'error': "No about found"}, status=status.HTTP_404_NOT_FOUND)


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
            return Response({'error': "No whychoose found"}, status=status.HTTP_404_NOT_FOUND)


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


class TeamView(APIView):
    def get(self, request):
        try:
            Team_obj = Team.objects.all()
            Team_serializer = TeamSerializer(
                Team_obj, context={'request': request}, many=True).data
            return Response(Team_serializer, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': "No team found"}, status=status.HTTP_404_NOT_FOUND)

