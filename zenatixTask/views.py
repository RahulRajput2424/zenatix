import datetime
from rest_framework import  generics
from rest_framework.views import APIView
from rest_framework.response import Response
from zenatixTask.models import *
from rest_framework.authtoken.models import Token
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import  login
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from zenatixTask.serializers import *

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            return Response(response, status=status.HTTP_200_OK)
        else:
            error_data = serializer.errors
            return Response(data=error_data)

class AddIngredient(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = IngredientSerializer


class AddProduct(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        data = request.data
        name = data.get("name")
        ingredients = data.get("ingredients")
        cost_price = 0
        for i in ingredients:
            ingredient_id = i.get("id", 0)
            try:
                obj = Ingredient.objects.get(id=ingredient_id)
            except:
                response = {"message":"Ingredient does not exists.", "is_added":False}
                return Response(response, status=200)
            i_quantity = i.get("quantity", 0)
            if i_quantity > obj.quantity or i_quantity == 0:
                response = {"message":"Quantity can not be greater than Ingredient's available quantity or zero.", "is_added":False}
                return Response(response, status=200)
            i_price = obj.price * i_quantity
            cost_price = cost_price + i_price
        quantity = data.get("quantity", 0)
        cost_price = cost_price * quantity
        selling_price = data.get("selling_price")
        if cost_price > selling_price:
            response = {"message":"Cost price can not be greater than selling price.", "is_added":False}
            return Response(response, status=200)
        serializer_data = {"name":name, "quantity":quantity, "selling_price":selling_price, "cost_price":cost_price}

        serializer = ProductSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            return Response(serializer.errors)

        for i in ingredients:
            obj = IngredientProduct.objects.create(ingredients_id=i.get("id"), quantity=i.get("quantity"), product_id=data.get("id"))
            obj.save()
            i_obj = Ingredient.objects.get(id=i.get("id"))
            i_obj.quantity = i_obj.quantity - i.get("quantity")
            i_obj.save()
        response = {"message":"Product Created Successfully.", "is_added":True}
        return Response(response, status=200)

class ProductDetails(APIView):

    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        pk = request.query_params.get("id")

        try:
            obj = Product.objects.get(id=pk)
        except:
            response = {"message":"Product dose not exists.", "status":False, "data":{}}
            return Response(response, status=200)

        ingredients = IngredientProduct.objects.filter(product_id=pk)
        ingredients_list = []
        for i in ingredients:
            ingredients_dict = {}
            ingredients_dict["name"] = i.ingredients.name
            ingredients_dict["quantity"] = i.quantity
            if i.ingredients.unit == 1:
                unit = "KG."
            else:
                unit = "liter"
            ingredients_dict["unit"] = unit

            ingredients_list.append(ingredients_dict)
        details = {"name":obj.name, "quantity":obj.quantity, "selling_price":obj.selling_price, "cost_price":obj.cost_price,
                    "ingredients_list":ingredients_list}
        response = {"data":details, "status":True , "message":"success."}
        return Response(response, status=200)

    def delete(self, request):
        pk = request.query_params.get("id")

        try:
            obj = Product.objects.get(id=pk)
        except:
            response = {"message":"Product dose not exists.", "status":False}
            return Response(response, status=200)
        obj.delete()
        response = {"status":True , "message":"Product Deleted."}
        return Response(response, status=200)

    def put(self, request):
        pk = request.query_params.get("id")

        try:
            instance = Product.objects.get(id=pk)
        except:
            response = {"message":"Product dose not exists.", "status":False}
            return Response(response, status=200)

        data = request.data
        name = data.get("name")
        ingredients = data.get("ingredients")
        cost_price = 0
        for i in ingredients:
            ingredient_id = i.get("id", 0)
            try:
                obj = Ingredient.objects.get(id=ingredient_id)
            except:
                response = {"message":"Ingredient does not exists.", "is_added":False}
                return Response(response, status=200)
            i_quantity = i.get("quantity", 0)
            if i_quantity > obj.quantity:
                response = {"message":"Quantity can not be greater than Ingredient's available quantity.", "is_added":False}
                return Response(response, status=200)
            i_price = obj.price * i_quantity
            cost_price = cost_price + i_price
        quantity = data.get("quantity", 0)
        cost_price = cost_price * quantity
        selling_price = data.get("selling_price")
        if cost_price > selling_price:
            response = {"message":"Cost price can not be greater than selling price.", "is_added":False}
            return Response(response, status=200)
        serializer_data = {"name":name, "quantity":quantity, "selling_price":selling_price, "cost_price":cost_price}

        serializer = ProductSerializer(instance, serializer_data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            return Response(serializer.errors)

        IngredientProduct.objects.filter(product_id=pk).delete()

        for i in ingredients:
            obj = IngredientProduct.objects.create(ingredients_id=i.get("id"), quantity=i.get("quantity"), product_id=data.get("id"))
            obj.save()
            i_obj = Ingredient.objects.get(id=i.get("id"))
            i_obj.quantity = i_obj.quantity - i.get("quantity")
            i_obj.save()
        response = {"message":"Product Updated Successfully.", "is_added":True}
        return Response(response, status=200)


class ProductList(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):

        obj = Product.objects.all()
        data_list = []

        for o in obj:
            data_dict = {}
            data_dict["name"] = o.name
            data_dict["quantity"] = o.quantity
            data_dict["selling_price"] = o.selling_price
            data_list.append(data_dict)

        response = {"data":data_list, "status":True}
        return Response(response, status=200)


class PlaceOrder(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user_id = request.user.id
        username = request.user.username

        if request.user.is_superuser:
            response = {"message":"Admin user don't have place order permission.", "status":False}
            return Response(response, status=200)
        else:
            products = request.data.get("products", [])
            total_price = 0
            for p in products:
                try:
                    p_obj = Product.objects.get(id=p.get("product_id", 0))
                except:
                    response = {"message":"Product does not exists.", "status":False}
                    return Response(response, status=200)

                if p.get("quantity", 0) > p_obj.quantity or p.get("quantity", 0) == 0:
                    response = {"message":"Quantity can not be greater than available quantity or zero.", "is_added":False}
                    return Response(response, status=200)

                selling_price = p_obj.selling_price * p.get("quantity", 0)
                p["selling_price"] = p_obj.selling_price
                p["product_name"] = p_obj.name
                total_price = total_price + selling_price
            response = {"bill":{"grand_price":total_price, "products":products}, "message":"Order placed.", "status":False}
            serializer_data = {"customer":username, "grand_total":total_price, "products":str(products)}
            serializer = OrderSerializer(data=serializer_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors)

            ## remove quantity
            for p in products:
                p_obj = Product.objects.get(id=p.get("product_id", 0))
                p_obj.quantity = p_obj.quantity - p.get("quantity", 0)
                p_obj.save()
            return Response(response, status=200)

class OrderDetailsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        pk = request.query_params.get("id")
        try:
            obj = OrderDetails.objects.get(id=pk)
        except:
            response = {"message":"order does not exists,", "status":200}
            return Response(response, status=200)

        details = {"customer":obj.customer, "grand_total":obj.grand_total, "products":obj.products}
        response = {"data":details, "message":"success"}
        return Response(response, status=200)







