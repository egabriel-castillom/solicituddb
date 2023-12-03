import cssutils

def extract_styles(css, elements, classes):
    sheet = cssutils.parseString(css)
    styles = ''

    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            selector = rule.selectorText
            # Check if the selector matches any of the elements or classes
            if any(element in selector for element in elements) or any('.'+cls in selector for cls in classes):
                styles += selector + ' {\n'
                for prop in rule.style:
                    styles += '    {}: {};\n'.format(prop.name, prop.value)
                styles += '}\n\n'

    # Write the styles to a new CSS file
    with open('new.css', 'w') as f:
        f.write(styles)

# Your CSS goes here
css = """

html {
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  font-family: sans-serif;
}

body {
  margin: 0;
}

article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section, summary {
  display: block;
}

audio, canvas, progress, video {
  vertical-align: baseline;
  display: inline-block;
}

audio:not([controls]) {
  height: 0;
  display: none;
}

[hidden], template {
  display: none;
}

a {
  background-color: rgba(0, 0, 0, 0);
}

a:active, a:hover {
  outline: 0;
}

abbr[title] {
  border-bottom: 1px dotted;
}

b, strong {
  font-weight: bold;
}

dfn {
  font-style: italic;
}

h1 {
  margin: .67em 0;
  font-size: 2em;
}

mark {
  color: #000;
  background: #ff0;
}

small {
  font-size: 80%;
}

sub, sup {
  vertical-align: baseline;
  font-size: 75%;
  line-height: 0;
  position: relative;
}

sup {
  top: -.5em;
}

sub {
  bottom: -.25em;
}

img {
  border: 0;
}

svg:not(:root) {
  overflow: hidden;
}

figure {
  margin: 1em 40px;
}

hr {
  box-sizing: content-box;
  height: 0;
}

pre {
  overflow: auto;
}

code, kbd, pre, samp {
  font-family: monospace;
  font-size: 1em;
}

button, input, optgroup, select, textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}

button {
  overflow: visible;
}

button, select {
  text-transform: none;
}

button, html input[type="button"], input[type="reset"] {
  -webkit-appearance: button;
  cursor: pointer;
}

button[disabled], html input[disabled] {
  cursor: default;
}

button::-moz-focus-inner, input::-moz-focus-inner {
  border: 0;
  padding: 0;
}

input {
  line-height: normal;
}

input[type="checkbox"], input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}

input[type="number"]::-webkit-inner-spin-button, input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

input[type="search"] {
  -webkit-appearance: none;
}

input[type="search"]::-webkit-search-cancel-button, input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

fieldset {
  border: 1px solid silver;
  margin: 0 2px;
  padding: .35em .625em .75em;
}

legend {
  border: 0;
  padding: 0;
}

textarea {
  overflow: auto;
}

optgroup {
  font-weight: bold;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

td, th {
  padding: 0;
}

@font-face {
  font-family: webflow-icons;
  src: url("data:application/x-font-ttf;charset=utf-8;base64,AAEAAAALAIAAAwAwT1MvMg8SBiUAAAC8AAAAYGNtYXDpP+a4AAABHAAAAFxnYXNwAAAAEAAAAXgAAAAIZ2x5ZmhS2XEAAAGAAAADHGhlYWQTFw3HAAAEnAAAADZoaGVhCXYFgQAABNQAAAAkaG10eCe4A1oAAAT4AAAAMGxvY2EDtALGAAAFKAAAABptYXhwABAAPgAABUQAAAAgbmFtZSoCsMsAAAVkAAABznBvc3QAAwAAAAAHNAAAACAAAwP4AZAABQAAApkCzAAAAI8CmQLMAAAB6wAzAQkAAAAAAAAAAAAAAAAAAAABEAAAAAAAAAAAAAAAAAAAAABAAADpAwPA/8AAQAPAAEAAAAABAAAAAAAAAAAAAAAgAAAAAAADAAAAAwAAABwAAQADAAAAHAADAAEAAAAcAAQAQAAAAAwACAACAAQAAQAg5gPpA//9//8AAAAAACDmAOkA//3//wAB/+MaBBcIAAMAAQAAAAAAAAAAAAAAAAABAAH//wAPAAEAAAAAAAAAAAACAAA3OQEAAAAAAQAAAAAAAAAAAAIAADc5AQAAAAABAAAAAAAAAAAAAgAANzkBAAAAAAEBIAAAAyADgAAFAAAJAQcJARcDIP5AQAGA/oBAAcABwED+gP6AQAABAOAAAALgA4AABQAAEwEXCQEH4AHAQP6AAYBAAcABwED+gP6AQAAAAwDAAOADQALAAA8AHwAvAAABISIGHQEUFjMhMjY9ATQmByEiBh0BFBYzITI2PQE0JgchIgYdARQWMyEyNj0BNCYDIP3ADRMTDQJADRMTDf3ADRMTDQJADRMTDf3ADRMTDQJADRMTAsATDSANExMNIA0TwBMNIA0TEw0gDRPAEw0gDRMTDSANEwAAAAABAJ0AtAOBApUABQAACQIHCQEDJP7r/upcAXEBcgKU/usBFVz+fAGEAAAAAAL//f+9BAMDwwAEAAkAABcBJwEXAwE3AQdpA5ps/GZsbAOabPxmbEMDmmz8ZmwDmvxmbAOabAAAAgAA/8AEAAPAAB0AOwAABSInLgEnJjU0Nz4BNzYzMTIXHgEXFhUUBw4BBwYjNTI3PgE3NjU0Jy4BJyYjMSIHDgEHBhUUFx4BFxYzAgBqXV6LKCgoKIteXWpqXV6LKCgoKIteXWpVSktvICEhIG9LSlVVSktvICEhIG9LSlVAKCiLXl1qal1eiygoKCiLXl1qal1eiygoZiEgb0tKVVVKS28gISEgb0tKVVVKS28gIQABAAABwAIAA8AAEgAAEzQ3PgE3NjMxFSIHDgEHBhUxIwAoKIteXWpVSktvICFmAcBqXV6LKChmISBvS0pVAAAAAgAA/8AFtgPAADIAOgAAARYXHgEXFhUUBw4BBwYHIxUhIicuAScmNTQ3PgE3NjMxOAExNDc+ATc2MzIXHgEXFhcVATMJATMVMzUEjD83NlAXFxYXTjU1PQL8kz01Nk8XFxcXTzY1PSIjd1BQWlJJSXInJw3+mdv+2/7c25MCUQYcHFg5OUA/ODlXHBwIAhcXTzY1PTw1Nk8XF1tQUHcjIhwcYUNDTgL+3QFt/pOTkwABAAAAAQAAmM7nP18PPPUACwQAAAAAANciZKUAAAAA1yJkpf/9/70FtgPDAAAACAACAAAAAAAAAAEAAAPA/8AAAAW3//3//QW2AAEAAAAAAAAAAAAAAAAAAAAMBAAAAAAAAAAAAAAAAgAAAAQAASAEAADgBAAAwAQAAJ0EAP/9BAAAAAQAAAAFtwAAAAAAAAAKABQAHgAyAEYAjACiAL4BFgE2AY4AAAABAAAADAA8AAMAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAADgCuAAEAAAAAAAEADQAAAAEAAAAAAAIABwCWAAEAAAAAAAMADQBIAAEAAAAAAAQADQCrAAEAAAAAAAUACwAnAAEAAAAAAAYADQBvAAEAAAAAAAoAGgDSAAMAAQQJAAEAGgANAAMAAQQJAAIADgCdAAMAAQQJAAMAGgBVAAMAAQQJAAQAGgC4AAMAAQQJAAUAFgAyAAMAAQQJAAYAGgB8AAMAAQQJAAoANADsd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzVmVyc2lvbiAxLjAAVgBlAHIAcwBpAG8AbgAgADEALgAwd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzUmVndWxhcgBSAGUAZwB1AGwAYQByd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzRm9udCBnZW5lcmF0ZWQgYnkgSWNvTW9vbi4ARgBvAG4AdAAgAGcAZQBuAGUAcgBhAHQAZQBkACAAYgB5ACAASQBjAG8ATQBvAG8AbgAuAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==") format("truetype");
  font-weight: normal;
  font-style: normal;
}

[class^="w-icon-"], [class*=" w-icon-"] {
  speak: none;
  font-variant: normal;
  text-transform: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  font-family: webflow-icons !important;
}

.w-icon-slider-right:before {
  content: "î˜€";
}

.w-icon-slider-left:before {
  content: "î˜";
}

.w-icon-arrow-down:before, .w-icon-dropdown-toggle:before {
  content: "î˜ƒ";
}

.w-icon-file-upload-remove:before {
  content: "î¤€";
}

.w-icon-file-upload-icon:before {
  content: "î¤ƒ";
}

* {
  box-sizing: border-box;
}

html {
  height: 100%;
}

body {
  min-height: 100%;
  color: #333;
  background-color: #fff;
  margin: 0;
  font-family: Arial, sans-serif;
  font-size: 14px;
  line-height: 20px;
}

img {
  max-width: 100%;
  vertical-align: middle;
  display: inline-block;
}

html.w-mod-touch * {
  background-attachment: scroll !important;
}

.w-block {
  display: block;
}

.w-inline-block {
  max-width: 100%;
  display: inline-block;
}

.w-clearfix:before, .w-clearfix:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-clearfix:after {
  clear: both;
}

.w-hidden {
  display: none;
}

.w-button {
  color: #fff;
  line-height: inherit;
  cursor: pointer;
  background-color: #3898ec;
  border: 0;
  border-radius: 0;
  padding: 9px 15px;
  text-decoration: none;
  display: inline-block;
}

input.w-button {
  -webkit-appearance: button;
}

html[data-w-dynpage] [data-w-cloak] {
  color: rgba(0, 0, 0, 0) !important;
}


h1, h2, h3, h4, h5, h6 {
  margin-bottom: 10px;
  font-weight: bold;
}

h1 {
  margin-top: 20px;
  font-size: 38px;
  line-height: 44px;
}

h2 {
  margin-top: 20px;
  font-size: 32px;
  line-height: 36px;
}

h3 {
  margin-top: 20px;
  font-size: 24px;
  line-height: 30px;
}

h4 {
  margin-top: 10px;
  font-size: 18px;
  line-height: 24px;
}

h5 {
  margin-top: 10px;
  font-size: 14px;
  line-height: 20px;
}

h6 {
  margin-top: 10px;
  font-size: 12px;
  line-height: 18px;
}

p {
  margin-top: 0;
  margin-bottom: 10px;
}

blockquote {
  border-left: 5px solid #e2e2e2;
  margin: 0 0 10px;
  padding: 10px 20px;
  font-size: 18px;
  line-height: 22px;
}

figure {
  margin: 0 0 10px;
}

figcaption {
  text-align: center;
  margin-top: 5px;
}

ul, ol {
  margin-top: 0;
  margin-bottom: 10px;
  padding-left: 40px;
}

.w-list-unstyled {
  padding-left: 0;
  list-style: none;
}

.w-embed:before, .w-embed:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-embed:after {
  clear: both;
}

.w-video {
  width: 100%;
  padding: 0;
  position: relative;
}

.w-video iframe, .w-video object, .w-video embed {
  width: 100%;
  height: 100%;
  border: none;
  position: absolute;
  top: 0;
  left: 0;
}

fieldset {
  border: 0;
  margin: 0;
  padding: 0;
}

button, [type="button"], [type="reset"] {
  cursor: pointer;
  -webkit-appearance: button;
  border: 0;
}

.w-form {
  margin: 0 0 15px;
}

.w-form-fail {
  background-color: #ffdede;
  margin-top: 10px;
  padding: 10px;
  display: none;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
  display: block;
}

.w-input, .w-select {
  width: 100%;
  height: 38px;
  color: #333;
  vertical-align: middle;
  background-color: #fff;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  padding: 8px 12px;
  font-size: 14px;
  line-height: 1.42857;
  display: block;
}

.w-input:-moz-placeholder, .w-select:-moz-placeholder {
  color: #999;
}

.w-input::-moz-placeholder, .w-select::-moz-placeholder {
  color: #999;
  opacity: 1;
}

.w-input::-webkit-input-placeholder, .w-select::-webkit-input-placeholder {
  color: #999;
}

.w-input:focus, .w-select:focus {
  border-color: #3898ec;
  outline: 0;
}

.w-input[disabled], .w-select[disabled], .w-input[readonly], .w-select[readonly], fieldset[disabled] .w-input, fieldset[disabled] .w-select {
  cursor: not-allowed;
}

.w-input[disabled]:not(.w-input-disabled), .w-select[disabled]:not(.w-input-disabled), .w-input[readonly], .w-select[readonly], fieldset[disabled]:not(.w-input-disabled) .w-input, fieldset[disabled]:not(.w-input-disabled) .w-select {
  background-color: #eee;
}

textarea.w-input, textarea.w-select {
  height: auto;
}

.w-select {
  background-color: #f3f3f3;
}

.w-select[multiple] {
  height: auto;
}

.w-form-label {
  cursor: pointer;
  margin-bottom: 0;
  font-weight: normal;
  display: inline-block;
}

.w-radio {
  margin-bottom: 5px;
  padding-left: 20px;
  display: block;
}

.w-radio:before, .w-radio:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-radio:after {
  clear: both;
}

.w-radio-input {
  float: left;
  margin: 3px 0 0 -20px;
  line-height: normal;
}

.w-file-upload {
  margin-bottom: 10px;
  display: block;
}

.w-file-upload-input {
  width: .1px;
  height: .1px;
  opacity: 0;
  z-index: -100;
  position: absolute;
  overflow: hidden;
}

.w-file-upload-default, .w-file-upload-uploading, .w-file-upload-success {
  color: #333;
  display: inline-block;
}

.w-file-upload-error {
  margin-top: 10px;
  display: block;
}

.w-file-upload-default.w-hidden, .w-file-upload-uploading.w-hidden, .w-file-upload-error.w-hidden, .w-file-upload-success.w-hidden {
  display: none;
}

.w-file-upload-uploading-btn {
  cursor: pointer;
  background-color: #fafafa;
  border: 1px solid #ccc;
  margin: 0;
  padding: 8px 12px;
  font-size: 14px;
  font-weight: normal;
  display: flex;
}

.w-file-upload-file {
  background-color: #fafafa;
  border: 1px solid #ccc;
  flex-grow: 1;
  justify-content: space-between;
  margin: 0;
  padding: 8px 9px 8px 11px;
  display: flex;
}

.w-file-upload-file-name {
  font-size: 14px;
  font-weight: normal;
  display: block;
}

.w-file-remove-link {
  width: auto;
  height: auto;
  cursor: pointer;
  margin-top: 3px;
  margin-left: 10px;
  padding: 3px;
  display: block;
}

.w-icon-file-upload-remove {
  margin: auto;
  font-size: 10px;
}

.w-file-upload-error-msg {
  color: #ea384c;
  padding: 2px 0;
  display: inline-block;
}

.w-file-upload-info {
  padding: 0 12px;
  line-height: 38px;
  display: inline-block;
}

.w-file-upload-label {
  cursor: pointer;
  background-color: #fafafa;
  border: 1px solid #ccc;
  margin: 0;
  padding: 8px 12px;
  font-size: 14px;
  font-weight: normal;
  display: inline-block;
}

.w-icon-file-upload-icon, .w-icon-file-upload-uploading {
  width: 20px;
  margin-right: 8px;
  display: inline-block;
}

.w-icon-file-upload-uploading {
  height: 20px;
}

.w-container {
  max-width: 940px;
  margin-left: auto;
  margin-right: auto;
}

.w-container:before, .w-container:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-container:after {
  clear: both;
}

.w-container .w-row {
  margin-left: -10px;
  margin-right: -10px;
}

.w-row:before, .w-row:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-row:after {
  clear: both;
}

.w-row .w-row {
  margin-left: 0;
  margin-right: 0;
}

.w-col {
  float: left;
  width: 100%;
  min-height: 1px;
  padding-left: 10px;
  padding-right: 10px;
  position: relative;
}

.w-col .w-col {
  padding-left: 0;
  padding-right: 0;
}

.w-col-1 {
  width: 8.33333%;
}

.w-col-2 {
  width: 16.6667%;
}

.w-col-3 {
  width: 25%;
}

.w-col-4 {
  width: 33.3333%;
}

.w-col-5 {
  width: 41.6667%;
}

.w-col-6 {
  width: 50%;
}

.w-col-7 {
  width: 58.3333%;
}

.w-col-8 {
  width: 66.6667%;
}

.w-col-9 {
  width: 75%;
}

.w-col-10 {
  width: 83.3333%;
}

.w-col-11 {
  width: 91.6667%;
}

.w-col-12 {
  width: 100%;
}

.w-hidden-main {
  display: none !important;
}

@media screen and (max-width: 991px) {
  .w-container {
    max-width: 728px;
  }

  .w-hidden-main {
    display: inherit !important;
  }

  .w-hidden-medium {
    display: none !important;
  }

  .w-col-medium-1 {
    width: 8.33333%;
  }

  .w-col-medium-2 {
    width: 16.6667%;
  }

  .w-col-medium-3 {
    width: 25%;
  }

  .w-col-medium-4 {
    width: 33.3333%;
  }

  .w-col-medium-5 {
    width: 41.6667%;
  }

  .w-col-medium-6 {
    width: 50%;
  }

  .w-col-medium-7 {
    width: 58.3333%;
  }

  .w-col-medium-8 {
    width: 66.6667%;
  }

  .w-col-medium-9 {
    width: 75%;
  }

  .w-col-medium-10 {
    width: 83.3333%;
  }

  .w-col-medium-11 {
    width: 91.6667%;
  }

  .w-col-medium-12 {
    width: 100%;
  }

  .w-col-stack {
    width: 100%;
    left: auto;
    right: auto;
  }
}

@media screen and (max-width: 767px) {
  .w-hidden-main, .w-hidden-medium {
    display: inherit !important;
  }

  .w-hidden-small {
    display: none !important;
  }

  .w-row, .w-container .w-row {
    margin-left: 0;
    margin-right: 0;
  }

  .w-col {
    width: 100%;
    left: auto;
    right: auto;
  }

  .w-col-small-1 {
    width: 8.33333%;
  }

  .w-col-small-2 {
    width: 16.6667%;
  }

  .w-col-small-3 {
    width: 25%;
  }

  .w-col-small-4 {
    width: 33.3333%;
  }

  .w-col-small-5 {
    width: 41.6667%;
  }

  .w-col-small-6 {
    width: 50%;
  }

  .w-col-small-7 {
    width: 58.3333%;
  }

  .w-col-small-8 {
    width: 66.6667%;
  }

  .w-col-small-9 {
    width: 75%;
  }

  .w-col-small-10 {
    width: 83.3333%;
  }

  .w-col-small-11 {
    width: 91.6667%;
  }

  .w-col-small-12 {
    width: 100%;
  }
}

@media screen and (max-width: 479px) {
  .w-container {
    max-width: none;
  }

  .w-hidden-main, .w-hidden-medium, .w-hidden-small {
    display: inherit !important;
  }

  .w-hidden-tiny {
    display: none !important;
  }

  .w-col {
    width: 100%;
  }

  .w-col-tiny-1 {
    width: 8.33333%;
  }

  .w-col-tiny-2 {
    width: 16.6667%;
  }

  .w-col-tiny-3 {
    width: 25%;
  }

  .w-col-tiny-4 {
    width: 33.3333%;
  }

  .w-col-tiny-5 {
    width: 41.6667%;
  }

  .w-col-tiny-6 {
    width: 50%;
  }

  .w-col-tiny-7 {
    width: 58.3333%;
  }

  .w-col-tiny-8 {
    width: 66.6667%;
  }

  .w-col-tiny-9 {
    width: 75%;
  }

  .w-col-tiny-10 {
    width: 83.3333%;
  }

  .w-col-tiny-11 {
    width: 91.6667%;
  }

  .w-col-tiny-12 {
    width: 100%;
  }
}

.w-widget {
  position: relative;
}

.w-widget-map {
  width: 100%;
  height: 400px;
}

.w-widget-map label {
  width: auto;
  display: inline;
}

.w-widget-map img {
  max-width: inherit;
}

.w-widget-map .gm-style-iw {
  text-align: center;
}

.w-widget-map .gm-style-iw > button {
  display: none !important;
}

.w-widget-twitter {
  overflow: hidden;
}

.w-widget-twitter-count-shim {
  vertical-align: top;
  width: 28px;
  height: 20px;
  text-align: center;
  background: #fff;
  border: 1px solid #758696;
  border-radius: 3px;
  display: inline-block;
  position: relative;
}

.w-widget-twitter-count-shim * {
  pointer-events: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.w-widget-twitter-count-shim .w-widget-twitter-count-inner {
  text-align: center;
  color: #999;
  font-family: serif;
  font-size: 15px;
  line-height: 12px;
  position: relative;
}

.w-widget-twitter-count-shim .w-widget-twitter-count-clear {
  display: block;
  position: relative;
}

.w-widget-twitter-count-shim.w--large {
  width: 36px;
  height: 28px;
}

.w-widget-twitter-count-shim.w--large .w-widget-twitter-count-inner {
  font-size: 18px;
  line-height: 18px;
}

.w-widget-twitter-count-shim:not(.w--vertical) {
  margin-left: 5px;
  margin-right: 8px;
}

.w-widget-twitter-count-shim:not(.w--vertical).w--large {
  margin-left: 6px;
}

.w-widget-twitter-count-shim:not(.w--vertical):before, .w-widget-twitter-count-shim:not(.w--vertical):after {
  content: " ";
  height: 0;
  width: 0;
  pointer-events: none;
  border: solid rgba(0, 0, 0, 0);
  position: absolute;
  top: 50%;
  left: 0;
}

.w-widget-twitter-count-shim:not(.w--vertical):before {
  border-width: 4px;
  border-color: rgba(117, 134, 150, 0) #5d6c7b rgba(117, 134, 150, 0) rgba(117, 134, 150, 0);
  margin-top: -4px;
  margin-left: -9px;
}

.w-widget-twitter-count-shim:not(.w--vertical).w--large:before {
  border-width: 5px;
  margin-top: -5px;
  margin-left: -10px;
}

.w-widget-twitter-count-shim:not(.w--vertical):after {
  border-width: 4px;
  border-color: rgba(255, 255, 255, 0) #fff rgba(255, 255, 255, 0) rgba(255, 255, 255, 0);
  margin-top: -4px;
  margin-left: -8px;
}

.w-widget-twitter-count-shim:not(.w--vertical).w--large:after {
  border-width: 5px;
  margin-top: -5px;
  margin-left: -9px;
}

.w-widget-twitter-count-shim.w--vertical {
  width: 61px;
  height: 33px;
  margin-bottom: 8px;
}

.w-widget-twitter-count-shim.w--vertical:before, .w-widget-twitter-count-shim.w--vertical:after {
  content: " ";
  height: 0;
  width: 0;
  pointer-events: none;
  border: solid rgba(0, 0, 0, 0);
  position: absolute;
  top: 100%;
  left: 50%;
}

.w-widget-twitter-count-shim.w--vertical:before {
  border-width: 5px;
  border-color: #5d6c7b rgba(117, 134, 150, 0) rgba(117, 134, 150, 0);
  margin-left: -5px;
}

.w-widget-twitter-count-shim.w--vertical:after {
  border-width: 4px;
  border-color: #fff rgba(255, 255, 255, 0) rgba(255, 255, 255, 0);
  margin-left: -4px;
}

.w-widget-twitter-count-shim.w--vertical .w-widget-twitter-count-inner {
  font-size: 18px;
  line-height: 22px;
}

.w-widget-twitter-count-shim.w--vertical.w--large {
  width: 76px;
}

.w-background-video {
  height: 500px;
  color: #fff;
  position: relative;
  overflow: hidden;
}

.w-background-video > video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -100;
  background-position: 50%;
  background-size: cover;
  margin: auto;
  position: absolute;
  top: -100%;
  bottom: -100%;
  left: -100%;
  right: -100%;
}

.w-background-video > video::-webkit-media-controls-start-playback-button {
  -webkit-appearance: none;
  display: none !important;
}

.w-background-video--control {
  background-color: rgba(0, 0, 0, 0);
  padding: 0;
  position: absolute;
  bottom: 1em;
  right: 1em;
}

.w-background-video--control > [hidden] {
  display: none !important;
}

.w-slider {
  height: 300px;
  text-align: center;
  clear: both;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  tap-highlight-color: rgba(0, 0, 0, 0);
  background: #ddd;
  position: relative;
}

.w-slider-mask {
  z-index: 1;
  height: 100%;
  white-space: nowrap;
  display: block;
  position: relative;
  left: 0;
  right: 0;
  overflow: hidden;
}

.w-slide {
  vertical-align: top;
  width: 100%;
  height: 100%;
  white-space: normal;
  text-align: left;
  display: inline-block;
  position: relative;
}

.w-slider-nav {
  z-index: 2;
  height: 40px;
  text-align: center;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  tap-highlight-color: rgba(0, 0, 0, 0);
  margin: auto;
  padding-top: 10px;
  position: absolute;
  top: auto;
  bottom: 0;
  left: 0;
  right: 0;
}

.w-slider-nav.w-round > div {
  border-radius: 100%;
}

.w-slider-nav.w-num > div {
  width: auto;
  height: auto;
  font-size: inherit;
  line-height: inherit;
  padding: .2em .5em;
}

.w-slider-nav.w-shadow > div {
  box-shadow: 0 0 3px rgba(51, 51, 51, .4);
}

.w-slider-nav-invert {
  color: #fff;
}

.w-slider-nav-invert > div {
  background-color: rgba(34, 34, 34, .4);
}

.w-slider-nav-invert > div.w-active {
  background-color: #222;
}

.w-slider-dot {
  width: 1em;
  height: 1em;
  cursor: pointer;
  background-color: rgba(255, 255, 255, .4);
  margin: 0 3px .5em;
  transition: background-color .1s, color .1s;
  display: inline-block;
  position: relative;
}

.w-slider-dot.w-active {
  background-color: #fff;
}

.w-slider-dot:focus {
  outline: none;
  box-shadow: 0 0 0 2px #fff;
}

.w-slider-dot:focus.w-active {
  box-shadow: none;
}

.w-slider-arrow-left, .w-slider-arrow-right {
  width: 80px;
  cursor: pointer;
  color: #fff;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
  margin: auto;
  font-size: 40px;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
}

.w-slider-arrow-left [class^="w-icon-"], .w-slider-arrow-right [class^="w-icon-"], .w-slider-arrow-left [class*=" w-icon-"], .w-slider-arrow-right [class*=" w-icon-"] {
  position: absolute;
}

.w-slider-arrow-left:focus, .w-slider-arrow-right:focus {
  outline: 0;
}

.w-slider-arrow-left {
  z-index: 3;
  right: auto;
}

.w-slider-arrow-right {
  z-index: 4;
  left: auto;
}

.w-icon-slider-left, .w-icon-slider-right {
  width: 1em;
  height: 1em;
  margin: auto;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.w-slider-aria-label {
  clip: rect(0 0 0 0);
  height: 1px;
  width: 1px;
  border: 0;
  margin: -1px;
  padding: 0;
  position: absolute;
  overflow: hidden;
}

.w-slider-force-show {
  display: block !important;
}

.w-dropdown {
  text-align: left;
  z-index: 900;
  margin-left: auto;
  margin-right: auto;
  display: inline-block;
  position: relative;
}

.w-dropdown-btn, .w-dropdown-toggle, .w-dropdown-link {
  vertical-align: top;
  color: #222;
  text-align: left;
  white-space: nowrap;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  text-decoration: none;
  position: relative;
}

.w-dropdown-toggle {
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
  cursor: pointer;
  padding-right: 40px;
  display: inline-block;
}

.w-dropdown-toggle:focus {
  outline: 0;
}

.w-icon-dropdown-toggle {
  width: 1em;
  height: 1em;
  margin: auto 20px auto auto;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
}

.w-dropdown-list {
  min-width: 100%;
  background: #ddd;
  display: none;
  position: absolute;
}

.w-dropdown-list.w--open {
  display: block;
}

.w-dropdown-link {
  color: #222;
  padding: 10px 20px;
  display: block;
}

.w-dropdown-link.w--current {
  color: #0082f3;
}

.w-dropdown-link:focus {
  outline: 0;
}

@media screen and (max-width: 767px) {
  .w-nav-brand {
    padding-left: 10px;
  }
}

.w-lightbox-backdrop {
  cursor: auto;
  letter-spacing: normal;
  text-indent: 0;
  text-shadow: none;
  text-transform: none;
  visibility: visible;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  color: #fff;
  text-align: center;
  z-index: 2000;
  opacity: 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  -webkit-tap-highlight-color: transparent;
  background: rgba(0, 0, 0, .9);
  outline: 0;
  font-family: Helvetica Neue, Helvetica, Ubuntu, Segoe UI, Verdana, sans-serif;
  font-size: 17px;
  font-style: normal;
  font-weight: 300;
  line-height: 1.2;
  list-style: disc;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  -webkit-transform: translate(0);
}

.w-lightbox-backdrop, .w-lightbox-container {
  height: 100%;
  -webkit-overflow-scrolling: touch;
  overflow: auto;
}

.w-lightbox-content {
  height: 100vh;
  position: relative;
  overflow: hidden;
}

.w-lightbox-view {
  width: 100vw;
  height: 100vh;
  opacity: 0;
  position: absolute;
}

.w-lightbox-view:before {
  content: "";
  height: 100vh;
}

.w-lightbox-group, .w-lightbox-group .w-lightbox-view, .w-lightbox-group .w-lightbox-view:before {
  height: 86vh;
}

.w-lightbox-frame, .w-lightbox-view:before {
  vertical-align: middle;
  display: inline-block;
}

.w-lightbox-figure {
  margin: 0;
  position: relative;
}

.w-lightbox-group .w-lightbox-figure {
  cursor: pointer;
}

.w-lightbox-img {
  width: auto;
  height: auto;
  max-width: none;
}

.w-lightbox-image {
  float: none;
  max-width: 100vw;
  max-height: 100vh;
  display: block;
}

.w-lightbox-group .w-lightbox-image {
  max-height: 86vh;
}

.w-lightbox-caption {
  text-align: left;
  text-overflow: ellipsis;
  white-space: nowrap;
  background: rgba(0, 0, 0, .4);
  padding: .5em 1em;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
}

.w-lightbox-embed {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.w-lightbox-control {
  width: 4em;
  cursor: pointer;
  background-position: center;
  background-repeat: no-repeat;
  background-size: 24px;
  transition: all .3s;
  position: absolute;
  top: 0;
}

.w-lightbox-left {
  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0yMCAwIDI0IDQwIiB3aWR0aD0iMjQiIGhlaWdodD0iNDAiPjxnIHRyYW5zZm9ybT0icm90YXRlKDQ1KSI+PHBhdGggZD0ibTAgMGg1djIzaDIzdjVoLTI4eiIgb3BhY2l0eT0iLjQiLz48cGF0aCBkPSJtMSAxaDN2MjNoMjN2M2gtMjZ6IiBmaWxsPSIjZmZmIi8+PC9nPjwvc3ZnPg==");
  display: none;
  bottom: 0;
  left: 0;
}

.w-lightbox-right {
  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii00IDAgMjQgNDAiIHdpZHRoPSIyNCIgaGVpZ2h0PSI0MCI+PGcgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48cGF0aCBkPSJtMC0waDI4djI4aC01di0yM2gtMjN6IiBvcGFjaXR5PSIuNCIvPjxwYXRoIGQ9Im0xIDFoMjZ2MjZoLTN2LTIzaC0yM3oiIGZpbGw9IiNmZmYiLz48L2c+PC9zdmc+");
  display: none;
  bottom: 0;
  right: 0;
}

.w-lightbox-close {
  height: 2.6em;
  background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii00IDAgMTggMTciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxNyI+PGcgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48cGF0aCBkPSJtMCAwaDd2LTdoNXY3aDd2NWgtN3Y3aC01di03aC03eiIgb3BhY2l0eT0iLjQiLz48cGF0aCBkPSJtMSAxaDd2LTdoM3Y3aDd2M2gtN3Y3aC0zdi03aC03eiIgZmlsbD0iI2ZmZiIvPjwvZz48L3N2Zz4=");
  background-size: 18px;
  right: 0;
}

.w-lightbox-strip {
  white-space: nowrap;
  padding: 0 1vh;
  line-height: 0;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  overflow-x: auto;
  overflow-y: hidden;
}

.w-lightbox-item {
  width: 10vh;
  box-sizing: content-box;
  cursor: pointer;
  padding: 2vh 1vh;
  display: inline-block;
  -webkit-transform: translate3d(0, 0, 0);
}

.w-lightbox-active {
  opacity: .3;
}

.w-lightbox-thumbnail {
  height: 10vh;
  background: #222;
  position: relative;
  overflow: hidden;
}

.w-lightbox-thumbnail-image {
  position: absolute;
  top: 0;
  left: 0;
}

.w-lightbox-thumbnail .w-lightbox-tall {
  width: 100%;
  top: 50%;
  transform: translate(0, -50%);
}

.w-lightbox-thumbnail .w-lightbox-wide {
  height: 100%;
  left: 50%;
  transform: translate(-50%);
}

.w-lightbox-spinner {
  box-sizing: border-box;
  width: 40px;
  height: 40px;
  border: 5px solid rgba(0, 0, 0, .4);
  border-radius: 50%;
  margin-top: -20px;
  margin-left: -20px;
  animation: .8s linear infinite spin;
  position: absolute;
  top: 50%;
  left: 50%;
}

.w-lightbox-spinner:after {
  content: "";
  border: 3px solid rgba(0, 0, 0, 0);
  border-bottom-color: #fff;
  border-radius: 50%;
  position: absolute;
  top: -4px;
  bottom: -4px;
  left: -4px;
  right: -4px;
}

.w-lightbox-hide {
  display: none;
}

.w-lightbox-noscroll {
  overflow: hidden;
}

@media (min-width: 768px) {
  .w-lightbox-content {
    height: 96vh;
    margin-top: 2vh;
  }

  .w-lightbox-view, .w-lightbox-view:before {
    height: 96vh;
  }

  .w-lightbox-group, .w-lightbox-group .w-lightbox-view, .w-lightbox-group .w-lightbox-view:before {
    height: 84vh;
  }

  .w-lightbox-image {
    max-width: 96vw;
    max-height: 96vh;
  }

  .w-lightbox-group .w-lightbox-image {
    max-width: 82.3vw;
    max-height: 84vh;
  }

  .w-lightbox-left, .w-lightbox-right {
    opacity: .5;
    display: block;
  }

  .w-lightbox-close {
    opacity: .8;
  }

  .w-lightbox-control:hover {
    opacity: 1;
  }
}

.w-lightbox-inactive, .w-lightbox-inactive:hover {
  opacity: 0;
}

.w-richtext:before, .w-richtext:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-richtext:after {
  clear: both;
}

.w-richtext[contenteditable="true"]:before, .w-richtext[contenteditable="true"]:after {
  white-space: initial;
}

.w-richtext ol, .w-richtext ul {
  overflow: hidden;
}

.w-richtext .w-richtext-figure-selected.w-richtext-figure-type-video div:after, .w-richtext .w-richtext-figure-selected[data-rt-type="video"] div:after, .w-richtext .w-richtext-figure-selected.w-richtext-figure-type-image div, .w-richtext .w-richtext-figure-selected[data-rt-type="image"] div {
  outline: 2px solid #2895f7;
}

.w-richtext figure.w-richtext-figure-type-video > div:after, .w-richtext figure[data-rt-type="video"] > div:after {
  content: "";
  display: none;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.w-richtext figure {
  max-width: 60%;
  position: relative;
}

.w-richtext figure > div:before {
  cursor: default !important;
}

.w-richtext figure img {
  width: 100%;
}

.w-richtext figure figcaption.w-richtext-figcaption-placeholder {
  opacity: .6;
}

.w-richtext figure div {
  color: rgba(0, 0, 0, 0);
  font-size: 0;
}

.w-richtext figure.w-richtext-figure-type-image, .w-richtext figure[data-rt-type="image"] {
  display: table;
}

.w-richtext figure.w-richtext-figure-type-image > div, .w-richtext figure[data-rt-type="image"] > div {
  display: inline-block;
}

.w-richtext figure.w-richtext-figure-type-image > figcaption, .w-richtext figure[data-rt-type="image"] > figcaption {
  caption-side: bottom;
  display: table-caption;
}

.w-richtext figure.w-richtext-figure-type-video, .w-richtext figure[data-rt-type="video"] {
  width: 60%;
  height: 0;
}

.w-richtext figure.w-richtext-figure-type-video iframe, .w-richtext figure[data-rt-type="video"] iframe {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.w-richtext figure.w-richtext-figure-type-video > div, .w-richtext figure[data-rt-type="video"] > div {
  width: 100%;
}

.w-richtext figure.w-richtext-align-center {
  clear: both;
  margin-left: auto;
  margin-right: auto;
}

.w-richtext figure.w-richtext-align-center.w-richtext-figure-type-image > div, .w-richtext figure.w-richtext-align-center[data-rt-type="image"] > div {
  max-width: 100%;
}

.w-richtext figure.w-richtext-align-normal {
  clear: both;
}

.w-richtext figure.w-richtext-align-fullwidth {
  width: 100%;
  max-width: 100%;
  text-align: center;
  clear: both;
  margin-left: auto;
  margin-right: auto;
  display: block;
}

.w-richtext figure.w-richtext-align-fullwidth > div {
  padding-bottom: inherit;
  display: inline-block;
}

.w-richtext figure.w-richtext-align-fullwidth > figcaption {
  display: block;
}

.w-richtext figure.w-richtext-align-floatleft {
  float: left;
  clear: none;
  margin-right: 15px;
}

.w-richtext figure.w-richtext-align-floatright {
  float: right;
  clear: none;
  margin-left: 15px;
}

.w-nav {
  z-index: 1000;
  background: #ddd;
  position: relative;
}

.w-nav:before, .w-nav:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-nav:after {
  clear: both;
}

.w-nav-brand {
  float: left;
  color: #333;
  text-decoration: none;
  position: relative;
}

.w-nav-link {
  vertical-align: top;
  color: #222;
  text-align: left;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  text-decoration: none;
  display: inline-block;
  position: relative;
}

.w-nav-link.w--current {
  color: #0082f3;
}

.w-nav-menu {
  float: right;
  position: relative;
}

[data-nav-menu-open] {
  text-align: center;
  min-width: 200px;
  background: #c8c8c8;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  overflow: visible;
  display: block !important;
}

.w--nav-link-open {
  display: block;
  position: relative;
}

.w-nav-overlay {
  width: 100%;
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  overflow: hidden;
}

.w-nav-overlay [data-nav-menu-open] {
  top: 0;
}

.w-nav[data-animation="over-left"] .w-nav-overlay {
  width: auto;
}

.w-nav[data-animation="over-left"] .w-nav-overlay, .w-nav[data-animation="over-left"] [data-nav-menu-open] {
  z-index: 1;
  top: 0;
  right: auto;
}

.w-nav[data-animation="over-right"] .w-nav-overlay {
  width: auto;
}

.w-nav[data-animation="over-right"] .w-nav-overlay, .w-nav[data-animation="over-right"] [data-nav-menu-open] {
  z-index: 1;
  top: 0;
  left: auto;
}

.w-nav-button {
  float: right;
  cursor: pointer;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
  padding: 18px;
  font-size: 24px;
  display: none;
  position: relative;
}

.w-nav-button:focus {
  outline: 0;
}

.w-nav-button.w--open {
  color: #fff;
  background-color: #c8c8c8;
}

.w-nav[data-collapse="all"] .w-nav-menu {
  display: none;
}

.w-nav[data-collapse="all"] .w-nav-button, .w--nav-dropdown-open, .w--nav-dropdown-toggle-open {
  display: block;
}

.w--nav-dropdown-list-open {
  position: static;
}

@media screen and (max-width: 991px) {
  .w-nav[data-collapse="medium"] .w-nav-menu {
    display: none;
  }

  .w-nav[data-collapse="medium"] .w-nav-button {
    display: block;
  }
}

@media screen and (max-width: 767px) {
  .w-nav[data-collapse="small"] .w-nav-menu {
    display: none;
  }

  .w-nav[data-collapse="small"] .w-nav-button {
    display: block;
  }

  .w-nav-brand {
    padding-left: 10px;
  }
}

@media screen and (max-width: 479px) {
  .w-nav[data-collapse="tiny"] .w-nav-menu {
    display: none;
  }

  .w-nav[data-collapse="tiny"] .w-nav-button {
    display: block;
  }
}

.w-tabs {
  position: relative;
}

.w-tabs:before, .w-tabs:after {
  content: " ";
  grid-area: 1 / 1 / 2 / 2;
  display: table;
}

.w-tabs:after {
  clear: both;
}

.w-tab-menu {
  position: relative;
}

.w-tab-link {
  vertical-align: top;
  text-align: left;
  cursor: pointer;
  color: #222;
  background-color: #ddd;
  padding: 9px 30px;
  text-decoration: none;
  display: inline-block;
  position: relative;
}

.w-tab-link.w--current {
  background-color: #c8c8c8;
}

.w-tab-link:focus {
  outline: 0;
}

.w-tab-content {
  display: block;
  position: relative;
  overflow: hidden;
}

.w-tab-pane {
  display: none;
  position: relative;
}

.w--tab-active {
  display: block;
}

@media screen and (max-width: 479px) {
  .w-tab-link {
    display: block;
  }
}

.w-ix-emptyfix:after {
  content: "";
}

@keyframes spin {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}

.w-dyn-empty {
  background-color: #ddd;
  padding: 10px;
}

.w-dyn-hide, .w-dyn-bind-empty, .w-condition-invisible {
  display: none !important;
}

.wf-layout-layout {
  display: grid;
}

.navbar-logo-left {
  width: 100%;
  max-width: 1440px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #fff;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.navbar-brand {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-2 {
  color: #000;
  font-size: 14px;
  font-weight: 400;
  line-height: 150%;
}

.navbar-menu {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-3 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.desktop---1 {
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  background-color: rgba(88, 78, 59, 0);
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-2 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-2 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-2 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-2 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-2 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-2 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-4 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-2 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-2, .navbar-link-3, .navbar-link-4 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-2 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-5 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left {
  width: 100%;
  height: 512px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.title-copy-goes-here-be-awesome {
  color: #000;
  font-size: 56px;
  font-weight: 700;
  line-height: 120%;
}

.error-b752fee3-6f00-1a55-ba86-9bb2c9503ac2 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions {
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.column-2 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-3 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-comparison {
  width: 100%;
  height: 458px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns {
  width: 100%;
  height: 452px;
  max-width: 1106px;
  grid-column-gap: 15px;
  grid-row-gap: 15px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-3 {
  width: 100%;
  height: 439px;
  max-width: 260px;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.intro {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 32px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.image-wrapper-2 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-1 {
  width: 183px;
  height: 115px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.name {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-6 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-7 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.pricing {
  width: 100%;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  justify-content: center;
  align-items: flex-end;
  display: flex;
}

.text-8 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.text-9 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-2 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-10 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-4 {
  width: 100%;
  height: 439px;
  max-width: 260px;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-3 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-11 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-12 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-4 {
  width: 100%;
  height: 52px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.hacer-pedido {
  color: #fff;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-1 {
  color: #212121;
  font-size: 18px;
  font-weight: 700;
  line-height: 150%;
}

.image-4 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-13 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-14 {
  color: #000;
  font-size: 14px;
  font-weight: 400;
  line-height: 150%;
}

.navbar-menu-3 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-5 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.text-15 {
  color: #000;
  font-size: 14px;
  font-weight: 400;
  line-height: 150%;
}

.navbar-link-6 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-3 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-16 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-2 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-2 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-5 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-3 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.button-5 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.column-6 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-3 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-5 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-comparison-2 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-2 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-7 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.image-wrapper-4 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-17 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-18 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-19 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.description {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-20 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-6 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-21 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-8 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-7 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-22 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-23 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-8 {
  width: 100%;
  height: 52px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-2 {
  color: #212121;
  font-size: 18px;
  font-weight: 700;
  line-height: 150%;
}

.content-4 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-6 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-24 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-4 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-25 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.content-5 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.button-9 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.column-9 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-5 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-7 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-comparison-3 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-3 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-10 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.image-wrapper-6 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-26 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-27 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-28 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.text-29 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.text-30 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-11 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-10 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-31 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-32 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-11 {
  width: 100%;
  height: 52px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-3 {
  color: #212121;
  font-size: 18px;
  font-weight: 700;
  line-height: 150%;
}

.text-33 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-12 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-7 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-8 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-6 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.button-12 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-4 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-4 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-13 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.image-wrapper-8 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-34 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-35 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-36 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.text-37 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.text-38 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-14 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-13 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-39 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-40 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-14 {
  width: 100%;
  height: 52px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-4 {
  color: #212121;
  font-size: 18px;
  font-weight: 700;
  line-height: 150%;
}

.desktop---4 {
  width: 100%;
  height: 1022px;
  max-width: 1268px;
  grid-column-gap: 65px;
  grid-row-gap: 65px;
  background-color: rgba(88, 78, 59, 0);
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-3 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-3 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-3 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-7 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-3 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-9 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-41 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-5 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-7, .navbar-link-8, .navbar-link-9 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-4 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-42 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.team-circles {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 24px 64px;
  display: flex;
}

.container-3 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 85px;
  grid-row-gap: 85px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.columns-5 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.card {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-wrapper-9 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-10 {
  width: 180px;
  height: 180px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-8 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.info {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-43 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
}

.text-44 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.description-2 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.title-section {
  width: 100%;
  max-width: 530px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-45 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.desktop---5 {
  width: 100%;
  height: 1022px;
  max-width: 1268px;
  grid-column-gap: 65px;
  grid-row-gap: 65px;
  background-color: rgba(88, 78, 59, 0);
  flex-flow: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-4 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-4 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-4 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-9 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-4 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-11 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-46 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-6 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-10, .navbar-link-11, .navbar-link-12 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-5 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-47 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.container-4 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 58px;
  grid-row-gap: 58px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.columns-6 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-wrapper-10 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-12 {
  width: 100px;
  height: 100px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-10 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-48 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
}

.text-49 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.description-3 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.text-50 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.desktop---6 {
  width: 100%;
  max-width: 1268px;
  grid-column-gap: 65px;
  grid-row-gap: 65px;
  background-color: rgba(88, 78, 59, 0);
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-5 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-5 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-5 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-11 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-5 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-13, .navbar-link-14, .navbar-link-15 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-6 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-51 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.container-5 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 58px;
  grid-row-gap: 58px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.columns-7 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-wrapper-11 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-13 {
  width: 100px;
  height: 100px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-12 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-52 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
}

.text-53 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.description-4 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.text-54 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.desktop---7 {
  width: 100%;
  max-width: 1268px;
  grid-column-gap: 65px;
  grid-row-gap: 65px;
  background-color: #584e3b;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px;
  display: flex;
}

.content-13 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-link-16, .navbar-link-17, .navbar-link-18 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-7 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-55 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.container-6 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 58px;
  grid-row-gap: 58px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.columns-8 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-wrapper-12 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-14 {
  width: 100px;
  height: 100px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-14 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-56 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
}

.text-57 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.description-5 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.text-58 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.desktop---8 {
  grid-column-gap: 37px;
  grid-row-gap: 37px;
  background-color: rgba(88, 78, 59, 0);
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  display: flex;
}

.content-15 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-link-19, .navbar-link-20 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-8 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-59 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-3 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-7 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-15 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-13 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-15 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-16 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-16 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.error-d543413a-d1a2-674f-377e-248198feb8ae {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions-2 {
  height: 67px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-15 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-5 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-9 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-17 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.intro-2 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 32px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.image-wrapper-14 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-1-2 {
  width: 183px;
  height: 115px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.name-2 {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-60 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-61 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.pricing-2 {
  width: 100%;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  justify-content: center;
  align-items: flex-end;
  display: flex;
}

.text-62 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.description-6 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-63 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-16 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-64 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-18 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-17 {
  width: 100%;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-65 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-66 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-18 {
  width: 100%;
  height: 52px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.hacer-pedido-2 {
  color: #fff;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.container-8 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 58px;
  grid-row-gap: 58px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.columns-10 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-16 {
  width: 100px;
  height: 100px;
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  object-fit: cover;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-67 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
}

.text-68 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.description-7 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.text-69 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-0 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.desktop---9 {
  grid-column-gap: 37px;
  grid-row-gap: 37px;
  background-color: #584e3b;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-6 {
  width: 100%;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-6 {
  width: 100%;
  max-width: 1200px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-6 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-17 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-6 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-17 {
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-70 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-7 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-21, .navbar-link-22 {
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.navbar-button-9 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 8px 20px;
  display: flex;
}

.text-71 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-4 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-9 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-19 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-15 {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-18 {
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-20 {
  width: 100%;
  max-width: 560px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-18 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.error-dcda2372-13e2-fe2c-8cb3-c1ef879690f8 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions-3 {
  height: 67px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-19 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-6 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-11 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-21 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.intro-3 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 32px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.image-wrapper-16 {
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.pricing-1-3 {
  width: 183px;
  height: 115px;
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.name-3 {
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-72 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-73 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.pricing-3 {
  width: 100%;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  justify-content: center;
  align-items: flex-end;
  display: flex;
}

.text-74 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.description-8 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-75 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-20 {
  width: 100%;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-76 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-22 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-21 {
  width: 100%;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-77 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-78 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-22 {
  width: 100%;
  height: 52px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.hacer-pedido-3 {
  color: #fff;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.team-circles-2 {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 24px 64px;
  display: flex;
}

.container-10 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 53px;
  grid-row-gap: 53px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.title-section-2 {
  width: 100%;
  max-width: 530px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-79 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.error-dcda2372-13e2-fe2c-8cb3-c1ef87969114 {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-weight: 400;
  line-height: 150%;
}

.columns-12 {
  width: 100%;
  height: 500px;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.card-2 {
  width: 100%;
  height: 500px;
  max-width: 368px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.image-wrapper-17 {
  width: 120px;
  height: 120px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-1 {
  object-fit: cover;
  border-radius: 250px;
}

.content-19 {
  width: 100%;
  height: 370px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.info-2 {
  width: 100%;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-80 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
  text-decoration: underline;
}

.text-81 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  line-height: 150%;
}

.card-3 {
  width: 100%;
  height: 500px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.card-4 {
  width: 100%;
  height: 500px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  opacity: .99;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.hero-heading-right {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 64px 24px;
  display: flex;
}

.container-11 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-23 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-18 {
  width: 100%;
  height: 500px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-82 {
  color: #000;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.error-dcda2372-13e2-fe2c-8cb3-c1ef87969124 {
  color: #212121;
  font-size: 18px;
  font-weight: 600;
  line-height: 150%;
}

.actions-4 {
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-23 {
  width: 124px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.button-24 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
  text-decoration: none;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-5 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.desktop---10 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  background-color: #584e3b;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-7 {
  width: 100%;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-7 {
  width: 100%;
  max-width: 1200px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-7 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-20 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-7 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-19 {
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-83 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-8 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-23, .navbar-link-24 {
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.text-84 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-5 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-12 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-24 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-19 {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-20 {
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-25 {
  width: 100%;
  max-width: 560px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-21 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-6 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions-5 {
  height: 67px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-25 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-7 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-13 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-26 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.intro-4 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 32px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.image-wrapper-20 {
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-85 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-86 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-87 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.description-9 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.text-88 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-26 {
  width: 100%;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-89 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-27 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-27 {
  width: 100%;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-90 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-91 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-28 {
  width: 100%;
  height: 52px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.team-circles-3 {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 24px 64px;
  display: flex;
}

.container-13 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 160px;
  grid-row-gap: 160px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-92 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.columns-14 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.card-5 {
  width: 100%;
  height: 350px;
  max-width: 368px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.image-wrapper-21 {
  width: 120px;
  height: 120px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-22 {
  width: 100%;
  height: 370px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-93 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
  text-decoration: underline;
}

.text-94 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  line-height: 150%;
}

.card-6 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.card-7 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  opacity: .99;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.hero-heading-right-2 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  margin-top: -100px;
  padding-bottom: 64px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.container-14 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-28 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-22 {
  width: 100%;
  height: 500px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-95 {
  color: #000;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.button-29 {
  width: 124px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.button-30 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
  text-decoration: none;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-7 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.desktop---11 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  background-color: #584e3b;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  display: flex;
}

.navbar-logo-left-8 {
  width: 100%;
  justify-content: center;
  align-items: flex-start;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.navbarcontainer-8 {
  width: 100%;
  max-width: 1200px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-8 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-23 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-8 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-21 {
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-96 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-9 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-25, .navbar-link-26 {
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.text-97 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-6 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-15 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-wrapper-23 {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-22 {
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-29 {
  width: 100%;
  max-width: 560px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-24 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-8 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions-6 {
  height: 67px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-31 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-8 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-15 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-30 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.image-wrapper-24 {
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-98 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-99 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-100 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.text-101 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-32 {
  width: 100%;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-102 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-31 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.button-33 {
  width: 100%;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-103 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-104 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-34 {
  width: 100%;
  height: 52px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.team-circles-4 {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 24px 64px;
  display: flex;
}

.container-16 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 160px;
  grid-row-gap: 160px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-105 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.columns-16 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.card-8 {
  width: 100%;
  height: 350px;
  max-width: 368px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.image-wrapper-25 {
  width: 120px;
  height: 120px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-25 {
  width: 100%;
  height: 370px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.info-3 {
  width: 100%;
  max-width: 300px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-106 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
  text-decoration: underline;
}

.text-107 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  line-height: 150%;
}

.card-9 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.card-10 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  opacity: .99;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.container-17 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-32 {
  width: 100%;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-26 {
  width: 100%;
  height: 500px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-108 {
  color: #000;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.button-35 {
  width: 124px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.button-36 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
  text-decoration: none;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-9 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.navbarcontainer-9 {
  width: 100%;
  max-width: 1200px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.navbar-content-9 {
  width: 100%;
  max-width: 1200px;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.content-26 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.author-9 {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-23 {
  object-fit: cover;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-109 {
  width: 100%;
  max-width: 308px;
  grid-column-gap: 4px;
  grid-row-gap: 4px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.navbar-menu-10 {
  grid-column-gap: 32px;
  grid-row-gap: 32px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.navbar-link-27, .navbar-link-28 {
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 24px 12px;
  display: flex;
}

.text-110 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.hero-heading-left-7 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding: 33px 24px 11px;
  display: flex;
}

.container-18 {
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.column-33 {
  width: 100%;
  max-width: 560px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.image-wrapper-27 {
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.image-24 {
  object-fit: cover;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-34 {
  width: 100%;
  max-width: 560px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.content-27 {
  width: 100%;
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-10 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.actions-7 {
  height: 67px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex: 0 auto;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 16px;
  display: flex;
}

.button-37 {
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.pricing-comparison-9 {
  width: 100%;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: center;
  align-items: flex-start;
  padding-bottom: 9px;
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
}

.columns-17 {
  grid-column-gap: 29px;
  grid-row-gap: 29px;
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.column-35 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #000;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
}

.image-wrapper-28 {
  flex: 0 auto;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-111 {
  color: #212121;
  font-size: 40px;
  font-weight: 600;
  line-height: 180%;
}

.text-112 {
  color: #333;
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  line-height: 100%;
}

.text-113 {
  color: #333;
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 100%;
}

.text-114 {
  color: #212121;
  text-align: center;
  font-size: 16px;
  font-weight: 500;
  line-height: 140%;
}

.button-38 {
  width: 100%;
  background-color: #fff;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.text-115 {
  color: #000;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.column-36 {
  grid-column-gap: 24px;
  grid-row-gap: 24px;
  border: 1px solid #fff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-top: 32px;
  padding-bottom: 32px;
  display: flex;
  box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
}

.text-116 {
  color: #fff;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.text-117 {
  color: #000;
  text-align: center;
  letter-spacing: 2px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.button-39 {
  width: 100%;
  height: 52px;
  background-color: #212121;
  border: 1px solid #212121;
  justify-content: center;
  align-items: center;
  padding: 16px 24px;
  text-decoration: none;
  display: flex;
}

.team-circles-5 {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 24px 64px;
  display: flex;
}

.container-19 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 160px;
  grid-row-gap: 160px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-118 {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.columns-18 {
  width: 100%;
  grid-column-gap: 48px;
  grid-row-gap: 48px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.card-11 {
  width: 100%;
  height: 350px;
  max-width: 368px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 100px;
  padding-bottom: 100px;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.image-wrapper-29 {
  width: 120px;
  height: 120px;
  justify-content: center;
  align-items: center;
  display: flex;
}

.content-28 {
  width: 100%;
  height: 370px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.info-4 {
  width: 100%;
  max-width: 300px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.text-119 {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  line-height: 150%;
  text-decoration: underline;
}

.text-120 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  line-height: 150%;
}

.card-12 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 100px;
  padding-bottom: 100px;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.card-13 {
  width: 100%;
  height: 350px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  opacity: .99;
  border: 0 solid #000;
  border-width: 0 1px;
  border-radius: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 100px;
  padding-bottom: 100px;
  display: flex;
  box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
}

.container-20 {
  width: 100%;
  max-width: 1200px;
  grid-column-gap: 80px;
  grid-row-gap: 80px;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.image-wrapper-30 {
  width: 100%;
  height: 500px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.text-121 {
  color: #000;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.button-40 {
  width: 124px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  background-color: #000;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  text-decoration: none;
  display: flex;
}

.button-41 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
  text-decoration: none;
}

.lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-11 {
  color: #212121;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.desktop---3 {
  width: 100%;
  height: 800px;
  max-width: 1460px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 64px;
  padding-bottom: 64px;
  display: flex;
}

.contact-form {
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  background-color: #fff;
  border: 1px solid #000;
  border-radius: 80px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 60px;
  display: flex;
}

.container-21 {
  grid-column-gap: 40px;
  grid-row-gap: 40px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.section-title {
  width: 100%;
  max-width: 530px;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

.get-in-touch {
  color: #000;
  text-align: center;
  font-size: 32px;
  font-weight: 700;
  line-height: 120%;
}

.text-122 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.form-wrapper {
  width: 100%;
  max-width: 500px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.form {
  width: 100%;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.input-wrapper {
  width: 100%;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  display: flex;
}

.form-block-label {
  color: #000;
  font-size: 14px;
  font-weight: 400;
  line-height: 150%;
}

.form-text-input {
  width: 100%;
  height: 42px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #979797;
  background-color: #fff;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: center;
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.form-text-input::-ms-input-placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input::placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.text-123 {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input-2 {
  width: 100%;
  height: 42px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #979797;
  background-color: #fff;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.form-text-input-2::-ms-input-placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input-2::placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-textarea {
  width: 100%;
  height: 100px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #979797;
  background-color: #fff;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.form-textarea::-ms-input-placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-textarea::placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-button {
  width: 100%;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #fff;
  background-color: #000;
  justify-content: center;
  align-items: center;
  padding: 12px 24px;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.text-124 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.desktop---12 {
  width: 100%;
  height: 800px;
  max-width: 1460px;
  grid-column-gap: 10px;
  grid-row-gap: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 64px;
  padding-bottom: 64px;
  display: flex;
}

.contact-form-2 {
  width: 100%;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  border-radius: 80px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 60px;
  display: flex;
}

@keyframes slideDown {
  0% {
      transform: translateY(-100%);
      opacity: 0;
  }
  100% {
      transform: translateY(0);
      opacity: 1;
  }
}

@keyframes slideUp {
  0% {
      transform: translateY(0);
      opacity: 1;
  }
  100% {
      transform: translateY(-100%);
      opacity: 0;
  }
}

.container-22 {
  width: 95%;
  height: 95%;
  grid-column-gap: 40px;
  grid-row-gap: 40px;
  object-fit: contain;
  background-color: #fff;
  border: 1px solid #000;
  border-radius: 80px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 0;
  margin-bottom: 0;
  padding: 10%;
  display: none;
  animation-fill-mode: forwards;
}

.text-125 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.text-126 {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input-3 {
  width: 100%;
  height: 42px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #979797;
  background-color: #fff;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.form-text-input-3::-ms-input-placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input-3::placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.text-127 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.overlay {
  position: fixed; /* Position the overlay fixed within the viewport */
  top: 0; /* Position at the top */
  left: 0; /* Position on the left side */
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  background-color: rgba(0,0,0,0.5); /* Black background with opacity */
  display: none; /* Initially hidden */
}


.contact-form-3 {
  width: 100%;
  height: 672px;
  grid-column-gap: 64px;
  grid-row-gap: 64px;
  border-radius: 80px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0;
  display: flex;
}

.text-128 {
  color: #000;
  text-align: center;
  font-size: 18px;
  font-weight: 400;
  line-height: 150%;
}

.form-text-input-4 {
  width: 100%;
  height: 42px;
  grid-column-gap: 8px;
  grid-row-gap: 8px;
  color: #979797;
  background-color: #fff;
  border: 1px solid #000;
  justify-content: flex-start;
  align-items: center;
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
  display: flex;
}

.form-text-input-4::-ms-input-placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.form-text-input-4::placeholder {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.text-129 {
  color: #979797;
  font-size: 14px;
  font-weight: 500;
  line-height: 140%;
}

.text-130 {
  color: #fff;
  font-size: 12px;
  font-weight: 500;
  line-height: 140%;
}

.enviado {
  position: absolute;
  left: 25%;
  right: 25%;
  text-align: center;
  background-color: #ddd;
  padding: 20px;
  display: none;
  animation-fill-mode: forwards;
}

@media screen and (max-width: 991px) {
  .navbar-logo-left {
    padding-right: 0;
  }

  .navbar-menu {
    max-width: unset;
  }

  .navbar-link, .navbar-button {
    justify-content: center;
  }

  .navbar-logo-left-2 {
    padding-right: 0;
  }

  .navbar-menu-2 {
    max-width: unset;
  }

  .navbar-link-2, .navbar-link-3, .navbar-link-4, .navbar-button-2 {
    justify-content: center;
  }

  .container, .columns {
    flex-direction: column;
    align-items: center;
  }

  .navbar-menu-3 {
    max-width: unset;
  }

  .navbar-link-5, .navbar-link-6, .navbar-button-3 {
    justify-content: center;
  }

  .container-2, .columns-2 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-menu-4 {
    max-width: unset;
  }

  .columns-3, .columns-4 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-3 {
    padding-right: 0;
  }

  .navbar-menu-5 {
    max-width: unset;
  }

  .navbar-link-7, .navbar-link-8, .navbar-link-9, .navbar-button-4 {
    justify-content: center;
  }

  .columns-5 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-4 {
    padding-right: 0;
  }

  .navbar-menu-6 {
    max-width: unset;
  }

  .navbar-link-10, .navbar-link-11, .navbar-link-12, .navbar-button-5 {
    justify-content: center;
  }

  .columns-6 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-5 {
    padding-right: 0;
  }

  .navbar-link-13, .navbar-link-14, .navbar-link-15, .navbar-button-6 {
    justify-content: center;
  }

  .columns-7 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-link-16, .navbar-link-17, .navbar-link-18, .navbar-button-7 {
    justify-content: center;
  }

  .columns-8 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-link-19, .navbar-link-20, .navbar-button-8 {
    justify-content: center;
  }

  .container-7, .columns-9, .columns-10 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-6 {
    padding-right: 0;
  }

  .navbar-menu-7 {
    max-width: unset;
  }

  .navbar-link-21, .navbar-link-22, .navbar-button-9 {
    justify-content: center;
  }

  .container-9, .columns-11, .columns-12, .container-11 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-7 {
    padding-right: 0;
  }

  .navbar-menu-8 {
    max-width: unset;
  }

  .navbar-link-23, .navbar-link-24 {
    justify-content: center;
  }

  .container-12, .columns-13, .columns-14, .container-14 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-logo-left-8 {
    padding-right: 0;
  }

  .navbar-menu-9 {
    max-width: unset;
  }

  .navbar-link-25, .navbar-link-26 {
    justify-content: center;
  }

  .container-15, .columns-15, .columns-16, .container-17 {
    flex-direction: column;
    align-items: center;
  }

  .navbar-menu-10 {
    max-width: unset;
  }

  .navbar-link-27, .navbar-link-28 {
    justify-content: center;
  }

  .container-18, .columns-17, .columns-18, .container-20 {
    flex-direction: column;
    align-items: center;
  }
}

 .close{
    position: absolute;
    right: 2.5%;    
    cursor: pointer;
  }
  html {
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    font-family: sans-serif;
  }
  
  body {
    margin: 0;
  }
  
  article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section, summary {
    display: block;
  }
  
  audio, canvas, progress, video {
    vertical-align: baseline;
    display: inline-block;
  }
  
  audio:not([controls]) {
    height: 0;
    display: none;
  }
  
  [hidden], template {
    display: none;
  }
  
  a {
    background-color: rgba(0, 0, 0, 0);
  }
  
  a:active, a:hover {
    outline: 0;
  }
  
  abbr[title] {
    border-bottom: 1px dotted;
  }
  
  b, strong {
    font-weight: bold;
  }
  
  dfn {
    font-style: italic;
  }
  
  h1 {
    margin: .67em 0;
    font-size: 2em;
  }
  
  mark {
    color: #000;
    background: #ff0;
  }
  
  small {
    font-size: 80%;
  }
  
  sub, sup {
    vertical-align: baseline;
    font-size: 75%;
    line-height: 0;
    position: relative;
  }
  
  sup {
    top: -.5em;
  }
  
  sub {
    bottom: -.25em;
  }
  
  img {
    border: 0;
  }
  
  svg:not(:root) {
    overflow: hidden;
  }
  
  figure {
    margin: 1em 40px;
  }
  
  hr {
    box-sizing: content-box;
    height: 0;
  }
  
  pre {
    overflow: auto;
  }
  
  code, kbd, pre, samp {
    font-family: monospace;
    font-size: 1em;
  }
  
  button, input, optgroup, select, textarea {
    color: inherit;
    font: inherit;
    margin: 0;
  }
  
  button {
    overflow: visible;
  }
  
  button, select {
    text-transform: none;
  }
  
  button, html input[type="button"], input[type="reset"] {
    -webkit-appearance: button;
    cursor: pointer;
  }
  
  button[disabled], html input[disabled] {
    cursor: default;
  }
  
  button::-moz-focus-inner, input::-moz-focus-inner {
    border: 0;
    padding: 0;
  }
  
  input {
    line-height: normal;
  }
  
  input[type="checkbox"], input[type="radio"] {
    box-sizing: border-box;
    padding: 0;
  }
  
  input[type="number"]::-webkit-inner-spin-button, input[type="number"]::-webkit-outer-spin-button {
    height: auto;
  }
  
  input[type="search"] {
    -webkit-appearance: none;
  }
  
  input[type="search"]::-webkit-search-cancel-button, input[type="search"]::-webkit-search-decoration {
    -webkit-appearance: none;
  }
  
  fieldset {
    border: 1px solid silver;
    margin: 0 2px;
    padding: .35em .625em .75em;
  }
  
  legend {
    border: 0;
    padding: 0;
  }
  
  textarea {
    overflow: auto;
  }
  
  optgroup {
    font-weight: bold;
  }
  
  table {
    border-collapse: collapse;
    border-spacing: 0;
  }
  
  td, th {
    padding: 0;
  }
  
  @font-face {
    font-family: webflow-icons;
    src: url("data:application/x-font-ttf;charset=utf-8;base64,AAEAAAALAIAAAwAwT1MvMg8SBiUAAAC8AAAAYGNtYXDpP+a4AAABHAAAAFxnYXNwAAAAEAAAAXgAAAAIZ2x5ZmhS2XEAAAGAAAADHGhlYWQTFw3HAAAEnAAAADZoaGVhCXYFgQAABNQAAAAkaG10eCe4A1oAAAT4AAAAMGxvY2EDtALGAAAFKAAAABptYXhwABAAPgAABUQAAAAgbmFtZSoCsMsAAAVkAAABznBvc3QAAwAAAAAHNAAAACAAAwP4AZAABQAAApkCzAAAAI8CmQLMAAAB6wAzAQkAAAAAAAAAAAAAAAAAAAABEAAAAAAAAAAAAAAAAAAAAABAAADpAwPA/8AAQAPAAEAAAAABAAAAAAAAAAAAAAAgAAAAAAADAAAAAwAAABwAAQADAAAAHAADAAEAAAAcAAQAQAAAAAwACAACAAQAAQAg5gPpA//9//8AAAAAACDmAOkA//3//wAB/+MaBBcIAAMAAQAAAAAAAAAAAAAAAAABAAH//wAPAAEAAAAAAAAAAAACAAA3OQEAAAAAAQAAAAAAAAAAAAIAADc5AQAAAAABAAAAAAAAAAAAAgAANzkBAAAAAAEBIAAAAyADgAAFAAAJAQcJARcDIP5AQAGA/oBAAcABwED+gP6AQAABAOAAAALgA4AABQAAEwEXCQEH4AHAQP6AAYBAAcABwED+gP6AQAAAAwDAAOADQALAAA8AHwAvAAABISIGHQEUFjMhMjY9ATQmByEiBh0BFBYzITI2PQE0JgchIgYdARQWMyEyNj0BNCYDIP3ADRMTDQJADRMTDf3ADRMTDQJADRMTDf3ADRMTDQJADRMTAsATDSANExMNIA0TwBMNIA0TEw0gDRPAEw0gDRMTDSANEwAAAAABAJ0AtAOBApUABQAACQIHCQEDJP7r/upcAXEBcgKU/usBFVz+fAGEAAAAAAL//f+9BAMDwwAEAAkAABcBJwEXAwE3AQdpA5ps/GZsbAOabPxmbEMDmmz8ZmwDmvxmbAOabAAAAgAA/8AEAAPAAB0AOwAABSInLgEnJjU0Nz4BNzYzMTIXHgEXFhUUBw4BBwYjNTI3PgE3NjU0Jy4BJyYjMSIHDgEHBhUUFx4BFxYzAgBqXV6LKCgoKIteXWpqXV6LKCgoKIteXWpVSktvICEhIG9LSlVVSktvICEhIG9LSlVAKCiLXl1qal1eiygoKCiLXl1qal1eiygoZiEgb0tKVVVKS28gISEgb0tKVVVKS28gIQABAAABwAIAA8AAEgAAEzQ3PgE3NjMxFSIHDgEHBhUxIwAoKIteXWpVSktvICFmAcBqXV6LKChmISBvS0pVAAAAAgAA/8AFtgPAADIAOgAAARYXHgEXFhUUBw4BBwYHIxUhIicuAScmNTQ3PgE3NjMxOAExNDc+ATc2MzIXHgEXFhcVATMJATMVMzUEjD83NlAXFxYXTjU1PQL8kz01Nk8XFxcXTzY1PSIjd1BQWlJJSXInJw3+mdv+2/7c25MCUQYcHFg5OUA/ODlXHBwIAhcXTzY1PTw1Nk8XF1tQUHcjIhwcYUNDTgL+3QFt/pOTkwABAAAAAQAAmM7nP18PPPUACwQAAAAAANciZKUAAAAA1yJkpf/9/70FtgPDAAAACAACAAAAAAAAAAEAAAPA/8AAAAW3//3//QW2AAEAAAAAAAAAAAAAAAAAAAAMBAAAAAAAAAAAAAAAAgAAAAQAASAEAADgBAAAwAQAAJ0EAP/9BAAAAAQAAAAFtwAAAAAAAAAKABQAHgAyAEYAjACiAL4BFgE2AY4AAAABAAAADAA8AAMAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAADgCuAAEAAAAAAAEADQAAAAEAAAAAAAIABwCWAAEAAAAAAAMADQBIAAEAAAAAAAQADQCrAAEAAAAAAAUACwAnAAEAAAAAAAYADQBvAAEAAAAAAAoAGgDSAAMAAQQJAAEAGgANAAMAAQQJAAIADgCdAAMAAQQJAAMAGgBVAAMAAQQJAAQAGgC4AAMAAQQJAAUAFgAyAAMAAQQJAAYAGgB8AAMAAQQJAAoANADsd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzVmVyc2lvbiAxLjAAVgBlAHIAcwBpAG8AbgAgADEALgAwd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzUmVndWxhcgBSAGUAZwB1AGwAYQByd2ViZmxvdy1pY29ucwB3AGUAYgBmAGwAbwB3AC0AaQBjAG8AbgBzRm9udCBnZW5lcmF0ZWQgYnkgSWNvTW9vbi4ARgBvAG4AdAAgAGcAZQBuAGUAcgBhAHQAZQBkACAAYgB5ACAASQBjAG8ATQBvAG8AbgAuAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==") format("truetype");
    font-weight: normal;
    font-style: normal;
  }
  
  [class^="w-icon-"], [class*=" w-icon-"] {
    speak: none;
    font-variant: normal;
    text-transform: none;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-style: normal;
    font-weight: normal;
    line-height: 1;
    font-family: webflow-icons !important;
  }
  
  .w-icon-slider-right:before {
    content: "î˜€";
  }
  
  .w-icon-slider-left:before {
    content: "î˜";
  }
 
  
  .w-icon-arrow-down:before, .w-icon-dropdown-toggle:before {
    content: "î˜ƒ";
  }
  
  .w-icon-file-upload-remove:before {
    content: "î¤€";
  }
  
  .w-icon-file-upload-icon:before {
    content: "î¤ƒ";
  }
  
  * {
    box-sizing: border-box;
  }
  
  html {
    height: 100%;
  }
  
  body {
    min-height: 100%;
    color: #333;
    background-color: #fff;
    margin: 0;
    font-family: Arial, sans-serif;
    font-size: 14px;
    line-height: 20px;
  }
  
  img {
    max-width: 100%;
    vertical-align: middle;
    display: inline-block;
  }
  
  html.w-mod-touch * {
    background-attachment: scroll !important;
  }
  
  .w-block {
    display: block;
  }
  
  .w-inline-block {
    max-width: 100%;
    display: inline-block;
  }
  
  .w-clearfix:before, .w-clearfix:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-clearfix:after {
    clear: both;
  }
  
  .w-hidden {
    display: none;
  }
  
  .w-button {
    color: #fff;
    line-height: inherit;
    cursor: pointer;
    background-color: #3898ec;
    border: 0;
    border-radius: 0;
    padding: 9px 15px;
    text-decoration: none;
    display: inline-block;
  }
  
  input.w-button {
    -webkit-appearance: button;
  }
  
  html[data-w-dynpage] [data-w-cloak] {
    color: rgba(0, 0, 0, 0) !important;
  }
  
  .w-webflow-badge, .w-webflow-badge * {
    z-index: auto;
    visibility: visible;
    box-sizing: border-box;
    width: auto;
    height: auto;
    max-height: none;
    max-width: none;
    min-height: 0;
    min-width: 0;
    float: none;
    clear: none;
    box-shadow: none;
    opacity: 1;
    direction: ltr;
    font-family: inherit;
    font-weight: inherit;
    color: inherit;
    font-size: inherit;
    line-height: inherit;
    font-style: inherit;
    font-variant: inherit;
    text-align: inherit;
    letter-spacing: inherit;
    -webkit-text-decoration: inherit;
    text-decoration: inherit;
    text-indent: 0;
    text-transform: inherit;
    text-shadow: none;
    font-smoothing: auto;
    vertical-align: baseline;
    cursor: inherit;
    white-space: inherit;
    word-break: normal;
    word-spacing: normal;
    word-wrap: normal;
    background: none;
    border: 0 rgba(0, 0, 0, 0);
    border-radius: 0;
    margin: 0;
    padding: 0;
    list-style-type: disc;
    transition: none;
    display: block;
    position: static;
    top: auto;
    bottom: auto;
    left: auto;
    right: auto;
    overflow: visible;
    transform: none;
  }
  
  .w-webflow-badge {
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, .1), 0 1px 3px rgba(0, 0, 0, .1);
    visibility: visible !important;
    z-index: 2147483647 !important;
    color: #aaadb0 !important;
    opacity: 1 !important;
    width: auto !important;
    height: auto !important;
    background-color: #fff !important;
    border-radius: 3px !important;
    margin: 0 !important;
    padding: 6px 8px 6px 6px !important;
    font-size: 12px !important;
    line-height: 14px !important;
    text-decoration: none !important;
    display: inline-block !important;
    position: fixed !important;
    top: auto !important;
    bottom: 12px !important;
    left: auto !important;
    right: 12px !important;
    overflow: visible !important;
    transform: none !important;
  }
  
  .w-webflow-badge > img {
    visibility: visible !important;
    opacity: 1 !important;
    vertical-align: middle !important;
    display: inline-block !important;
  }
  
  h1, h2, h3, h4, h5, h6 {
    margin-bottom: 10px;
    font-weight: bold;
  }
  
  h1 {
    margin-top: 20px;
    font-size: 38px;
    line-height: 44px;
  }
  
  h2 {
    margin-top: 20px;
    font-size: 32px;
    line-height: 36px;
  }
  
  h3 {
    margin-top: 20px;
    font-size: 24px;
    line-height: 30px;
  }
  
  h4 {
    margin-top: 10px;
    font-size: 18px;
    line-height: 24px;
  }
  
  h5 {
    margin-top: 10px;
    font-size: 14px;
    line-height: 20px;
  }
  
  h6 {
    margin-top: 10px;
    font-size: 12px;
    line-height: 18px;
  }
  
  p {
    margin-top: 0;
    margin-bottom: 10px;
  }
  
  blockquote {
    border-left: 5px solid #e2e2e2;
    margin: 0 0 10px;
    padding: 10px 20px;
    font-size: 18px;
    line-height: 22px;
  }
  
  figure {
    margin: 0 0 10px;
  }
  
  figcaption {
    text-align: center;
    margin-top: 5px;
  }
  
  ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 40px;
  }
  
  .w-list-unstyled {
    padding-left: 0;
    list-style: none;
  }
  
  .w-embed:before, .w-embed:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-embed:after {
    clear: both;
  }
  
  .w-video {
    width: 100%;
    padding: 0;
    position: relative;
  }
  
  .w-video iframe, .w-video object, .w-video embed {
    width: 100%;
    height: 100%;
    border: none;
    position: absolute;
    top: 0;
    left: 0;
  }
  
  fieldset {
    border: 0;
    margin: 0;
    padding: 0;
  }
  
  button, [type="button"], [type="reset"] {
    cursor: pointer;
    -webkit-appearance: button;
    border: 0;
  }
  
  .w-form {
    margin: 0 0 15px;
  }
  
  .w-form-done {
    text-align: center;
    background-color: #ddd;
    padding: 20px;
    display: none;
  }
  
  .w-form-fail {
    background-color: #ffdede;
    margin-top: 10px;
    padding: 10px;
    display: none;
  }
  
  label {
    margin-bottom: 5px;
    font-weight: bold;
    display: block;
  }
  
  .w-input, .w-select {
    width: 100%;
    height: 38px;
    color: #333;
    vertical-align: middle;
    background-color: #fff;
    border: 1px solid #ccc;
    margin-bottom: 10px;
    padding: 8px 12px;
    font-size: 14px;
    line-height: 1.42857;
    display: block;
  }
  
  .w-input:-moz-placeholder, .w-select:-moz-placeholder {
    color: #999;
  }
  
  .w-input::-moz-placeholder, .w-select::-moz-placeholder {
    color: #999;
    opacity: 1;
  }
  
  .w-input::-webkit-input-placeholder, .w-select::-webkit-input-placeholder {
    color: #999;
  }
  
  .w-input:focus, .w-select:focus {
    border-color: #3898ec;
    outline: 0;
  }
  
  .w-input[disabled], .w-select[disabled], .w-input[readonly], .w-select[readonly], fieldset[disabled] .w-input, fieldset[disabled] .w-select {
    cursor: not-allowed;
  }
  
  .w-input[disabled]:not(.w-input-disabled), .w-select[disabled]:not(.w-input-disabled), .w-input[readonly], .w-select[readonly], fieldset[disabled]:not(.w-input-disabled) .w-input, fieldset[disabled]:not(.w-input-disabled) .w-select {
    background-color: #eee;
  }
  
  textarea.w-input, textarea.w-select {
    height: auto;
  }
  
  .w-select {
    background-color: #f3f3f3;
  }
  
  .w-select[multiple] {
    height: auto;
  }
  
  .w-form-label {
    cursor: pointer;
    margin-bottom: 0;
    font-weight: normal;
    display: inline-block;
  }
  
  .w-radio {
    margin-bottom: 5px;
    padding-left: 20px;
    display: block;
  }
  
  .w-radio:before, .w-radio:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-radio:after {
    clear: both;
  }
  
  .w-radio-input {
    float: left;
    margin: 3px 0 0 -20px;
    line-height: normal;
  }
  
  .w-file-upload {
    margin-bottom: 10px;
    display: block;
  }
  
  .w-file-upload-input {
    width: .1px;
    height: .1px;
    opacity: 0;
    z-index: -100;
    position: absolute;
    overflow: hidden;
  }
  
  .w-file-upload-default, .w-file-upload-uploading, .w-file-upload-success {
    color: #333;
    display: inline-block;
  }
  
  .w-file-upload-error {
    margin-top: 10px;
    display: block;
  }
  
  .w-file-upload-default.w-hidden, .w-file-upload-uploading.w-hidden, .w-file-upload-error.w-hidden, .w-file-upload-success.w-hidden {
    display: none;
  }
  
  .w-file-upload-uploading-btn {
    cursor: pointer;
    background-color: #fafafa;
    border: 1px solid #ccc;
    margin: 0;
    padding: 8px 12px;
    font-size: 14px;
    font-weight: normal;
    display: flex;
  }
  
  .w-file-upload-file {
    background-color: #fafafa;
    border: 1px solid #ccc;
    flex-grow: 1;
    justify-content: space-between;
    margin: 0;
    padding: 8px 9px 8px 11px;
    display: flex;
  }
  
  .w-file-upload-file-name {
    font-size: 14px;
    font-weight: normal;
    display: block;
  }
  
  .w-file-remove-link {
    width: auto;
    height: auto;
    cursor: pointer;
    margin-top: 3px;
    margin-left: 10px;
    padding: 3px;
    display: block;
  }
  
  .w-icon-file-upload-remove {
    margin: auto;
    font-size: 10px;
  }
  
  .w-file-upload-error-msg {
    color: #ea384c;
    padding: 2px 0;
    display: inline-block;
  }
  
  .w-file-upload-info {
    padding: 0 12px;
    line-height: 38px;
    display: inline-block;
  }
  
  .w-file-upload-label {
    cursor: pointer;
    background-color: #fafafa;
    border: 1px solid #ccc;
    margin: 0;
    padding: 8px 12px;
    font-size: 14px;
    font-weight: normal;
    display: inline-block;
  }
  
  .w-icon-file-upload-icon, .w-icon-file-upload-uploading {
    width: 20px;
    margin-right: 8px;
    display: inline-block;
  }
  
  .w-icon-file-upload-uploading {
    height: 20px;
  }
  
  .w-container {
    max-width: 940px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .w-container:before, .w-container:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-container:after {
    clear: both;
  }
  
  .w-container .w-row {
    margin-left: -10px;
    margin-right: -10px;
  }
  
  .w-row:before, .w-row:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-row:after {
    clear: both;
  }
  
  .w-row .w-row {
    margin-left: 0;
    margin-right: 0;
  }
  
  .w-col {
    float: left;
    width: 100%;
    min-height: 1px;
    padding-left: 10px;
    padding-right: 10px;
    position: relative;
  }
  
  .w-col .w-col {
    padding-left: 0;
    padding-right: 0;
  }
  
  .w-col-1 {
    width: 8.33333%;
  }
  
  .w-col-2 {
    width: 16.6667%;
  }
  
  .w-col-3 {
    width: 25%;
  }
  
  .w-col-4 {
    width: 33.3333%;
  }
  
  .w-col-5 {
    width: 41.6667%;
  }
  
  .w-col-6 {
    width: 50%;
  }
  
  .w-col-7 {
    width: 58.3333%;
  }
  
  .w-col-8 {
    width: 66.6667%;
  }
  
  .w-col-9 {
    width: 75%;
  }
  
  .w-col-10 {
    width: 83.3333%;
  }
  
  .w-col-11 {
    width: 91.6667%;
  }
  
  .w-col-12 {
    width: 100%;
  }
  
  .w-hidden-main {
    display: none !important;
  }
  
  @media screen and (max-width: 991px) {
    .w-container {
      max-width: 728px;
    }
  
    .w-hidden-main {
      display: inherit !important;
    }
  
    .w-hidden-medium {
      display: none !important;
    }
  
    .w-col-medium-1 {
      width: 8.33333%;
    }
  
    .w-col-medium-2 {
      width: 16.6667%;
    }
  
    .w-col-medium-3 {
      width: 25%;
    }
  
    .w-col-medium-4 {
      width: 33.3333%;
    }
  
    .w-col-medium-5 {
      width: 41.6667%;
    }
  
    .w-col-medium-6 {
      width: 50%;
    }
  
    .w-col-medium-7 {
      width: 58.3333%;
    }
  
    .w-col-medium-8 {
      width: 66.6667%;
    }
  
    .w-col-medium-9 {
      width: 75%;
    }
  
    .w-col-medium-10 {
      width: 83.3333%;
    }
  
    .w-col-medium-11 {
      width: 91.6667%;
    }
  
    .w-col-medium-12 {
      width: 100%;
    }
  
    .w-col-stack {
      width: 100%;
      left: auto;
      right: auto;
    }
  }
  
  @media screen and (max-width: 767px) {
    .w-hidden-main, .w-hidden-medium {
      display: inherit !important;
    }
  
    .w-hidden-small {
      display: none !important;
    }
  
    .w-row, .w-container .w-row {
      margin-left: 0;
      margin-right: 0;
    }
  
    .w-col {
      width: 100%;
      left: auto;
      right: auto;
    }
  
    .w-col-small-1 {
      width: 8.33333%;
    }
  
    .w-col-small-2 {
      width: 16.6667%;
    }
  
    .w-col-small-3 {
      width: 25%;
    }
  
    .w-col-small-4 {
      width: 33.3333%;
    }
  
    .w-col-small-5 {
      width: 41.6667%;
    }
  
    .w-col-small-6 {
      width: 50%;
    }
  
    .w-col-small-7 {
      width: 58.3333%;
    }
  
    .w-col-small-8 {
      width: 66.6667%;
    }
  
    .w-col-small-9 {
      width: 75%;
    }
  
    .w-col-small-10 {
      width: 83.3333%;
    }
  
    .w-col-small-11 {
      width: 91.6667%;
    }
  
    .w-col-small-12 {
      width: 100%;
    }
  }
  
  @media screen and (max-width: 479px) {
    .w-container {
      max-width: none;
    }
  
    .w-hidden-main, .w-hidden-medium, .w-hidden-small {
      display: inherit !important;
    }
  
    .w-hidden-tiny {
      display: none !important;
    }
  
    .w-col {
      width: 100%;
    }
  
    .w-col-tiny-1 {
      width: 8.33333%;
    }
  
    .w-col-tiny-2 {
      width: 16.6667%;
    }
  
    .w-col-tiny-3 {
      width: 25%;
    }
  
    .w-col-tiny-4 {
      width: 33.3333%;
    }
  
    .w-col-tiny-5 {
      width: 41.6667%;
    }
  
    .w-col-tiny-6 {
      width: 50%;
    }
  
    .w-col-tiny-7 {
      width: 58.3333%;
    }
  
    .w-col-tiny-8 {
      width: 66.6667%;
    }
  
    .w-col-tiny-9 {
      width: 75%;
    }
  
    .w-col-tiny-10 {
      width: 83.3333%;
    }
  
    .w-col-tiny-11 {
      width: 91.6667%;
    }
  
    .w-col-tiny-12 {
      width: 100%;
    }
  }
  
  .w-widget {
    position: relative;
  }
  
  .w-widget-map {
    width: 100%;
    height: 400px;
  }
  
  .w-widget-map label {
    width: auto;
    display: inline;
  }
  
  .w-widget-map img {
    max-width: inherit;
  }
  
  .w-widget-map .gm-style-iw {
    text-align: center;
  }
  
  .w-widget-map .gm-style-iw > button {
    display: none !important;
  }
  
  .w-widget-twitter {
    overflow: hidden;
  }
  
  .w-widget-twitter-count-shim {
    vertical-align: top;
    width: 28px;
    height: 20px;
    text-align: center;
    background: #fff;
    border: 1px solid #758696;
    border-radius: 3px;
    display: inline-block;
    position: relative;
  }
  
  .w-widget-twitter-count-shim * {
    pointer-events: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  
  .w-widget-twitter-count-shim .w-widget-twitter-count-inner {
    text-align: center;
    color: #999;
    font-family: serif;
    font-size: 15px;
    line-height: 12px;
    position: relative;
  }
  
  .w-widget-twitter-count-shim .w-widget-twitter-count-clear {
    display: block;
    position: relative;
  }
  
  .w-widget-twitter-count-shim.w--large {
    width: 36px;
    height: 28px;
  }
  
  .w-widget-twitter-count-shim.w--large .w-widget-twitter-count-inner {
    font-size: 18px;
    line-height: 18px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical) {
    margin-left: 5px;
    margin-right: 8px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical).w--large {
    margin-left: 6px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical):before, .w-widget-twitter-count-shim:not(.w--vertical):after {
    content: " ";
    height: 0;
    width: 0;
    pointer-events: none;
    border: solid rgba(0, 0, 0, 0);
    position: absolute;
    top: 50%;
    left: 0;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical):before {
    border-width: 4px;
    border-color: rgba(117, 134, 150, 0) #5d6c7b rgba(117, 134, 150, 0) rgba(117, 134, 150, 0);
    margin-top: -4px;
    margin-left: -9px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical).w--large:before {
    border-width: 5px;
    margin-top: -5px;
    margin-left: -10px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical):after {
    border-width: 4px;
    border-color: rgba(255, 255, 255, 0) #fff rgba(255, 255, 255, 0) rgba(255, 255, 255, 0);
    margin-top: -4px;
    margin-left: -8px;
  }
  
  .w-widget-twitter-count-shim:not(.w--vertical).w--large:after {
    border-width: 5px;
    margin-top: -5px;
    margin-left: -9px;
  }
  
  .w-widget-twitter-count-shim.w--vertical {
    width: 61px;
    height: 33px;
    margin-bottom: 8px;
  }
  
  .w-widget-twitter-count-shim.w--vertical:before, .w-widget-twitter-count-shim.w--vertical:after {
    content: " ";
    height: 0;
    width: 0;
    pointer-events: none;
    border: solid rgba(0, 0, 0, 0);
    position: absolute;
    top: 100%;
    left: 50%;
  }
  
  .w-widget-twitter-count-shim.w--vertical:before {
    border-width: 5px;
    border-color: #5d6c7b rgba(117, 134, 150, 0) rgba(117, 134, 150, 0);
    margin-left: -5px;
  }
  
  .w-widget-twitter-count-shim.w--vertical:after {
    border-width: 4px;
    border-color: #fff rgba(255, 255, 255, 0) rgba(255, 255, 255, 0);
    margin-left: -4px;
  }
  
  .w-widget-twitter-count-shim.w--vertical .w-widget-twitter-count-inner {
    font-size: 18px;
    line-height: 22px;
  }
  
  .w-widget-twitter-count-shim.w--vertical.w--large {
    width: 76px;
  }
  
  .w-background-video {
    height: 500px;
    color: #fff;
    position: relative;
    overflow: hidden;
  }
  
  .w-background-video > video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -100;
    background-position: 50%;
    background-size: cover;
    margin: auto;
    position: absolute;
    top: -100%;
    bottom: -100%;
    left: -100%;
    right: -100%;
  }
  
  .w-background-video > video::-webkit-media-controls-start-playback-button {
    -webkit-appearance: none;
    display: none !important;
  }
  
  .w-background-video--control {
    background-color: rgba(0, 0, 0, 0);
    padding: 0;
    position: absolute;
    bottom: 1em;
    right: 1em;
  }
  
  .w-background-video--control > [hidden] {
    display: none !important;
  }
  
  .w-slider {
    height: 300px;
    text-align: center;
    clear: both;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    tap-highlight-color: rgba(0, 0, 0, 0);
    background: #ddd;
    position: relative;
  }
  
  .w-slider-mask {
    z-index: 1;
    height: 100%;
    white-space: nowrap;
    display: block;
    position: relative;
    left: 0;
    right: 0;
    overflow: hidden;
  }
  
  .w-slide {
    vertical-align: top;
    width: 100%;
    height: 100%;
    white-space: normal;
    text-align: left;
    display: inline-block;
    position: relative;
  }
  
  .w-slider-nav {
    z-index: 2;
    height: 40px;
    text-align: center;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    tap-highlight-color: rgba(0, 0, 0, 0);
    margin: auto;
    padding-top: 10px;
    position: absolute;
    top: auto;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .w-slider-nav.w-round > div {
    border-radius: 100%;
  }
  
  .w-slider-nav.w-num > div {
    width: auto;
    height: auto;
    font-size: inherit;
    line-height: inherit;
    padding: .2em .5em;
  }
  
  .w-slider-nav.w-shadow > div {
    box-shadow: 0 0 3px rgba(51, 51, 51, .4);
  }
  
  .w-slider-nav-invert {
    color: #fff;
  }
  
  .w-slider-nav-invert > div {
    background-color: rgba(34, 34, 34, .4);
  }
  
  .w-slider-nav-invert > div.w-active {
    background-color: #222;
  }
  
  .w-slider-dot {
    width: 1em;
    height: 1em;
    cursor: pointer;
    background-color: rgba(255, 255, 255, .4);
    margin: 0 3px .5em;
    transition: background-color .1s, color .1s;
    display: inline-block;
    position: relative;
  }
  
  .w-slider-dot.w-active {
    background-color: #fff;
  }
  
  .w-slider-dot:focus {
    outline: none;
    box-shadow: 0 0 0 2px #fff;
  }
  
  .w-slider-dot:focus.w-active {
    box-shadow: none;
  }
  
  .w-slider-arrow-left, .w-slider-arrow-right {
    width: 80px;
    cursor: pointer;
    color: #fff;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    margin: auto;
    font-size: 40px;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    overflow: hidden;
  }
  
  .w-slider-arrow-left [class^="w-icon-"], .w-slider-arrow-right [class^="w-icon-"], .w-slider-arrow-left [class*=" w-icon-"], .w-slider-arrow-right [class*=" w-icon-"] {
    position: absolute;
  }
  
  .w-slider-arrow-left:focus, .w-slider-arrow-right:focus {
    outline: 0;
  }
  
  .w-slider-arrow-left {
    z-index: 3;
    right: auto;
  }
  
  .w-slider-arrow-right {
    z-index: 4;
    left: auto;
  }
  
  .w-icon-slider-left, .w-icon-slider-right {
    width: 1em;
    height: 1em;
    margin: auto;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .w-slider-aria-label {
    clip: rect(0 0 0 0);
    height: 1px;
    width: 1px;
    border: 0;
    margin: -1px;
    padding: 0;
    position: absolute;
    overflow: hidden;
  }
  
  .w-slider-force-show {
    display: block !important;
  }
  
  .w-dropdown {
    text-align: left;
    z-index: 900;
    margin-left: auto;
    margin-right: auto;
    display: inline-block;
    position: relative;
  }
  
  .w-dropdown-btn, .w-dropdown-toggle, .w-dropdown-link {
    vertical-align: top;
    color: #222;
    text-align: left;
    white-space: nowrap;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
    text-decoration: none;
    position: relative;
  }
  
  .w-dropdown-toggle {
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: pointer;
    padding-right: 40px;
    display: inline-block;
  }
  
  .w-dropdown-toggle:focus {
    outline: 0;
  }
  
  .w-icon-dropdown-toggle {
    width: 1em;
    height: 1em;
    margin: auto 20px auto auto;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
  }
  
  .w-dropdown-list {
    min-width: 100%;
    background: #ddd;
    display: none;
    position: absolute;
  }
  
  .w-dropdown-list.w--open {
    display: block;
  }
  
  .w-dropdown-link {
    color: #222;
    padding: 10px 20px;
    display: block;
  }
  
  .w-dropdown-link.w--current {
    color: #0082f3;
  }
  
  .w-dropdown-link:focus {
    outline: 0;
  }
  
  @media screen and (max-width: 767px) {
    .w-nav-brand {
      padding-left: 10px;
    }
  }
  
  .w-lightbox-backdrop {
    cursor: auto;
    letter-spacing: normal;
    text-indent: 0;
    text-shadow: none;
    text-transform: none;
    visibility: visible;
    white-space: normal;
    word-break: normal;
    word-spacing: normal;
    word-wrap: normal;
    color: #fff;
    text-align: center;
    z-index: 2000;
    opacity: 0;
    -webkit-user-select: none;
    -moz-user-select: none;
    -webkit-tap-highlight-color: transparent;
    background: rgba(0, 0, 0, .9);
    outline: 0;
    font-family: Helvetica Neue, Helvetica, Ubuntu, Segoe UI, Verdana, sans-serif;
    font-size: 17px;
    font-style: normal;
    font-weight: 300;
    line-height: 1.2;
    list-style: disc;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    -webkit-transform: translate(0);
  }
  
  .w-lightbox-backdrop, .w-lightbox-container {
    height: 100%;
    -webkit-overflow-scrolling: touch;
    overflow: auto;
  }
  
  .w-lightbox-content {
    height: 100vh;
    position: relative;
    overflow: hidden;
  }
  
  .w-lightbox-view {
    width: 100vw;
    height: 100vh;
    opacity: 0;
    position: absolute;
  }
  
  .w-lightbox-view:before {
    content: "";
    height: 100vh;
  }
  
  .w-lightbox-group, .w-lightbox-group .w-lightbox-view, .w-lightbox-group .w-lightbox-view:before {
    height: 86vh;
  }
  
  .w-lightbox-frame, .w-lightbox-view:before {
    vertical-align: middle;
    display: inline-block;
  }
  
  .w-lightbox-figure {
    margin: 0;
    position: relative;
  }
  
  .w-lightbox-group .w-lightbox-figure {
    cursor: pointer;
  }
  
  .w-lightbox-img {
    width: auto;
    height: auto;
    max-width: none;
  }
  
  .w-lightbox-image {
    float: none;
    max-width: 100vw;
    max-height: 100vh;
    display: block;
  }
  
  .w-lightbox-group .w-lightbox-image {
    max-height: 86vh;
  }
  
  .w-lightbox-caption {
    text-align: left;
    text-overflow: ellipsis;
    white-space: nowrap;
    background: rgba(0, 0, 0, .4);
    padding: .5em 1em;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    overflow: hidden;
  }
  
  .w-lightbox-embed {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .w-lightbox-control {
    width: 4em;
    cursor: pointer;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 24px;
    transition: all .3s;
    position: absolute;
    top: 0;
  }
  
  .w-lightbox-left {
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0yMCAwIDI0IDQwIiB3aWR0aD0iMjQiIGhlaWdodD0iNDAiPjxnIHRyYW5zZm9ybT0icm90YXRlKDQ1KSI+PHBhdGggZD0ibTAgMGg1djIzaDIzdjVoLTI4eiIgb3BhY2l0eT0iLjQiLz48cGF0aCBkPSJtMSAxaDN2MjNoMjN2M2gtMjZ6IiBmaWxsPSIjZmZmIi8+PC9nPjwvc3ZnPg==");
    display: none;
    bottom: 0;
    left: 0;
  }
  
  .w-lightbox-right {
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii00IDAgMjQgNDAiIHdpZHRoPSIyNCIgaGVpZ2h0PSI0MCI+PGcgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48cGF0aCBkPSJtMC0waDI4djI4aC01di0yM2gtMjN6IiBvcGFjaXR5PSIuNCIvPjxwYXRoIGQ9Im0xIDFoMjZ2MjZoLTN2LTIzaC0yM3oiIGZpbGw9IiNmZmYiLz48L2c+PC9zdmc+");
    display: none;
    bottom: 0;
    right: 0;
  }
  
  .w-lightbox-close {
    height: 2.6em;
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii00IDAgMTggMTciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxNyI+PGcgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIj48cGF0aCBkPSJtMCAwaDd2LTdoNXY3aDd2NWgtN3Y3aC01di03aC03eiIgb3BhY2l0eT0iLjQiLz48cGF0aCBkPSJtMSAxaDd2LTdoM3Y3aDd2M2gtN3Y3aC0zdi03aC03eiIgZmlsbD0iI2ZmZiIvPjwvZz48L3N2Zz4=");
    background-size: 18px;
    right: 0;
  }
  
  .w-lightbox-strip {
    white-space: nowrap;
    padding: 0 1vh;
    line-height: 0;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    overflow-x: auto;
    overflow-y: hidden;
  }
  
  .w-lightbox-item {
    width: 10vh;
    box-sizing: content-box;
    cursor: pointer;
    padding: 2vh 1vh;
    display: inline-block;
    -webkit-transform: translate3d(0, 0, 0);
  }
  
  .w-lightbox-active {
    opacity: .3;
  }
  
  .w-lightbox-thumbnail {
    height: 10vh;
    background: #222;
    position: relative;
    overflow: hidden;
  }
  
  .w-lightbox-thumbnail-image {
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .w-lightbox-thumbnail .w-lightbox-tall {
    width: 100%;
    top: 50%;
    transform: translate(0, -50%);
  }
  
  .w-lightbox-thumbnail .w-lightbox-wide {
    height: 100%;
    left: 50%;
    transform: translate(-50%);
  }
  
  .w-lightbox-spinner {
    box-sizing: border-box;
    width: 40px;
    height: 40px;
    border: 5px solid rgba(0, 0, 0, .4);
    border-radius: 50%;
    margin-top: -20px;
    margin-left: -20px;
    animation: .8s linear infinite spin;
    position: absolute;
    top: 50%;
    left: 50%;
  }
  
  .w-lightbox-spinner:after {
    content: "";
    border: 3px solid rgba(0, 0, 0, 0);
    border-bottom-color: #fff;
    border-radius: 50%;
    position: absolute;
    top: -4px;
    bottom: -4px;
    left: -4px;
    right: -4px;
  }
  
  .w-lightbox-hide {
    display: none;
  }
  
  .w-lightbox-noscroll {
    overflow: hidden;
  }
  
  @media (min-width: 768px) {
    .w-lightbox-content {
      height: 96vh;
      margin-top: 2vh;
    }
  
    .w-lightbox-view, .w-lightbox-view:before {
      height: 96vh;
    }
  
    .w-lightbox-group, .w-lightbox-group .w-lightbox-view, .w-lightbox-group .w-lightbox-view:before {
      height: 84vh;
    }
  
    .w-lightbox-image {
      max-width: 96vw;
      max-height: 96vh;
    }
  
    .w-lightbox-group .w-lightbox-image {
      max-width: 82.3vw;
      max-height: 84vh;
    }
  
    .w-lightbox-left, .w-lightbox-right {
      opacity: .5;
      display: block;
    }
  
    .w-lightbox-close {
      opacity: .8;
    }
  
    .w-lightbox-control:hover {
      opacity: 1;
    }
  }
  
  .w-lightbox-inactive, .w-lightbox-inactive:hover {
    opacity: 0;
  }
  
  .w-richtext:before, .w-richtext:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-richtext:after {
    clear: both;
  }
  
  .w-richtext[contenteditable="true"]:before, .w-richtext[contenteditable="true"]:after {
    white-space: initial;
  }
  
  .w-richtext ol, .w-richtext ul {
    overflow: hidden;
  }
  
  .w-richtext .w-richtext-figure-selected.w-richtext-figure-type-video div:after, .w-richtext .w-richtext-figure-selected[data-rt-type="video"] div:after, .w-richtext .w-richtext-figure-selected.w-richtext-figure-type-image div, .w-richtext .w-richtext-figure-selected[data-rt-type="image"] div {
    outline: 2px solid #2895f7;
  }
  
  .w-richtext figure.w-richtext-figure-type-video > div:after, .w-richtext figure[data-rt-type="video"] > div:after {
    content: "";
    display: none;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .w-richtext figure {
    max-width: 60%;
    position: relative;
  }
  
  .w-richtext figure > div:before {
    cursor: default !important;
  }
  
  .w-richtext figure img {
    width: 100%;
  }
  
  .w-richtext figure figcaption.w-richtext-figcaption-placeholder {
    opacity: .6;
  }
  
  .w-richtext figure div {
    color: rgba(0, 0, 0, 0);
    font-size: 0;
  }
  
  .w-richtext figure.w-richtext-figure-type-image, .w-richtext figure[data-rt-type="image"] {
    display: table;
  }
  
  .w-richtext figure.w-richtext-figure-type-image > div, .w-richtext figure[data-rt-type="image"] > div {
    display: inline-block;
  }
  
  .w-richtext figure.w-richtext-figure-type-image > figcaption, .w-richtext figure[data-rt-type="image"] > figcaption {
    caption-side: bottom;
    display: table-caption;
  }
  
  .w-richtext figure.w-richtext-figure-type-video, .w-richtext figure[data-rt-type="video"] {
    width: 60%;
    height: 0;
  }
  
  .w-richtext figure.w-richtext-figure-type-video iframe, .w-richtext figure[data-rt-type="video"] iframe {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .w-richtext figure.w-richtext-figure-type-video > div, .w-richtext figure[data-rt-type="video"] > div {
    width: 100%;
  }
  
  .w-richtext figure.w-richtext-align-center {
    clear: both;
    margin-left: auto;
    margin-right: auto;
  }
  
  .w-richtext figure.w-richtext-align-center.w-richtext-figure-type-image > div, .w-richtext figure.w-richtext-align-center[data-rt-type="image"] > div {
    max-width: 100%;
  }
  
  .w-richtext figure.w-richtext-align-normal {
    clear: both;
  }
  
  .w-richtext figure.w-richtext-align-fullwidth {
    width: 100%;
    max-width: 100%;
    text-align: center;
    clear: both;
    margin-left: auto;
    margin-right: auto;
    display: block;
  }
  
  .w-richtext figure.w-richtext-align-fullwidth > div {
    padding-bottom: inherit;
    display: inline-block;
  }
  
  .w-richtext figure.w-richtext-align-fullwidth > figcaption {
    display: block;
  }
  
  .w-richtext figure.w-richtext-align-floatleft {
    float: left;
    clear: none;
    margin-right: 15px;
  }
  
  .w-richtext figure.w-richtext-align-floatright {
    float: right;
    clear: none;
    margin-left: 15px;
  }
  
  .w-nav {
    z-index: 1000;
    background: #ddd;
    position: relative;
  }
  
  .w-nav:before, .w-nav:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-nav:after {
    clear: both;
  }
  
  .w-nav-brand {
    float: left;
    color: #333;
    text-decoration: none;
    position: relative;
  }
  
  .w-nav-link {
    vertical-align: top;
    color: #222;
    text-align: left;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
    text-decoration: none;
    display: inline-block;
    position: relative;
  }
  
  .w-nav-link.w--current {
    color: #0082f3;
  }
  
  .w-nav-menu {
    float: right;
    position: relative;
  }
  
  [data-nav-menu-open] {
    text-align: center;
    min-width: 200px;
    background: #c8c8c8;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    overflow: visible;
    display: block !important;
  }
  
  .w--nav-link-open {
    display: block;
    position: relative;
  }
  
  .w-nav-overlay {
    width: 100%;
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    overflow: hidden;
  }
  
  .w-nav-overlay [data-nav-menu-open] {
    top: 0;
  }
  
  .w-nav[data-animation="over-left"] .w-nav-overlay {
    width: auto;
  }
  
  .w-nav[data-animation="over-left"] .w-nav-overlay, .w-nav[data-animation="over-left"] [data-nav-menu-open] {
    z-index: 1;
    top: 0;
    right: auto;
  }
  
  .w-nav[data-animation="over-right"] .w-nav-overlay {
    width: auto;
  }
  
  .w-nav[data-animation="over-right"] .w-nav-overlay, .w-nav[data-animation="over-right"] [data-nav-menu-open] {
    z-index: 1;
    top: 0;
    left: auto;
  }
  
  .w-nav-button {
    float: right;
    cursor: pointer;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    padding: 18px;
    font-size: 24px;
    display: none;
    position: relative;
  }
  
  .w-nav-button:focus {
    outline: 0;
  }
  
  .w-nav-button.w--open {
    color: #fff;
    background-color: #c8c8c8;
  }
  
  .w-nav[data-collapse="all"] .w-nav-menu {
    display: none;
  }
  
  .w-nav[data-collapse="all"] .w-nav-button, .w--nav-dropdown-open, .w--nav-dropdown-toggle-open {
    display: block;
  }
  
  .w--nav-dropdown-list-open {
    position: static;
  }
  
  @media screen and (max-width: 991px) {
    .w-nav[data-collapse="medium"] .w-nav-menu {
      display: none;
    }
  
    .w-nav[data-collapse="medium"] .w-nav-button {
      display: block;
    }
  }
  
  @media screen and (max-width: 767px) {
    .w-nav[data-collapse="small"] .w-nav-menu {
      display: none;
    }
  
    .w-nav[data-collapse="small"] .w-nav-button {
      display: block;
    }
  
    .w-nav-brand {
      padding-left: 10px;
    }
  }
  
  @media screen and (max-width: 479px) {
    .w-nav[data-collapse="tiny"] .w-nav-menu {
      display: none;
    }
  
    .w-nav[data-collapse="tiny"] .w-nav-button {
      display: block;
    }
  }
  
  .w-tabs {
    position: relative;
  }
  
  .w-tabs:before, .w-tabs:after {
    content: " ";
    grid-area: 1 / 1 / 2 / 2;
    display: table;
  }
  
  .w-tabs:after {
    clear: both;
  }
  
  .w-tab-menu {
    position: relative;
  }
  
  .w-tab-link {
    vertical-align: top;
    text-align: left;
    cursor: pointer;
    color: #222;
    background-color: #ddd;
    padding: 9px 30px;
    text-decoration: none;
    display: inline-block;
    position: relative;
  }
  
  .w-tab-link.w--current {
    background-color: #c8c8c8;
  }
  
  .w-tab-link:focus {
    outline: 0;
  }
  
  .w-tab-content {
    display: block;
    position: relative;
    overflow: hidden;
  }
  
  .w-tab-pane {
    display: none;
    position: relative;
  }
  
  .w--tab-active {
    display: block;
  }
  
  @media screen and (max-width: 479px) {
    .w-tab-link {
      display: block;
    }
  }
  
  .w-ix-emptyfix:after {
    content: "";
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0);
    }
  
    100% {
      transform: rotate(360deg);
    }
  }
  
  .w-dyn-empty {
    background-color: #ddd;
    padding: 10px;
  }
  
  .w-dyn-hide, .w-dyn-bind-empty, .w-condition-invisible {
    display: none !important;
  }
  
  .wf-layout-layout {
    display: grid;
  }
  
  .navbar-logo-left {
    width: 100%;
    max-width: 1440px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #fff;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .navbar-brand {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-2 {
    color: #000;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .navbar-menu {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-3 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .desktop---1 {
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    background-color: rgba(88, 78, 59, 0);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-2 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-2 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-2 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-2 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-2 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-2 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-4 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-2 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-2, .navbar-link-3, .navbar-link-4 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-2 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-5 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left {
    width: 100%;
    height: 512px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .title-copy-goes-here-be-awesome {
    color: #000;
    font-size: 56px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .error-b752fee3-6f00-1a55-ba86-9bb2c9503ac2 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions {
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .column-2 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-3 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-comparison {
    width: 100%;
    height: 458px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns {
    width: 100%;
    height: 452px;
    max-width: 1106px;
    grid-column-gap: 15px;
    grid-row-gap: 15px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-3 {
    width: 100%;
    height: 439px;
    max-width: 260px;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .intro {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 32px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .image-wrapper-2 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-1 {
    width: 183px;
    height: 115px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .name {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-6 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-7 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .pricing {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    justify-content: center;
    align-items: flex-end;
    display: flex;
  }
  
  .text-8 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .text-9 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-2 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-10 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-4 {
    width: 100%;
    height: 439px;
    max-width: 260px;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-3 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-11 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-12 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-4 {
    width: 100%;
    height: 52px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .hacer-pedido {
    color: #fff;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-1 {
    color: #212121;
    font-size: 18px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .image-4 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-13 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-14 {
    color: #000;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .navbar-menu-3 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-5 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .text-15 {
    color: #000;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .navbar-link-6 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-3 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-16 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-2 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-2 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-5 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-3 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .button-5 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .column-6 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-3 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-5 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-comparison-2 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-2 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-7 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-4 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-17 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-18 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-19 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-20 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-6 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-21 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-8 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-7 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-22 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-23 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-8 {
    width: 100%;
    height: 52px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-2 {
    color: #212121;
    font-size: 18px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .content-4 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-6 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-24 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-4 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-25 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .content-5 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .button-9 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .column-9 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-5 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-7 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-comparison-3 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-3 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-10 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-6 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-26 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-27 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-28 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .text-29 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-30 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-11 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-10 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-31 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-32 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-11 {
    width: 100%;
    height: 52px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-3 {
    color: #212121;
    font-size: 18px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-33 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-12 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-7 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-8 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-6 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .button-12 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-4 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-4 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-13 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-8 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-34 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-35 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-36 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .text-37 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-38 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-14 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-13 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-39 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-40 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-14 {
    width: 100%;
    height: 52px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-4 {
    color: #212121;
    font-size: 18px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .desktop---4 {
    width: 100%;
    height: 1022px;
    max-width: 1268px;
    grid-column-gap: 65px;
    grid-row-gap: 65px;
    background-color: rgba(88, 78, 59, 0);
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-3 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-3 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-3 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-7 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-3 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-9 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-41 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-5 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-7, .navbar-link-8, .navbar-link-9 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-4 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-42 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .team-circles {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-3 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 85px;
    grid-row-gap: 85px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .columns-5 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-9 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-10 {
    width: 180px;
    height: 180px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-8 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-43 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-44 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .description-2 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .title-section {
    width: 100%;
    max-width: 530px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-45 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .desktop---5 {
    width: 100%;
    height: 1022px;
    max-width: 1268px;
    grid-column-gap: 65px;
    grid-row-gap: 65px;
    background-color: rgba(88, 78, 59, 0);
    flex-flow: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-4 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-4 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-4 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-9 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-4 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-11 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-46 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-6 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-10, .navbar-link-11, .navbar-link-12 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-5 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-47 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .container-4 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 58px;
    grid-row-gap: 58px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .columns-6 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-10 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-12 {
    width: 100px;
    height: 100px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-10 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-48 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-49 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .description-3 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-50 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .desktop---6 {
    width: 100%;
    max-width: 1268px;
    grid-column-gap: 65px;
    grid-row-gap: 65px;
    background-color: rgba(88, 78, 59, 0);
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-5 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-5 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-5 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-11 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-5 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-13, .navbar-link-14, .navbar-link-15 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-6 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-51 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .container-5 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 58px;
    grid-row-gap: 58px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .columns-7 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-11 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-13 {
    width: 100px;
    height: 100px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-12 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-52 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-53 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .description-4 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-54 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .desktop---7 {
    width: 100%;
    max-width: 1268px;
    grid-column-gap: 65px;
    grid-row-gap: 65px;
    background-color: #584e3b;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .content-13 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-link-16, .navbar-link-17, .navbar-link-18 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-7 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-55 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .container-6 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 58px;
    grid-row-gap: 58px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .columns-8 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-12 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-14 {
    width: 100px;
    height: 100px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-14 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-56 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-57 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .description-5 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-58 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .desktop---8 {
    grid-column-gap: 37px;
    grid-row-gap: 37px;
    background-color: rgba(88, 78, 59, 0);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .content-15 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-link-19, .navbar-link-20 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-8 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-59 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-3 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-7 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-15 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-13 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-15 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-16 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-16 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .error-d543413a-d1a2-674f-377e-248198feb8ae {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-2 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-15 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-5 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-9 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-17 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .intro-2 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 32px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .image-wrapper-14 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-1-2 {
    width: 183px;
    height: 115px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .name-2 {
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-60 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-61 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .pricing-2 {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    justify-content: center;
    align-items: flex-end;
    display: flex;
  }
  
  .text-62 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description-6 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-63 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-16 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-64 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-18 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-17 {
    width: 100%;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-65 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-66 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-18 {
    width: 100%;
    height: 52px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .hacer-pedido-2 {
    color: #fff;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .container-8 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 58px;
    grid-row-gap: 58px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .columns-10 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-16 {
    width: 100px;
    height: 100px;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    object-fit: cover;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-67 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-68 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .description-7 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-69 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-0 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .desktop---9 {
    grid-column-gap: 37px;
    grid-row-gap: 37px;
    background-color: #584e3b;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-6 {
    width: 100%;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-6 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-6 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-17 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-6 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-17 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-70 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-7 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-21, .navbar-link-22 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-9 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-71 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-4 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-9 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-19 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-15 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-18 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-20 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-18 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .error-dcda2372-13e2-fe2c-8cb3-c1ef879690f8 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-3 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-19 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-6 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-11 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-21 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .intro-3 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 32px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .image-wrapper-16 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-1-3 {
    width: 183px;
    height: 115px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .name-3 {
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-72 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-73 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .pricing-3 {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    justify-content: center;
    align-items: flex-end;
    display: flex;
  }
  
  .text-74 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description-8 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-75 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-20 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-76 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-22 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-21 {
    width: 100%;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-77 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-78 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-22 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .hacer-pedido-3 {
    color: #fff;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .team-circles-2 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-10 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 53px;
    grid-row-gap: 53px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .title-section-2 {
    width: 100%;
    max-width: 530px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-79 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .error-dcda2372-13e2-fe2c-8cb3-c1ef87969114 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .columns-12 {
    width: 100%;
    height: 500px;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-2 {
    width: 100%;
    height: 500px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-17 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-1 {
    object-fit: cover;
    border-radius: 250px;
  }
  
  .content-19 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info-2 {
    width: 100%;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-80 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-81 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .card-3 {
    width: 100%;
    height: 500px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .card-4 {
    width: 100%;
    height: 500px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .hero-heading-right {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 64px 24px;
    display: flex;
  }
  
  .container-11 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-23 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-18 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-82 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .error-dcda2372-13e2-fe2c-8cb3-c1ef87969124 {
    color: #212121;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .actions-4 {
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-23 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-24 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-5 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .desktop---10 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    background-color: #584e3b;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-7 {
    width: 100%;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-7 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-7 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-20 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-7 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-19 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-83 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-8 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-23, .navbar-link-24 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .text-84 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-5 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-12 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-24 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-19 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-20 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-25 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-21 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-6 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-5 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-25 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-7 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-13 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-26 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .intro-4 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 32px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .image-wrapper-20 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-85 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-86 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-87 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description-9 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .text-88 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-26 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-89 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-27 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-27 {
    width: 100%;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-90 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-91 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-28 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .team-circles-3 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-13 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 160px;
    grid-row-gap: 160px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-92 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .columns-14 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-5 {
    width: 100%;
    height: 350px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-21 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-22 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-93 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-94 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .card-6 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .card-7 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .hero-heading-right-2 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    margin-top: -100px;
    padding-bottom: 64px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .container-14 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-28 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-22 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-95 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .button-29 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-30 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-7 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .desktop---11 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    background-color: #584e3b;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    display: flex;
  }
  
  .navbar-logo-left-8 {
    width: 100%;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-8 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-8 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-23 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-8 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-21 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-96 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-9 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-25, .navbar-link-26 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .text-97 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-6 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-15 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-23 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-22 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-29 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-24 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-8 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-6 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-31 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-8 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-15 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-30 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-24 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-98 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-99 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-100 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .text-101 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-32 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-102 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-31 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-33 {
    width: 100%;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-103 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-104 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-34 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .team-circles-4 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-16 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 160px;
    grid-row-gap: 160px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-105 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .columns-16 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-8 {
    width: 100%;
    height: 350px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-25 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-25 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info-3 {
    width: 100%;
    max-width: 300px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-106 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-107 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .card-9 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .card-10 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .container-17 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-32 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-26 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-108 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .button-35 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-36 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-9 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .navbarcontainer-9 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-9 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-26 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-9 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-23 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-109 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-10 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-27, .navbar-link-28 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .text-110 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-7 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-18 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-33 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-27 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-24 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-34 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-27 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-10 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-7 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-37 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-9 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-17 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-35 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-28 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-111 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-112 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .text-113 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .text-114 {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-38 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-115 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-36 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .text-116 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-117 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-39 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .team-circles-5 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-19 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 160px;
    grid-row-gap: 160px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-118 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .columns-18 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-11 {
    width: 100%;
    height: 350px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 100px;
    padding-bottom: 100px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-29 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-28 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info-4 {
    width: 100%;
    max-width: 300px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-119 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-120 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .card-12 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 100px;
    padding-bottom: 100px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .card-13 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 100px;
    padding-bottom: 100px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .container-20 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-wrapper-30 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-121 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .button-40 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-41 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-11 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .desktop---3 {
    width: 100%;
    height: 800px;
    max-width: 1460px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-top: 64px;
    padding-bottom: 64px;
    display: flex;
  }
  
  .contact-form {
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    background-color: #fff;
    border: 1px solid #000;
    border-radius: 80px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 60px;
    display: flex;
  }
  
  .container-21 {
    grid-column-gap: 40px;
    grid-row-gap: 40px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .section-title {
    width: 100%;
    max-width: 530px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .get-in-touch {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .text-122 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .form-wrapper {
    width: 100%;
    max-width: 500px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .form {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .input-wrapper {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .form-block-label {
    color: #000;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .form-text-input {
    width: 100%;
    height: 42px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #979797;
    background-color: #fff;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: center;
    padding: 12px;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .form-text-input::-ms-input-placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input::placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-123 {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input-2 {
    width: 100%;
    height: 42px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #979797;
    background-color: #fff;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 12px;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .form-text-input-2::-ms-input-placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input-2::placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-textarea {
    width: 100%;
    height: 100px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #979797;
    background-color: #fff;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 12px;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .form-textarea::-ms-input-placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-textarea::placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-button {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #fff;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .text-124 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .desktop---12 {
    width: 100%;
    height: 800px;
    max-width: 1460px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-top: 64px;
    padding-bottom: 64px;
    display: flex;
  }
  
  .contact-form-2 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    border-radius: 80px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 60px;
    display: flex;
  }
  
  .container-22 {
    width: 95%;
    height: 95%;
    grid-column-gap: 40px;
    grid-row-gap: 40px;
    object-fit: contain;
    background-color: #fff;
    border: 1px solid #000;
    border-radius: 80px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 0;
    margin-bottom: 0;
    padding: 10%;
    display: flex;
  }
  
  .text-125 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-126 {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input-3 {
    width: 100%;
    height: 42px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #979797;
    background-color: #fff;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 12px;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .form-text-input-3::-ms-input-placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input-3::placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-127 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .contact-form-3 {
    width: 100%;
    height: 672px;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    border-radius: 80px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0;
    display: flex;
  }
  
  .text-128 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .form-text-input-4 {
    width: 100%;
    height: 42px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    color: #979797;
    background-color: #fff;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: center;
    padding: 12px;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
    display: flex;
  }
  
  .form-text-input-4::-ms-input-placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .form-text-input-4::placeholder {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-129 {
    color: #979797;
    font-size: 14px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-130 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .success-message {
    position: absolute;
    left: 25%;
    right: 25%;
  }
  
  .desktop---13 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    background-color: rgba(255, 255, 255, 0);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 10px;
    padding-right: 10px;
    display: flex;
  }
  
  .navbar-logo-left-9 {
    width: 100%;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .navbarcontainer-10 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-10 {
    width: 100%;
    max-width: 1200px;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .content-29 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .author-10 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .image-25 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-131 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-11 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-29, .navbar-link-30 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-10 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-132 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-8 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding: 33px 24px 11px;
    display: flex;
  }
  
  .container-23 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-37 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-31 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-26 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-38 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-30 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-8 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-42 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-10 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-19 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-39 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .intro-5 {
    width: 100%;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 32px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .image-wrapper-32 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-1-4 {
    width: 183px;
    height: 115px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .name-4 {
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-133 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-134 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .pricing-4 {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    justify-content: center;
    align-items: flex-end;
    display: flex;
  }
  
  .text-135 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description-10 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .vence-en-1-d-a {
    color: #212121;
    text-align: center;
    font-size: 16px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-43 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-136 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-40 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-44 {
    width: 100%;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-137 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-138 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-45 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .hacer-pedido-4 {
    color: #fff;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .team-circles-6 {
    width: 100%;
    grid-column-gap: 64px;
    grid-row-gap: 64px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px 64px;
    display: flex;
  }
  
  .container-24 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 160px;
    grid-row-gap: 160px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .title-section-3 {
    width: 100%;
    max-width: 530px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-139 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .somos-pasi-n-por-la-madera-seleccionamos-cuidadosamente-cada-pieza-garantizando-que-cada-producto-que-ofrecemos-cumple-con-los-m-s-altos-est-ndares-de-calidad-nuestro-equipo-capacitado-brinda-un-excelente-servicio-cubriendo-las-necesidades-de-nuestros-clientes-con-una-variedad-de-productos-de-madera-duraderos-y-de-alta-calidad {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .columns-20 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-14 {
    width: 100%;
    height: 350px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 20px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-33 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-31 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info-5 {
    width: 100%;
    max-width: 300px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-140 {
    color: #000;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-141 {
    color: #000;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .card-15 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 20px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .card-16 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 20px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .hero-heading-right-3 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-bottom: 64px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .container-25 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-41 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-34 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-142 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .estamos-ubicados-en-av-fulanito-de-tal-777-colonia-quien-sabe-como-en-general-escobedo-nuevo-le-n {
    color: #212121;
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
  }
  
  .actions-9 {
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-46 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-47 {
    color: #fff;
    text-align: center;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .footer {
    width: 100%;
    background-color: #f5f7fa;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 10px 24px;
    display: flex;
  }
  
  .columns-21 {
    width: 100%;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .small-columns {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    padding-top: 16px;
    display: flex;
  }
  
  .column-42 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    display: flex;
  }
  
  .content-32 {
    width: 142px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    display: flex;
  }
  
  .footer-links {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    object-fit: contain;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-143 {
    color: #212121;
    font-size: 14px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .link {
    width: 150px;
    color: #212121;
    object-fit: contain;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .copyright {
    width: 100%;
    max-width: 940px;
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    justify-content: center;
    align-items: center;
    padding-top: 16px;
    padding-bottom: 16px;
    display: flex;
    box-shadow: 0 -1px #e4ebf3;
  }
  
  .text-144 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-12 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .desktop---14 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    background-color: rgba(255, 255, 255, 0);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 10px;
    padding-right: 10px;
    display: flex;
  }
  
  .navbar-logo-left-10 {
    width: 100%;
    justify-content: center;
    align-items: flex-start;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
    position: fixed;
    top: 0%;
    bottom: auto;
    left: 0%;
    right: 0%;
  }
  
  .navbarcontainer-11 {
    width: 100%;
    max-width: 1200px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .navbar-content-11 {
    width: 100%;
    max-width: 1200px;
    flex: 0 auto;
    justify-content: space-between;
    align-items: center;
    display: flex;
  }
  
  .image-27 {
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-145 {
    width: 100%;
    max-width: 308px;
    grid-column-gap: 4px;
    grid-row-gap: 4px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .navbar-menu-12 {
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .navbar-link-31 {
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-link-32 {
    background-color: #000;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 24px 12px;
    display: flex;
  }
  
  .navbar-button-11 {
    height: auto;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    object-fit: contain;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 8px 20px;
    display: flex;
  }
  
  .text-146 {
    color: #fff;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .hero-heading-left-9 {
    z-index: auto;
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    margin-top: 15%;
    padding: 33px 24px 11px;
    display: flex;
    position: static;
    top: 20%;
  }
  
  .container-26 {
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-43 {
    width: 100%;
    max-width: 560px;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-35 {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .image-28 {
    object-fit: cover;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-44 {
    width: 100%;
    max-width: 560px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .content-33 {
    width: 100%;
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-13 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .actions-10 {
    height: 67px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-48 {
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .pricing-comparison-11 {
    width: 100%;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: center;
    align-items: flex-start;
    padding-bottom: 9px;
    padding-left: 24px;
    padding-right: 24px;
    display: flex;
  }
  
  .columns-22 {
    grid-column-gap: 29px;
    grid-row-gap: 29px;
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .column-45 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #000;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .12);
  }
  
  .image-wrapper-36 {
    flex: 0 auto;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .pricing-1-5 {
    width: 183px;
    height: 115px;
    object-fit: cover;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .name-5 {
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-147 {
    color: #212121;
    font-size: 40px;
    font-weight: 600;
    line-height: 180%;
  }
  
  .text-148 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 100%;
  }
  
  .pricing-5 {
    width: 100%;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    justify-content: center;
    align-items: flex-end;
    display: flex;
  }
  
  .text-149 {
    color: #333;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    line-height: 100%;
  }
  
  .description-11 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    text-align: center;
    justify-content: space-around;
    align-items: flex-start;
    display: flex;
  }
  
  .button-49 {
    width: 100%;
    background-color: #fff;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-150 {
    color: #000;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .column-46 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    border: 1px solid #fff;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 32px;
    padding-bottom: 32px;
    display: flex;
    box-shadow: 0 4px 130px rgba(150, 163, 181, .3);
  }
  
  .button-50 {
    width: 100%;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .text-151 {
    color: #fff;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .text-152 {
    color: #000;
    text-align: center;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
  }
  
  .button-51 {
    width: 100%;
    height: 52px;
    background-color: #212121;
    border: 1px solid #212121;
    justify-content: center;
    align-items: center;
    padding: 16px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .container-27 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 160px;
    grid-row-gap: 160px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .title-section-4 {
    width: 100%;
    max-width: 530px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-153 {
    color: #000;
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .columns-23 {
    width: 100%;
    grid-column-gap: 48px;
    grid-row-gap: 48px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .card-17 {
    width: 100%;
    height: 350px;
    max-width: 368px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 20px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .image-wrapper-37 {
    width: 120px;
    height: 120px;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .content-34 {
    width: 100%;
    height: 370px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .info-6 {
    width: 100%;
    max-width: 300px;
    grid-column-gap: 0px;
    grid-row-gap: 12px;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .text-154 {
    color: #000;
    text-align: center;
    font-size: 16px;
    font-weight: 700;
    line-height: 150%;
    text-decoration: underline;
  }
  
  .text-155 {
    color: #000;
    text-align: center;
    object-fit: fill;
    margin-left: 0;
    margin-right: 0;
    font-size: 16px;
    font-weight: 400;
    line-height: 115%;
  }
  
  .card-18 {
    width: 100%;
    height: 350px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    opacity: .99;
    border: 0 solid #000;
    border-width: 0 1px;
    border-radius: 40px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-bottom: 20px;
    display: flex;
    box-shadow: 0 11px 9px rgba(0, 0, 0, .71);
  }
  
  .container-28 {
    width: 100%;
    max-width: 1200px;
    grid-column-gap: 80px;
    grid-row-gap: 80px;
    justify-content: flex-start;
    align-items: center;
    display: flex;
  }
  
  .column-47 {
    width: 100%;
    grid-column-gap: 10px;
    grid-row-gap: 10px;
    border: 1px solid #000;
    justify-content: flex-start;
    align-items: flex-start;
    display: flex;
  }
  
  .image-wrapper-38 {
    width: 100%;
    height: 500px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    display: flex;
  }
  
  .text-156 {
    color: #000;
    font-size: 32px;
    font-weight: 700;
    line-height: 120%;
  }
  
  .actions-11 {
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex: 0 auto;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 16px;
    display: flex;
  }
  
  .button-52 {
    width: 124px;
    grid-column-gap: 8px;
    grid-row-gap: 8px;
    background-color: #000;
    justify-content: center;
    align-items: center;
    padding: 12px 24px;
    text-decoration: none;
    display: flex;
  }
  
  .button-53 {
    color: #fff;
    text-align: center;
    font-size: 12px;
    font-weight: 500;
    line-height: 140%;
    text-decoration: none;
  }
  
  .columns-24 {
    width: 100%;
    grid-column-gap: 5%;
    grid-row-gap: 5%;
    justify-content: center;
    align-items: center;
    margin-bottom: 2%;
    display: flex;
  }
  
  .content-35 {
    grid-column-gap: 24px;
    grid-row-gap: 24px;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    display: flex;
  }
  
  .small-columns-2 {
    width: 150px;
    grid-column-gap: 32px;
    grid-row-gap: 32px;
    flex: 0 auto;
    justify-content: flex-end;
    align-items: center;
    padding-top: 16px;
    display: flex;
  }
  
  .content-36 {
    width: 142px;
    grid-column-gap: 16px;
    grid-row-gap: 16px;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    display: flex;
  }
  
  .text-157 {
    width: 150px;
    color: #212121;
    font-size: 14px;
    font-weight: 700;
    line-height: 150%;
  }
  
  .text-158 {
    color: #333;
    text-align: center;
    font-size: 14px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-suspendisse-varius-enim-in-eros-elementum-tristique-duis-cursus-mi-quis-viverra-ornare-eros-dolor-interdum-nulla-ut-commodo-diam-libero-vitae-erat-14 {
    color: #212121;
    font-size: 18px;
    font-weight: 400;
    line-height: 150%;
  }
  
  .text-block {
    color: #fff;
  }
  
  @media screen and (max-width: 991px) {
    .navbar-logo-left {
      padding-right: 0;
    }
  
    .navbar-menu {
      max-width: unset;
    }
  
    .navbar-link, .navbar-button {
      justify-content: center;
    }
  
    .navbar-logo-left-2 {
      padding-right: 0;
    }
  
    .navbar-menu-2 {
      max-width: unset;
    }
  
    .navbar-link-2, .navbar-link-3, .navbar-link-4, .navbar-button-2 {
      justify-content: center;
    }
  
    .container, .columns {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-menu-3 {
      max-width: unset;
    }
  
    .navbar-link-5, .navbar-link-6, .navbar-button-3 {
      justify-content: center;
    }
  
    .container-2, .columns-2 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-menu-4 {
      max-width: unset;
    }
  
    .columns-3, .columns-4 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-3 {
      padding-right: 0;
    }
  
    .navbar-menu-5 {
      max-width: unset;
    }
  
    .navbar-link-7, .navbar-link-8, .navbar-link-9, .navbar-button-4 {
      justify-content: center;
    }
  
    .columns-5 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-4 {
      padding-right: 0;
    }
  
    .navbar-menu-6 {
      max-width: unset;
    }
  
    .navbar-link-10, .navbar-link-11, .navbar-link-12, .navbar-button-5 {
      justify-content: center;
    }
  
    .columns-6 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-5 {
      padding-right: 0;
    }
  
    .navbar-link-13, .navbar-link-14, .navbar-link-15, .navbar-button-6 {
      justify-content: center;
    }
  
    .columns-7 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-link-16, .navbar-link-17, .navbar-link-18, .navbar-button-7 {
      justify-content: center;
    }
  
    .columns-8 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-link-19, .navbar-link-20, .navbar-button-8 {
      justify-content: center;
    }
  
    .container-7, .columns-9, .columns-10 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-6 {
      padding-right: 0;
    }
  
    .navbar-menu-7 {
      max-width: unset;
    }
  
    .navbar-link-21, .navbar-link-22, .navbar-button-9 {
      justify-content: center;
    }
  
    .container-9, .columns-11, .columns-12, .container-11 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-7 {
      padding-right: 0;
    }
  
    .navbar-menu-8 {
      max-width: unset;
    }
  
    .navbar-link-23, .navbar-link-24 {
      justify-content: center;
    }
  
    .container-12, .columns-13, .columns-14, .container-14 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-8 {
      padding-right: 0;
    }
  
    .navbar-menu-9 {
      max-width: unset;
    }
  
    .navbar-link-25, .navbar-link-26 {
      justify-content: center;
    }
  
    .container-15, .columns-15, .columns-16, .container-17 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-menu-10 {
      max-width: unset;
    }
  
    .navbar-link-27, .navbar-link-28 {
      justify-content: center;
    }
  
    .container-18, .columns-17, .columns-18, .container-20 {
      flex-direction: column;
      align-items: center;
    }
  
    .navbar-logo-left-9 {
      padding-right: 0;
    }
  
    .navbar-menu-11 {
      max-width: unset;
    }
  
    .navbar-link-29, .navbar-link-30, .navbar-button-10 {
      justify-content: center;
    }
  
    .container-23, .columns-19, .columns-20, .container-25, .columns-21 {
      flex-direction: column;
      align-items: center;
    }
  
    .content-32, .footer-links {
      align-items: center;
    }
  
    .navbar-logo-left-10 {
      padding-right: 0;
    }
  
    .navbar-menu-12 {
      max-width: unset;
    }
  
    .navbar-link-31, .navbar-link-32, .navbar-button-11 {
      justify-content: center;
    }
  
    .container-26, .columns-22, .columns-23, .container-28, .columns-24 {
      flex-direction: column;
      align-items: center;
    }
  
    .content-36 {
      align-items: center;
    }
  }
  
  @media screen and (max-width: 479px) {
    .small-columns, .small-columns-2 {
      flex-direction: column;
      align-items: center;
    }
  }
"""

elements = ['div', 'input', 'label', 'textarea']
classes = ['overlay', 'close', 'contact-form-3', 'container-22', 'section-title', 'get-in-touch', 'text-128', 'form-wrapper', 'w-form', 'form', 'input-wrapper', 'form-block-label', 'form-text-input-4', 'w-input', 'form-text-input-3', 'form-textarea', 'form-button', 'w-button', 'enviado', 'w-form-fail']

extract_styles(css, elements, classes)
