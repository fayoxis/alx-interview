#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

const getCharacterNames = (filmId) => {
  return new Promise((resolve, reject) => {
    request(`${API_URL}/films/${filmId}/`, (err, _, body) => {
      if (err) {
        reject(err);
        return;
      }
      
      const charactersURL = JSON.parse(body).characters;
      const charactersName = charactersURL.map(url => {
        return new Promise((resolveChar, rejectChar) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              rejectChar(promiseErr);
            } else {
              resolveChar(JSON.parse(charactersReqBody).name);
            }
          });
        });
      });

      Promise.all(charactersName)
        .then(names => resolve(names))
        .catch(allErr => reject(allErr));
    });
  });
};

const main = async () => {
  for (let i = 2; i < process.argv.length; i++) {
    try {
      const names = await getCharacterNames(process.argv[i]);
      console.log(names.join('\n'));
    } catch (error) {
      console.log(error);
    }
  }
};

main();
