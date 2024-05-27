const yaml = require("yaml");
const { DateTime } = require("luxon");

const path = require("node:path");
const Image = require("@11ty/eleventy-img");

const markdownit = require("markdown-it");

// markdown-it-attrs uses commonJs modules and is a showstopper for modernizing the codebase
const markdownItAttrs = require("markdown-it-attrs");

const markdownItOptions = {
    html: true,
    breaks: false,
    linkify: true
};

module.exports = (eleventyConfig) => {
    // the following line is required for stylesheet development
    // config.setServerPassthroughCopyBehavior("passthrough");

    eleventyConfig.ignores.add("_system/**");
    eleventyConfig.ignores.add(".devcontainer/**");
    eleventyConfig.ignores.add("**/node_modules/**");
    eleventyConfig.ignores.add("**/scss/**");
    eleventyConfig.ignores.add("_site/**");

    eleventyConfig.addPassthroughCopy("assets/**");
    eleventyConfig.addPassthroughCopy("docs/images/**");

    eleventyConfig.addPassthroughCopy("docs/**/*.jpg");
    eleventyConfig.addPassthroughCopy("docs/**/*.jpeg");
    eleventyConfig.addPassthroughCopy("docs/**/*.png");
    eleventyConfig.addPassthroughCopy("docs/**/*.svg");
    eleventyConfig.addPassthroughCopy("docs/**/*.pdf");
    eleventyConfig.addPassthroughCopy("docs/**/*.webp");
    eleventyConfig.addPassthroughCopy("docs/**/*.ico");
    eleventyConfig.addPassthroughCopy("docs/**/*.zip");

    eleventyConfig.addPlugin(Image.eleventyImageTransformPlugin, {
        // which file extensions to process
        extensions: "html",

        // Add any other Image utility options here:

        // optional, output image formats
        // formats: ["webp", "jpeg","svg"],
        formats: ["auto"],

        svgShortCircuit: "size",

        // optional, output image widths
        widths: [200, 400, 800, 1280, 1920, 2400, "auto"],

        // optional, attributes assigned on <img> override these values.
        defaultAttributes: {
            loading: "lazy",
            decoding: "async",
            sizes: [200, 400, 800, 1280, 1920, 2400, "auto"],
        },

        filenameFormat: function (id, src, width, format, options) {
            // id: hash of the original image
            // src: original image path
            // width: current width in px
            // format: current file format
            // options: set of options passed to the Image call
            const ext = path.extname(src);
            const filename = path.basename(src, ext);

            return `${filename}-${width}.${format}`;
        }
    });

    eleventyConfig.addDataExtension("yaml", contents => yaml.parse(contents));

    eleventyConfig.addShortcode("thisYear", () => DateTime.now().setZone("Europe/Amsterdam").toFormat("yyyy"));
    eleventyConfig.addShortcode("thisDate", () => DateTime.now().setZone("Europe/Amsterdam").toFormat("yyyy-LL-dd"));

    eleventyConfig.addFilter("dateYear", (dateObj) => {
        // dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
        return `${DateTime.fromJSDate(dateObj, {zone: "Europe/Amsterdam"}).toFormat("yyyy")}`;
    });

    eleventyConfig.addFilter("htmlDateString", (dateObj) => {
        // dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
        return `${DateTime.fromJSDate(dateObj, {zone: "Europe/Amsterdam"}).toFormat("yyyy-LL-dd")}`;
    });

    eleventyConfig.addFilter("readableDate", (dateObj) => {
        // dateObj input: https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
        return DateTime.fromJSDate(dateObj, {zone: "Europe/Amsterdam"}).toFormat("dd LLLL yyyy");
    });

    eleventyConfig.addFilter("entryLimit", (arr, limit) => arr.slice(0, limit));

    eleventyConfig.setLibrary("md", markdownit(markdownItOptions).use(markdownItAttrs));

    return {
        markdownTemplateEngine: "njk",
        dataTemplateEngine: "njk",
        htmlTemplateEngine: "njk",
        dir: {
            input: "docs",
            includes: "../_layouts",
            data: "../_data",
        }
    };
};
