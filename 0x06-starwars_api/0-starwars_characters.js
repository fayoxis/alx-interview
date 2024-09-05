#!/usr/bin/node

// Import 'request' module for making HTTP requests
const request = require('request');

// Make request to Star Wars API for specific film (ID from command line)
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  // Parse JSON response and extract 'characters' array
  const actors = JSON.parse(body).characters;
  // Start recursive function to fetch and print character names
  exactOrder(actors, 0);
});

// Recursive function to fetch and print character names in order
const exactOrder = (actors, x) => {
  // Base case: if all actors processed, return
  if (x === actors.length) return;
  // Request info about current character
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    // Parse JSON response and print character's name
    console.log(JSON.parse(body).name);
    // Recursive call to process next character
    exactOrder(actors, x + 1);
  });
};
