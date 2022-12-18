
# Algo Trading-Formador de mercado. 
## Versão: 0.01

## 💻 Projeto
Esse algoritmo busca continuamente o livro de pedidos atual para um determinado ticker, ele calcula o preço médio e coloca ordens de compra e venda em um determinado spread em torno do preço médio. Ele então espera por um atraso especificado (neste caso, 1 segundo) antes de colocar o próximo conjunto de pedidos.

## 🚀 Tecnologias e Libs utilizadas na construção

- Node-js
- Axios
- crypto-js
- dotenv
  
## ✍🏻 Instalação

- Faça o download do projeto.
- Instale as dependências

```bash
  npm install
```

- configure o arquivo .env colocando suas chaves de api, como nesse exemplo:
```bash
API_KEY= Z59H9xQTqh4HvYV-BrzzFvVy
API_SECRET=RuL-uXURsjmU1AXHoergGqTSM8aKpsccISUgNonos6RpGT4k
```
## No Arquivo index.js alterar as seguintes etapas

- Altere a baseURL, a sua necessidade, que está nesse trecho do código:
 ```bash
 // Configure o cliente axios com chave de API e segredo para autenticação
  const client = axios.create({
    baseURL: 'https://api.que.será.usada.com',// Alterar a api de acordo com a necessidade
    headers: {
      'Content-Type': 'application/json',
      'X-API-KEY': API_KEY,
      'X-API-SECRET': API_SECRET
    }
  });
```

- Defina o ticker do ativo e outros parâmetros, que será usado alterando os campos:
 ```bash
// Configurar parâmetros para o algoritmo do criador de mercado
  const ticker = 'AAPL';
  const spread = 0.01; // 1% spread-(definir aqui)
  const size = 0.1; // tamanho da ordem-(definir aqui)
```

- Altere o endereço do GET do algoritmo a sua necessidade de rota
 ```bash
// Faz o Get no book de ofertas atual
      const response = await client.get(`/v1/seu-book-aqui/${ticker}`);
      const orderBook = response.data;
```

- Altere o método POST do algoritmo a sua necessidade de rota
 ```bash
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
```

- Rode o projeto com o comando
 ```bash
npm start
```

# 🛑 Disclaimer
 #### Este ainda é uma versão inicial, do algoritmo, fique a vontade para baixar fazer testes e melhorias, não indico testar em contas reais, os seus testes são por sua conta em risco !

## Licença

[MIT](https://choosealicense.com/licenses/mit/)



