import React from 'react';

const NewsList = ({ articles }) => {
  return (
    <div>
      <h2>Latest News</h2>
      <ul>
        {articles.map(article => (
          <li key={article.title}>
            <h3>{article.title}</h3>
            <p>{article.description}</p>
            <p><strong>Publication Date:</strong> {new Date(article.publishedAt).toLocaleDateString()}</p>
            <p><a href={article.url} target="_blank" rel="noopener noreferrer">Read More</a></p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsList;
