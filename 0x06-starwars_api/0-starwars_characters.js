#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  let i = x;
  while (i < actors.length) {
    request(actors[i], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
    i++;
  }
};
