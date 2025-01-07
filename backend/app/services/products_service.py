from app.models import Products


def get_all_products(page, per_page):
    products = Products.query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
        "per_page": products.per_page,
        "data": products.items,
    }
