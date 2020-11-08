/* SJSU_BOOKSHARE POM FACTORIES */
let LoginFactory = require('../pages/login.js');
let RegisterFactory = require('../pages/register.js');
let BrowseFactory = require('../pages/browse.js');
let ProfileFactory = require('../pages/profile.js');

/* TEST STUFF */
let assert = require('assert');
const { doesNotMatch } = require('assert');
const moment = require('moment');
const TIMEOUT = 350000000;

describe('Registration Tests', () => {

  describe('Registering without an SJSU email address', async () => {
    it('Should display an error', async () => {
      registerPage = await RegisterFactory.build();
      assert(!await registerPage.register(moment().valueOf(), 'person@gmail.com', '12345%@$KdkcxL', '12345%@$KdkcxL'));
      await registerPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Registering with invalid password', async () => {
    it('Should display an error', async () => {
      registerPage = await RegisterFactory.build();
      assert(!await registerPage.register(moment().valueOf(), 'person@sjsu.edu', 'password', 'password'));
      await registerPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Registering with mismatched passwords', async () => {
    it('Should display an error', async () => {
      registerPage = await RegisterFactory.build();
      assert(!await registerPage.register(moment().valueOf(), 'person@sjsu.edu', 'firstPassword', 'secondPassword'));
      await registerPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Registering with valid credentails', async () => {
    it('Should prompt the user\'s profile', async () => {
      registerPage = await RegisterFactory.build();
      assert(await registerPage.register(moment().valueOf(), 'person@sjsu.edu', '12345%@$KdkcxL', '12345%@$KdkcxL'));
      await registerPage.destroy();
    }).timeout(TIMEOUT);
  });
});

describe('Login Tests', () => {

  describe('Logging in with a non-existent user', async () => {
    it('Should display an error', async () => {
      loginPage = await LoginFactory.build();
      assert(!(await loginPage.login('FAKE_USER', 'DOES NOT EXIST')));
      await loginPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Logging in with an existing user', async () => {
    it('Should prompt the user\'s profile', async () => {
      loginPage = await LoginFactory.build();
      assert((await loginPage.login('DemoBuyer', 'sjsu')));
      await loginPage.destroy();
    }).timeout(TIMEOUT);
  });

  describe('Logging in then logging out', async () => {
    it('Should log out the user', async () => {
      loginPage = await LoginFactory.build();
      assert((await loginPage.login('DemoBuyer', 'sjsu')));
      assert((await loginPage.logout()));
      await loginPage.destroy();
    }).timeout(TIMEOUT);
  });
});

describe('Favoriting a book Tests', () => {
  describe('Liking a book', async () => {
    it('Should update the liked state of the book', async () => {
      //TODO
    });
  });

  describe('Unliking a book', async () => {
    it('Should update the liked state of the book', async () => {
      //TODO
    });
  });
});