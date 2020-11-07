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
    console.log("hi");
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
    await driver.close()    
  }

  return {
    logout: logout,
    login: login,
    destroy: destroy
  }
}

//Colors for fancy error printing
reset = "\x1b[0m"
bgRed = "\x1b[41m"
