const { Builder, By, Key, until } = require('selenium-webdriver');
LoginFactory = require('./login');

//Factory function
exports.build = async () => {
    try {
        var basePage = await LoginFactory.build();
        await basePage.login('DemoBuyer', 'sjsu'); //Our default test person
        driver = basePage._driver;
    }
    catch (e) {
        console.log(bgRed + "Connection refused. Please startup the django server at 127.0.0.1:8000. EXITING." + reset);
        await driver.close();
    }

    getLikes = async (index) => {
        likes = [];
        for(i=(0-DEFUALT_BOOK_COUNT); i<0; i++){
            try {
                await (await driver.findElement(By.xpath(`//*[@id="unfavortie${i}"]`)));
                likes.push(i);
            }
            catch (ex) {}
        }
        return likes;
    };

    destroy = async () => {
        await driver.close()
    };

    return {
        getLikes: getLikes,
        destroy: destroy,
        _driver: driver
    };
}

//Colors for fancy error printing
reset = "\x1b[0m"
bgRed = "\x1b[41m"
DEFUALT_BOOK_COUNT = 5