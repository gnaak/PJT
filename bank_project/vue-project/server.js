// server.js

const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

app.use(express.json());

app.get('/api/news', async (req, res) => {
  const apiKey = 'v_Lz3CB_Y8gq2XmsD0Bg';
  const query = req.query.query;

  try {
    const response = await axios.get(`https://openapi.naver.com/v1/search/news.json?query=${query}`, {
      headers: {
        'X-Naver-Client-Id': apiKey,
        'X-Naver-Client-Secret': 'Log7bWqDXK',
      },
    });

    res.json(response.data);
  } catch (error) {
    console.error('Error fetching news:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
