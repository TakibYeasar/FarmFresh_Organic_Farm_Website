from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import stripe

# Create your views here.


class MyCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = Cart.objects.get(customer=request.user, ordered=False)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "You do not have an active order"}, status=status.HTTP_404_NOT_FOUND)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            prod = Productitem.objects.get(id=product_id)
        except Productitem.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_prod = CartProduct.objects.get_or_create(
            product=prod, customer=request.user, ordered=False)

        cart = Cart.objects.filter(
            customer=request.user, complete=False).first()
        if cart is None:
            cart = Cart.objects.create(
                customer=request.user, total=0, complete=False)

        if cart.items.filter(product=cart_prod).exists():
            cart_prod.quantity += 1
            cart_prod.subtotal += cart_prod.price
            cart_prod.save()
        else:
            cart.items.add(cart_prod)

        cart.total += cart_prod.price
        cart.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            prod = Productitem.objects.get(id=product_id)
            cart = Cart.objects.get(customer=request.user, ordered=False)
            cart_prod = CartProduct.objects.get(
                product=prod, customer=request.user, ordered=False
            )
            cart.items.remove(cart_prod)
            cart.save()
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "You do not have an active order"}, status=status.HTTP_404_NOT_FOUND)
        except CartProduct.DoesNotExist:
            return Response({"error": "Item was not in your cart"}, status=status.HTTP_404_NOT_FOUND)
        except Productitem.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class RemoveSingleItemFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            prod = Productitem.objects.get(id=product_id)
            cart = Cart.objects.get(customer=request.user, ordered=False)
            cart_prod = CartProduct.objects.get(
                product=prod, customer=request.user, ordered=False
            )
            if cart_prod.quantity > 1:
                cart_prod.quantity -= 1
                cart_prod.subtotal -= cart_prod.price
                cart_prod.save()
                cart.total -= cart_prod.price
                cart.save()
            else:
                cart.items.remove(cart_prod)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "You do not have an active order"}, status=status.HTTP_404_NOT_FOUND)
        except CartProduct.DoesNotExist:
            return Response({"error": "Item was not in your cart"}, status=status.HTTP_404_NOT_FOUND)
        except Productitem.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class DeleteFullCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            cart = Cart.objects.get(customer=request.user, ordered=False)
            cart.delete()
            return Response({"message": "Cart deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"error": "You do not have any cart"}, status=status.HTTP_404_NOT_FOUND)


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({"error": "You do not have an active order"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            address_serializer = AddressSerializer(
                data=request.data)
            if address_serializer.is_valid():
                address_serializer.save(
                    user=request.user, address_type='B')
                order.address = address_serializer.instance
                order.save()
                payment_option = request.data.get('payment_option')
                if payment_option:
                    return Response({"redirect_url": "/core/payment/stripe"})
                else:
                    return Response({"error": "Invalid payment option selected"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"error": "You do not have an active order"}, status=status.HTTP_404_NOT_FOUND)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.get(user=request.user, ordered=False)
        if order.address:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            return Response({"error": "No billing address added"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            token = request.data.get('stripeToken')
            amount = int(order.get_total() * 100)
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token
            )

            payment = Payment.objects.create(
                stripe_charge_id=charge['id'],
                user=request.user,
                amount=order.get_total()
            )

            order.ordered = True
            order.payment = payment
            order.save()

            return Response({"message": "Order successful"}, status=status.HTTP_201_CREATED)

        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Log the error for debugging
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
