#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  printActors(actors);
});

const printActors = (actors) => {
  let index = 0;

  const fetchActor = () => {
    if (index === actors.length) return;

    request(actors[index], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
      index++;
      fetchActor();
    });
  }

  fetchActor();
}
