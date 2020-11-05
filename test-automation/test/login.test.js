/*
    A collection of regression tests for spartan bookshare.
*/

/*  POM IMPORTS */
let LoginFactory = require('../pages/login.js');
let BrowseFactory = require('../pages/browse.js');
let ProfileFactory = require('../pages/profile.js');

/* TEST STUFF */
let assert = require('assert');
let setup = () => {}
let teardown = () => {}

describe('Login Tests', () => {
    describe('Logging in with a non-existent user', () => {
    it('Should return to the login page', () => {

    });
  });

  describe('Logging in with an existing user', () => {
    it('Should prompt the user\'s profile', () => {

    });
  });
});

describe('Profile Functionality Tests', () => {
    describe('Liking a book', () => {
    it('Should be rendered on a user\'s profile', () => {

    });
  });

  describe('Unliking a book from the browse menu', () => {
    it('The liked book should NOT be rendered on a users profile\'s profile', () => {

    });
  });
});