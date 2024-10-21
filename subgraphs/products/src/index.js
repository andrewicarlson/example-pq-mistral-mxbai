import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";
import { buildSubgraphSchema } from "@apollo/subgraph";
import { readFileSync } from "fs";
import gql from "graphql-tag";

import resolvers from "./resolvers.js";
import ProductsAPI from "./datasources/api.js";

const typeDefs = gql(readFileSync('./src/schema/products.graphql', { encoding: 'utf-8' }));

const server = new ApolloServer({
  schema: buildSubgraphSchema({ typeDefs, resolvers }),
});

const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 },
  context: async () => {
    return {
      dataSources: {
        productsAPI: new ProductsAPI()
      }
    }
  }
});

console.log(`🚀  Server ready at: ${url}`);
