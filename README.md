# Finnerio Music Scrapper

Napster web scrapping project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)


## Prerequisites

Make sure your DB is up and running.

## Installation

Install dependencies

Copy and replace .env.example

## Usage

Run commands through scrapy to obtain proper information data.

Make sure you run crawlers in this order.

- scrapy crawl genres
- scrape crawl subgenres
- scrapy crawl artists
- scrapy crawl albums
- scrapy crawl songs

## Docker

Build app image

- docker build -t finnerio-music-scrapper .

Run image

- docker run -e "NAPSTER_API_KEY=xxxx" -e "NAPSTER_API_URL=xxxx" -e "..." finnerio-music-scrapper <CMD>

## Support

Please [open an issue](https://github.com/gonzasestopal/finnerio-music-scrapping/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/gonzasestopal/finnerio-music-scrapping/compare/).
