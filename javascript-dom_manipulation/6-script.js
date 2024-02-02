#!/usr/bin/node
/*
This script fetches the character `name`
from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`.
*/

const ActorName = document.querySelector('#character');

fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => { ActorName.textContent = data.name; });
