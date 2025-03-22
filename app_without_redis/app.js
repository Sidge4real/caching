const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();

const NEWS_API_URL = `https://newsapi.org/v2/top-headlines?country=us&apiKey=${process.env.NEWS_API_KEY}`;

app.get('/news', async (req, res) => {
  try {
    const response = await axios.get(NEWS_API_URL);
    const newsData = response.data;
    // res.setHeader('Cache-Control', 'public, max-age=600'); // 10 minuten cache in de browser
    res.json(newsData);
  } catch (error) {
    res.status(500).send('Error fetching news');
  }
});

app.listen(8001, () => {
  console.log('Server is running on http://localhost:8001');
});
