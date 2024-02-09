const yaml = require("yaml");

module.exports = config => {
    config.addPassthroughCopy('./assets/');
    config.addPassthroughCopy("./images/");

    config.addDataExtension("yaml", contents => yaml.parse(contents));

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