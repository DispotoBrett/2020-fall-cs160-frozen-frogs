const { Builder, By, Key, until } = require('selenium-webdriver');

//Factory function
exports.build = async () => {
  try {
    var driver = new Builder().forBrowser('MicrosoftEdge').build();
    await driver.get('localhost:8000/login')
  }
  catch (e) {
    console.log(bgRed + "Connection refused. Please startup the django server at localhost:8000. EXITING." + reset);
    await driver.close();
  }
  logout = async () => {
    try {
      (await (await driver.findElement(By.xpath('//*[@id="logout"]'))).click());
      return true;
    } catch (ex) {
      //No one was logged in. 
      return false;
    }
  };

  login = async (username, password) => {
    await logout();
    (await (await driver.findElement(By.xpath('//*[@id="username"]'))).sendKeys(username));
    (await (await driver.findElement(By.xpath('//*[@id="password"]'))).sendKeys(password));
    (await (await driver.findElement(By.xpath('//*[@id="submit"]'))).click());

    try { //Check if login worked
      await driver.findElement(By.xpath('//*[@id="error"]'));
      return false;
    } catch (ex) {
      return true;
    }
  };

  destroy = async () => {
    await driver.sleep(1000); //Its nice to see the final page sometimes
    await driver.close();
  }

  return {
    logout: logout,
    login: login,
    destroy: destroy,
    _driver: driver
  }
}

//Colors for fancy error printing
reset = "\x1b[0m"
bgRed = "\x1b[41m"