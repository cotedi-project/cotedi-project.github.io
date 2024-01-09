module.exports = config => {
    config.addPassthroughCopy('./assets/');

    return {
      markdownTemplateEngine: 'njk',
      dataTemplateEngine: 'njk',
      htmlTemplateEngine: 'njk',
      dir: {
        input: 'docs',
        includes: '../_layouts',
      }
    };
  };