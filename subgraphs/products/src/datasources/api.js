import products from "./data.json" assert { type: "json" };

class ProductsAPI {
    getProduct(product_name) {
        return products.find(product => product.name.toLowerCase().indexOf(product_name.toLowerCase()) > -1);
    }

    getProducts() {
        return products;
    }
}

export default ProductsAPI;