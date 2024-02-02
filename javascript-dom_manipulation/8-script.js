#!/usr/bin/node
/*
This script fetches from
`https://hellosalut.stefanbohacek.dev/?lang=fr`
and displays the value of `hello` from that fetch
in the HTML element with id `hello`.
*/

document.addEventListener('DOMContentLoaded', () => {
    fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
        const helloContent = document.getElementById('hello');
        helloContent.textContent = document.getElementById('hello');
    });
})
