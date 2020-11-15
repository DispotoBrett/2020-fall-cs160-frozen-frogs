/* SJSU_BOOKSHARE POM FACTORIES */
let LoginFactory = require('../pages/login.js');
let RegisterFactory = require('../pages/register.js');
let BrowseFactory = require('../pages/browse.js');
let ProfileFactory = require('../pages/profile.js');
let PostingFactory = require('../pages/posting.js');

/* TEST STUFF */
let assert = require('assert');
const { doesNotMatch } = require('assert');
const moment = require('moment');
const TIMEOUT = 350000000;

// describe('Registration Tests', () => {

//   describe('Registering without an SJSU email address', async () => {
//     it('Should display an error', async () => {
//       registerPage = await RegisterFactory.build();
//       assert(!await registerPage.register(moment().valueOf(), 'person@gmail.com', '12345%@$KdkcxL', '12345%@$KdkcxL'));
//       await registerPage.destroy();
//     }).timeout(TIMEOUT);
//   });

//   describe('Registering with invalid password', async () => {
//     it('Should display an error', async () => {
//       registerPage = await RegisterFactory.build();
//       assert(!await registerPage.register(moment().valueOf(), 'person@sjsu.edu', 'password', 'password'));
//       await registerPage.destroy();
//     }).timeout(TIMEOUT);
//   });

//   describe('Registering with mismatched passwords', async () => {
//     it('Should display an error', async () => {
//       registerPage = await RegisterFactory.build();
//       assert(!await registerPage.register(moment().valueOf(), 'person@sjsu.edu', 'firstPassword', 'secondPassword'));
//       await registerPage.destroy();
//     }).timeout(TIMEOUT);
//   });

//   describe('Registering with valid credentails', async () => {
//     it('Should prompt the user\'s profile', async () => {
//       registerPage = await RegisterFactory.build();
//       assert(await registerPage.register(moment().valueOf(), 'person@sjsu.edu', '12345%@$KdkcxL', '12345%@$KdkcxL'));
//       await registerPage.destroy();
//     }).timeout(TIMEOUT);
//   });
// });

// describe('Login Tests', () => {

//   describe('Logging in with a non-existent user', async () => {
//     it('Should display an error', async () => {
//       loginPage = await LoginFactory.build();
//       assert(!(await loginPage.login('FAKE_USER', 'DOES NOT EXIST')));
//       await loginPage.destroy();
//     }).timeout(TIMEOUT);
//   });

//   describe('Logging in with an existing user', async () => {
//     it('Should prompt the user\'s profile', async () => {
//       loginPage = await LoginFactory.build();
//       assert((await loginPage.login('DemoBuyer', 'sjsu')));
//       await loginPage.destroy();
//     }).timeout(TIMEOUT);
//   });

//   describe('Logging in then logging out', async () => {
//     it('Should log out the user', async () => {
//       loginPage = await LoginFactory.build();
//       assert((await loginPage.login('DemoBuyer', 'sjsu')));
//       assert((await loginPage.logout()));
//       await loginPage.destroy();
//     }).timeout(TIMEOUT);
//   });
// });

// describe('Browse Tests', () => {
//   describe('Liking several books', async () => {
//     it('Should update the liked state of the book', async () => {
//       for (cnt = 0; cnt < 2; cnt++) {
//         browsePage = await BrowseFactory.build();
//         originalLikes = []
//         for (i = -5; i < 0; i++) if (browsePage.isLiked(i)) originalLikes.push(i);
//         for (i = -5; i < 0; i++) await browsePage.toggleLike(i);
//         for (i = -5; i < 0; i++) assert(!(i in originalLikes));
//         browsePage.destroy();
//       }
//     }).timeout(TIMEOUT);
//   });
// });

// describe('Profile Tests', () => {
//   describe('Liking several books', async () => {
//     it('Should shold show the books on the user\'s profile', async () => {
//       browsePage = await BrowseFactory.build();
//       for (i = -5; i < 0; i++) await browsePage.toggleLike(i);
//       expectedLikes = []
//       for (i = -5; i < 0; i++) if (browsePage.isLiked(i)) originalLikes.push(i);
//       browsePage.destroy();

//       profilePage = await ProfileFactory.build();
//       actualLikes = profilePage.getLikes();
//       for (i in expectedLikes)
//         assert(expectedLikes[i] in actualLikes);

//       browsePage.destroy();
//     }).timeout(TIMEOUT);
//   });
// });

describe('Posting Tests', () => {
  describe('Valid posting', async () => {
    it('Should make a successful book posting', async () => {
      postingPage = await PostingFactory.build();
      assert((await postingPage.posting('test','test','test', 'test', 'test', 'test',10)));
      postingPage.destroy();
    }).timeout(TIMEOUT);
  });

  // describe('Invalid posting: No Title', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('','test','test', 'test', 'test', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Author', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','','test', 'test', 'test', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No ISBN', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','', 'test', 'test', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Subject', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','test', '', 'test', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Class Used In', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','test', 'test', '', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Description', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','test', 'test', 'test', '',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Price', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','test', 'test', 'test', 'test','')));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: Non integer Price', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting('test','test','test', 'test', 'test', 'test','bad')));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });

  // describe('Invalid posting: No Image', async () => {
  //   it('Should make an unsuccessful book posting', async () => {
  //     postingPage = await PostingFactory.build();
  //     assert(!(await postingPage.posting_no_img('test','test','test', 'test', 'test', 'test',10)));
  //     postingPage.destroy();
  //   }).timeout(TIMEOUT);
  // });
});

