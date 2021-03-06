# Instagram Smart Nine

[![PyPI](https://img.shields.io/badge/pipy-v0.0.9-blue)](https://pypi.org/project/smart-nine/)

smart-nine is a command-line application written in Python that generates an Instagram user's smart nine photograph collage from a particular year.

Example collage:

<p align="center">
<img src="https://images.squarespace-cdn.com/content/5928b76015cf7dec0ac75521/1609380944062-197ANESF9YH2QL3RIFIM/bodegadude_2019.jpg?format=1500w&content-type=image%2Fjpeg"/>
</p>

## Install

To install smart-nine:

```
$ pip install smart-nine
```

## Usage

To generate a smart nine collage:

```
$ smart-nine <username> -u <your username> -p <your password>
```

*NOTE: To generate a smart-nine collage for a `<username>` which media is set to private, `<your username>` must be an approved follower of `<username>`.*

The resulting collage will be saved as: `/smart-nine-output/<username>_<year>.jpg`

## Options
|Argument| Description|
|--|--|
|--help, -h| Show help message and exit.|
|--login-user, -login_user, -u| Instagram scraper login user.|
|--login-pass, -login_pass, -p| Instagram scraper login password.|
|--year, -y| Year to use as filter for the smart nine collage.|
|--timezone, -t| Timezone of Instagram user(s).|
|--scrape, -s| Data scraping flag - set to False to work with local data.|

## Motivation
The current software applications for generating Instagram year photo collages suffer from the following:

- They only display the 9 photographs that have the most likes.
- They require you to enter your personal email (which they use to send spam), or...
- They overlay unwanted graphics on top of the resulting image.

## License

MIT License

Copyright (c) 2020 Ulysses Lizarraga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
