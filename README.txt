# zenatix
----------------------------------------------------
User SignUp - Post
----------------------------------------------------
SignUp: URL: http://127.0.0.1:8000/spiceApp/user_signup_view/ 

Param= {
    "user_type": 1, 
    "email":"user@gmail.com", 
    "mobileNumber":7858588481, 
    "username":"user1", 
    "password":"user"
}
----------------------------------------------------
User Login - Post
----------------------------------------------------

2- Login: URL: http://127.0.0.1:8000/spiceApp/user_login_view/ 

{
    "email": "user@gmail.com", "password":"user"
}



----------------------------------------------------
Add Ingredient 
----------------------------------------------------
http://127.0.0.1:8000/zenatixTask/add_ingredient/
{
    "name": "milk",
    "quantity": 1,
    "unit"="kg" (this could be in liter or kg),
    "price"=100
}

--------------------------------------------------
Create Product from a list of ingredients 
---------------------------------------------------
http://127.0.0.1:8000/zenatixTask/add_product/
{
  "name":"Test 6",
  "ingredients":[{"id":2, "quantity":1, "unit":1}],
  "quantity":2,
  "selling_price":100
}

output- {
"message": "Product Created Successfully.",
"is_added": true
}

----------------------------------------------------
Get the detail of Product 
----------------------------------------------------
product details - GET http: //127.0.0.1:8000/zenatixTask/details_product/?id=16
    {
    "data": {
        "name": "Test 6",
        "quantity": 2,
        "selling_price": 100.0,
        "cost_price": 50.0,
        "ingredients_list": [ {
            "name": "eggs", "quantity": 1, "unit": "KG."
        }
        ]
    }
    ,
    "status": true,
    "message": "success."
}

----------------------------------------------------
Product Delete- DELETE
----------------------------------------------------
DELETE http: //127.0.0.1:8000/zenatixTask/details_product/?id=15
    {
    "status": true, "message": "Product Deleted."
}

----------------------------------------------------
Product Update- PUT
----------------------------------------------------
Product Update- PUT http: //127.0.0.1:8000/zenatixTask/details_product/?id=16
    {
    "name":"Test 6",
    "ingredients":[ {
        "id": 2, "quantity":2, "unit":2
    }
    ],
    "quantity":2,
    "selling_price":100
}

OUTPUT- {
    "message": "Product Updated Successfully.", "is_added": true
}

----------------------------------------------------
Product List- GET
----------------------------------------------------
Product List- GET http: //127.0.0.1:8000/zenatixTask/product_list/
    {
    "data": [ {
        "name": "Test 3", "quantity": 2, "selling_price": 100.0
    }
    ,
        {
        "name": "Test 4", "quantity": 2, "selling_price": 100.0
    }
    ,
        {
        "name": "Test 6", "quantity": 2, "selling_price": 100.0
    }
    ],
    "status": true
}
----------------------------------------------------
Place Order- POST
----------------------------------------------------
Place Order- POST http: //127.0.0.1:8000/zenatixTask/place_order/
    {
    "products":[ {
        "product_id": 16, "quantity":1
    }
    ]
}

output- {
    "bill": {
        "grand_price": 100.0,
        "products": [ {
            "product_id": 16, "quantity": 1, "selling_price": 100.0, "product_name": "Test 6"
        }
        ]
    }
    ,
    "message": "Order placed.",
    "status": false
}

----------------------------------------------------
Order History - GET
----------------------------------------------------
order-hstory- GET http: //127.0.0.1:8000/zenatixTask/history-order/?id=2
    {
    "data": {
        "customer":"user1",
        "grand_total":100.0,
        "products":"[{'product_id': 16, 'quantity': 1, 'selling_price': 100.0, 'product_name': 'Test 6'}]"
    }
    ,
    "message":"success"
}
