const { Builder, By, Key, until } = require('selenium-webdriver');
LoginFactory = require('./login');

//Factory function
exports.build = async () => {
    try {
        var basePage = await LoginFactory.build();
        await basePage.login('DemoBuyer', 'sjsu'); //Our default test person
        driver = basePage._driver;
        await driver.get('http://127.0.0.1:8000/browse');
        await driver.sleep(1000);
    }
    catch (e) {
        console.log(bgRed + "Connection refused. Please startup the django server at 127.0.0.1:8000. EXITING." + reset);
        await driver.close();
    }

    isLiked = async (index) => {
        try {
            await (await driver.findElement(By.xpath(`//*[@id="unfavortie${index}"]`)));
            return true;
        }
        catch (ex) {
            return false;
        }
    };

    toggleLike = async (index) => {
        try {
            await (await driver.findElement(By.xpath(`//*[@id="unfavortie${index}"]`))).click();
        }
        catch (ex) {
            await (await driver.findElement(By.xpath(`//*[@id="favortie${index}"]`))).click();
        }
    };

    destroy = async () => {
        await driver.close()
    };

    return {
        toggleLike: toggleLike,
        isLiked: isLiked,
        destroy: destroy,
        _driver: driver
    };
}

//Colors for fancy error printing
reset = "\x1b[0m"
bgRed = "\x1b[41m"