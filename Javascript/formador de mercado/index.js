// AlgoTrading Formador de mercado em JS.
// By: Lucas Eduardo
// 2022


const axios = require('axios');
const crypto = require('crypto-js');
const dotenv = require('dotenv');

dotenv.config();

async function main() {

  // LCarregar chaves de API de variáveis ​​de ambiente
  const API_KEY = process.env.API_KEY;
  const API_SECRET = process.env.API_SECRET;

  // Configure o cliente axios com chave de API e segredo para autenticação
  const client = axios.create({
    baseURL: 'https://api.que.será.usada.com',// Alterar a api de acordo com a necessidade
    headers: {
      'Content-Type': 'application/json',
      'X-API-KEY': API_KEY,
      'X-API-SECRET': API_SECRET
    }
  });

  // Configurar parâmetros para o algoritmo do criador de mercado
  const ticker = 'AAPL';
  const spread = 0.01; // 1% spread-(definir aqui)
  const size = 0.1; // tamanho da ordem-(definir aqui)
  const delay = 1000; // 1 second

  // Start loop do criador de mercado
  while (true) {
    try {
      // Faz o Get no book de ofertas atual
      const response = await client.get(`/v1/orderbook/${ticker}`);
      const orderBook = response.data;

      // Calculate current midprice
      const midprice = (orderBook.bids[0].price + orderBook.asks[0].price) / 2;

      // Calcular o preço médio atual
      const bidPrice = midprice * (1 - spread);
      const askPrice = midprice * (1 + spread);

      // Coloca as ordens
      await client.post('/v1/orders', {
        ticker,
        side: 'buy',
        price: bidPrice,
        size
      });
      await client.post('/v1/orders', {
        ticker,
        side: 'sell',
        price: askPrice,
        size
      });

      // Imprimi a mensagem de status
      console.log(`Placed orders: bid at $${bidPrice} and ask at $${askPrice}`);
    } catch (error) {
      console.error(error);
    }

    // Aguarde o atraso especificado antes de fazer o próximo conjunto de pedidos
    await new Promise(resolve => setTimeout(resolve, delay));
  }
}

main();
