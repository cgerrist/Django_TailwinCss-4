# Installing TealWindCss 4 Tailwind CLI

install npm
install nodejs

run: npm install tailwindcss @tailwindcss/postcss postcss postcss-cli

create fille in root: postcss.config.js
enter:
export default {
    plugins: {
      "@tailwindcss/postcss": {},
    }
  }

create static dir if needed:
create: input.css file.  
enter:
@import "tailwindcss";
@source "../node_modules/@my-company/ui-lib";

create: tailwind file let it empty.

fill package.json file with:
{ "type":"module",
    "scripts": {
      "build": "postcss static/input.css --o static/tailwind.css",
      "watch": "postcss static/input.css --o static/tailwind.css --watch"
    },
    "dependencies": {
      "@tailwindcss/postcss": "^4.1.18",
      "postcss": "^8.5.6",
      "postcss-cli": "^11.0.1",
      "tailwindcss": "^4.1.18"
    }
  }

npm run watch

success
