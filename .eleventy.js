const yaml = require("yaml");
const { DateTime } = require("luxon");

module.exports = config => {
    config.addPassthroughCopy('./assets/');
    config.addPassthroughCopy("./images/");

    
    config.addDataExtension("yaml", contents => yaml.parse(contents));

    config.addFilter('htmlDateString', (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat('yyyy-LL-dd');
	});

    config.addFilter('readableDate', (dateObj) => {
		// dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
		return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat('dd LLLL yyyy');
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