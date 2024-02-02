#!/usr/bin/node
/*
This script updates the text
of the `header` element to `New Header!!!`
when the user clicks on the element with id `update_header`.
*/

const UpdateHeader = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
  UpdateHeader.textContent = 'New Header!!!';
});
