// Import the axios library
const axios = require('axios');

// Replace 'YOUR_API_KEY' with your actual News API key
const apiKey = '78a424b105794b8a9c6af00bc553cbcb';
const stockSymbol = 'AAPL'; // Example stock symbol (Apple Inc.)

// Define the URL for the News API endpoint
const apiUrl = `https://newsapi.org/v2/everything?q=${stockSymbol}&apiKey=${apiKey}&pageSize=10`;

// Make a GET request to the News API endpoint
axios.get(apiUrl)
  .then(response => {
    const articles = response.data.articles;
    articles.forEach(article => {
      console.log(article.title, article.url);
      // Display article title and URL in your application's UI
    });
  })
  .catch(error => {
    console.error('Error:', error.message);
    // Display error message in your application's UI
  });
