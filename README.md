# Finnerio Music Scrapper

Napster web scrapping project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install dependencies

Copy and replace .env.example

Make sure db is running

## Usage

Run commands through scrapy to obtain proper information data.

- scrapy crawl genres

## Docker

Build app image

- docker build -t finnerio-music-scrapper

Run image

- docker run -e "NAPSTER_API_KEY=xxxx" -e "NAPSTER_API_URL=xxxx" finnerio-music-scrapper

## Support

Please [open an issue](https://github.com/gonzasestopal/finnerio-music-scrapping/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/gonzasestopal/finnerio-music-scrapping/compare/).

Add data persistance layer
Add db-layer
