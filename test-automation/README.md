## <a name='RegressionTests'></a>Regression Tests
- The system-level automated tests use the following tools:
	- `npm` and `node` for most things
	- `mocha` for the test framework
	- `selenium` for remote webdriver 
	- `msedgewebdriver` for controlling microsoft edge
- The `test-automation/` directory is the home of our regression test node application
	- After `npm install` you can run the tests with `npm test`. Make you startup the django server first at `localhost:8000`
- The tests themselves are in 	`/test-automation/tests/all.test.js`
- There are several node modules in `/test-automation/pages/`. The each provide a factory function for page-object-model (POM) pages/objects. Below is a architectual diagram of the POM model. ![Pom model](https://miro.medium.com/max/1200/1*Uz0xBEbnd7IhEubY392Cow.png)

### The tests
1. Logging in with an actual user
2. Logging in with a non-existent user
3. Registering with all valid credentials
4. Registering with invalid password length, special characters.
5. Registering with non-matching password and confirm password
6. Registering with non-sjsu email address
7. Liking a book and having that reflected on the “browse books” page
8. Un-liking a book and having that reflected
9. Liking books and making sure they show up on the users profile page
