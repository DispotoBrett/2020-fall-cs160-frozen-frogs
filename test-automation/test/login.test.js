/*
    A collection of regression tests for spartan bookshare.
*/

/*  POM IMPORTS */
let LoginFactory = require('../pages/login.js');
let BrowseFactory = require('../pages/browse.js');
let ProfileFactory = require('../pages/profile.js');

/* TEST STUFF */
let assert = require('assert');
const { doesNotMatch } = require('assert');
const TIMEOUT = 350000000;

let setup = () => { }
let teardown = () => { }

describe('Login Tests', () => {

  describe('Logging in with a non-existent user', async () => {
    it('Should return to the login page', async () => {
      loginPage = await LoginFactory.build();
      await loginPage.login('D-N-E', 'DOES NOT EXIST');
    }).timeout(TIMEOUT);

    //Make sure we are still on the same pager
    //Check a loggedIn() method, to get the  uanme. If it throws an error we're happy.
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