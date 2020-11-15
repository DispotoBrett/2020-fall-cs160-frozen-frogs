const { Builder, By, Key, until } = require('selenium-webdriver');
LoginFactory = require('./login')

//Factory function
exports.build = async () => {
  try {
    var driver = (await LoginFactory.build())._driver;
    await driver.get('http://localhost:8000/register')
  }
  catch (e) {
    console.log(bgRed + "Connection refused. Please startup the django server at localhost:8000. EXITING." + reset);
    await driver.close();
  }

  register = async (username, email, password, confirm_password) => {
    await logout();
    (await (await driver.findElement(By.xpath('//*[@id="name"]'))).sendKeys(username));
    (await (await driver.findElement(By.xpath('//*[@id="email"]'))).sendKeys(email));
    (await (await driver.findElement(By.xpath('//*[@id="password"]'))).sendKeys(password));
    (await (await driver.findElement(By.xpath('//*[@id="confirm-password"]'))).sendKeys(confirm_password));
    (await (await driver.findElement(By.xpath('//*[@id="submit_btn"]'))).click());
    let url = ((await driver.getCurrentUrl()).toString())
    return url.includes('profile');
  };

  destroy = async () => {
    await driver.close()
  }

  return {
    logout: logout,
    register: register,
    destroy: destroy,
    _driver: driver
  }
}

//Colors for fancy error printing
reset = "\x1b[0m"
bgRed = "\x1b[41m"