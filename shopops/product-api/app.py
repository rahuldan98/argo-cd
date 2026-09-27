from fastapi import FastAPI

app = FastAPI(
    title="ShopOps Product API",
    version="1.0.0"
)

products = [
    {
        "id": 1,
        "name": "Kubernetes T-Shirt",
        "price": 999,
        "category": "DevOps"
    },
    {
        "id": 2,
        "name": "Docker Mug",
        "price": 499,
        "category": "DevOps"
    },
    {
        "id": 3,
        "name": "Cloud Engineer Hoodie",
        "price": 1499,
        "category": "Cloud"
    }
]


@app.get("/")
def root():
    return {
        "application": "ShopOps",
        "service": "Product API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "error": "Product not found"
    }
