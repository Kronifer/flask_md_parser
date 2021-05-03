# Flask Markdown Parser

*An Easy Way to Generate Static Webpages with Flask*

## Usage:

```py
@app.route('/')
def home():
    return parse('path/to/markdown/file')
```
It's as easy as that! Flask Markdown Parser converts your markdown into HTML at runtime, so you can easily make your websites without bothering with HTML.