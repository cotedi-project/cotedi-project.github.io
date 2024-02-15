# CoTEDI Project Website

All documents are stored under `docs`. Once committed they will become available online a few moments later. 



## Style and Template Development

To get started with improving the styles or 
templates run the following commands. 

```bash
npm ci # or npm install
npm run watch:all
```

This will create a development server on your 
computer. This server will be accessible via 
`http://localhost:8080`.

Any changes to the styles or templates will 
become immediately visible in the development 
site.

If you have Docker installed, there is a 
dev-container specification that does most of 
the steps for you and leaves you desktop clean. 

### Folder Structure

The layout is defined in the `scss` folder.

Any interactive elements are stored in `src`.
