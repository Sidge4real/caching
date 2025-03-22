// Express.js server met Redis caching
const express = require('express');
const Redis = require('ioredis');
const axios = require('axios');
require('dotenv').config();

const app = express();
// const redis = new Redis({
//   host: 'your-redis-host', // Upstash Redis URL
//   password: 'your-redis-password',
// });

const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
});

const NEWS_API_URL = `https://newsapi.org/v2/top-headlines?country=us&apiKey=${process.env.NEWS_API_KEY}`;

app.get('/news', async (req, res) => {
  const cachedNews = await redis.get('news_data');
  if (cachedNews) {
    // res.setHeader('Cache-Control', 'public, max-age=600'); // 10 minuten cache in de browser
    return res.json(JSON.parse(cachedNews));
  }

  try {
    const response = await axios.get(NEWS_API_URL);
    const newsData = response.data;
    await redis.setex('news_data', 600, JSON.stringify(newsData));
    res.setHeader('Cache-Control', 'public, max-age=600');
    res.json(newsData);
  } catch (error) {
    res.status(500).send('Error fetching news');
  }
});

app.listen(8000, () => {
  console.log('Server is running on http://localhost:8000');
});