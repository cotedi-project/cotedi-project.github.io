const yaml = require("yaml");
const { DateTime } = require("luxon");

module.exports = config => {

    // the following line is required for stylesheet development
    config.setServerPassthroughCopyBehavior("passthrough");

    config.addPassthroughCopy('./assets/');
    config.addPassthroughCopy("./images/");
    config.addPassthroughCopy("**/*.jpg");
    config.addPassthroughCopy("**/*.png");
    config.addPassthroughCopy("**/*.svg");
    config.addPassthroughCopy("**/*.pdf");
    
    config.addDataExtension("yaml", contents => yaml.parse(contents));

    config.addShortcode("thisYear", () => DateTime.now().setZone('Europe/Amsterdam').toFormat('yyyy'));
    config.addShortcode("thisDate", () => DateTime.now().setZone('Europe/Amsterdam').toFormat('yyyy-LL-dd'));

    config.addFilter('dateYear', (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return `${DateTime.fromJSDate(dateObj, {zone: 'Europe/Amsterdam'}).toFormat('yyyy')}`;
	});

    config.addFilter('htmlDateString', (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return `${DateTime.fromJSDate(dateObj, {zone: 'Europe/Amsterdam'}).toFormat('yyyy-LL-dd')}`;
	});

    config.addFilter('readableDate', (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return DateTime.fromJSDate(dateObj, {zone: 'Europe/Amsterdam'}).toFormat('dd LLLL yyyy');
	});

    config.addFilter("entryLimit", (arr, limit) => arr.slice(0, limit));

    return {
      markdownTemplateEngine: 'njk',
      dataTemplateEngine: 'njk',
      htmlTemplateEngine: 'njk',
      dir: {
        input: 'docs',
        includes: '../_layouts',
        data: '../_data',
      }
    };
  };