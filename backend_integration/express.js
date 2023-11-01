const express = require('express');
const cors = require('cors'); // Import the CORS middleware
const axios = require('axios');
const app = express();
const port = 9001; // Change this to your desired port number
app.use(cors());
// Define a route to search for products
app.get('/search', async (req, res) => {
  const query = req.query.query; // Get the search query from the request

  try {
    // Make requests to the Amazon and Flipkart APIs
    const amazonResponse = await axios.get(`http://localhost:8080/?q=${query}`);
    const flipkartResponse = await axios.get(`http://localhost:3000/search/${query}`);

    // Combine and send the responses to the frontend
    const combinedResponse = {
      amazon: amazonResponse.data,
      flipkart: flipkartResponse.data,
    };

    res.json(combinedResponse);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Backend server is running on port ${port}`);
});
