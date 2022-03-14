from typing import Optional, List
from fastapi import APIRouter, Cookie, Header, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

products = ["watch", "camera", "phone"]


@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get("/all")
def get_all_products():
    # return products
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/withheader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
):
    if custom_header:
        response.headers['custom-response-header'] = ", ".join(custom_header)
    return {
        "data": products,
        "header": custom_header,
        "cookie": test_cookie
    }


@ router.get("/{id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns the HTML for product object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not found"
            }
        },
        "description": "A plaintext error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")

    product = products[id]
    out = f"""
    <head>
        <style>
            .product {{
                width: 500px;
                height: 300px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="product">
            {product}
        </div>
    </body>
    """

    return HTMLResponse(content=out, media_type="text/html")
