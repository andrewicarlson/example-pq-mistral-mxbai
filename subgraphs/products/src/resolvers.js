const resolvers = {
  Query: {
    products: (_, __, {dataSources}) => {
      return dataSources.productsAPI.getProducts();
    },
    product: (_, { product_name }, { dataSources }) => {
      return dataSources.productsAPI.getProduct(product_name);
    },
  }
};

export default resolvers;
