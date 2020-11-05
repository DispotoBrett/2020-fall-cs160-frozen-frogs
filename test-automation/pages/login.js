const { Builder, By, Key, until } = require('selenium-webdriver');
var driver = new Builder().forBrowser('MicrosoftEdge').build();

//Example :)
(async function () {
  await driver.get('http://www.google.com/')
})();