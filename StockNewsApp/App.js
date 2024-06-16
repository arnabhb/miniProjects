import React, { useState, useEffect } from 'react';
import axios from 'axios';
import NewsList from './NewsList';

const App = () => {
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    // Fetch news articles from the backend API
    axios.get('http://localhost:3001/api/news') // Adjust URL based on backend server configuration
      .then(response => {
        setArticles(response.data);
      })
      .catch(error => {
        console.error('Error fetching news articles:', error);
      });
  }, []);

  return (
    <div>
      <h1>Stock News Aggregator</h1>
      <NewsList articles={articles} />
    </div>
  );
};

export default App;

