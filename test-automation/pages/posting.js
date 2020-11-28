const { Builder, By, Key, until } = require('selenium-webdriver');
LoginFactory = require('./login');
remote = require('selenium-webdriver/remote');
path = require('path')

exports.build = async () => {

	// Set up: Need to log in first
	try {
		var base = await LoginFactory.build();
		await base.login('DemoBuyer', 'sjsu');
		driver = base._driver;
		await driver.get('http://127.0.0.1:8000/list_book');
	}
	catch (e) {
		console.log(bgRed + "Connection refused. Please startup the django server at 127.0.0.1:8000. EXITING." + reset);
        await driver.close();
	}

	// Posting
	posting = async(title, author, isbn, subject, class_used, description, price) => {
		(await (await driver.findElement(By.xpath('//*[@id="title"]'))).sendKeys(title));
		(await (await driver.findElement(By.xpath('//*[@id="picture"]'))).sendKeys(path.resolve(__dirname, "test.jpg")));
		(await (await driver.findElement(By.xpath('//*[@id="author"]'))).sendKeys(author));
		(await (await driver.findElement(By.xpath('//*[@id="isbn"]'))).sendKeys(isbn));
		(await (await driver.findElement(By.xpath('//*[@id="subject"]'))).sendKeys(subject));
		(await (await driver.findElement(By.xpath('//*[@id="class_used"]'))).sendKeys(class_used));
		(await (await driver.findElement(By.xpath('//*[@id="description"]'))).sendKeys(description));
		(await (await driver.findElement(By.xpath('//*[@id="price"]'))).sendKeys(price));
		(await (await driver.findElement(By.xpath('//*[@id="submit_btn"]'))).click());
	    let url = ((await driver.getCurrentUrl()).toString())
	    return url.includes('app/posting');
	};

	// Posting with no image supplied
	posting_no_img = async(title, author, isbn, subject, class_used, description, price) => {
		(await (await driver.findElement(By.xpath('//*[@id="title"]'))).sendKeys(title));
		(await (await driver.findElement(By.xpath('//*[@id="author"]'))).sendKeys(author));
		(await (await driver.findElement(By.xpath('//*[@id="isbn"]'))).sendKeys(isbn));
		(await (await driver.findElement(By.xpath('//*[@id="subject"]'))).sendKeys(subject));
		(await (await driver.findElement(By.xpath('//*[@id="class_used"]'))).sendKeys(class_used));
		(await (await driver.findElement(By.xpath('//*[@id="description"]'))).sendKeys(description));
		(await (await driver.findElement(By.xpath('//*[@id="price"]'))).sendKeys(price));
		(await (await driver.findElement(By.xpath('//*[@id="submit_btn"]'))).click());
	    let url = ((await driver.getCurrentUrl()).toString())
	    return url.includes('app/posting');
	};

	destroy = async () => {
		await driver.close()
	}

	return {
		posting: posting,
		posting_no_img: posting_no_img,
		destroy: destroy,
		_driver: driver
	};

}
