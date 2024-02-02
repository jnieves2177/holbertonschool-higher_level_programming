#!/usr/bin/node
/*
This script updates the text color
of the `header` element to red (`#FF0000`)
when the user clicks on the tag with id `red_header`
*/

const headColor = document.querySelector('header');

const setColor = document.querySelector('#red_header');
setColor.addEventListener('click', () => {
  headColor.style.color = '#FF0000';
});
