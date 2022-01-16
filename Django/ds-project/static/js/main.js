import Typed from './node_modules/typed.js'

// console.log('object');
const greeting = document.querySelector('#greeting')
const typed = new Typed(greeting, {
    strings: ['Welcome to', 'Data Science'],
    typeSpeed: 30
})

