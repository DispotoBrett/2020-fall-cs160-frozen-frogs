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
    it('Should display an error', async () => {
      loginPage = await LoginFactory.build();
      assert(!(await loginPage.login('FAKE_USER', 'DOES NOT EXIST')));
      loginPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Logging in with an existing user', async () => {
    it('Should prompt the user\'s profile', async () => {
      loginPage = await LoginFactory.build();
      assert((await loginPage.login('DemoBuyer', 'sjsu')));
      loginPage.destroy();
    }).timeout(TIMEOUT);
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