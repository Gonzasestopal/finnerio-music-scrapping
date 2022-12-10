# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from scrapy.utils.log import configure_logging

load_dotenv()

BOT_NAME = "napster-catalog"

SPIDER_MODULES = ["spiders"]
NEWSPIDER_MODULE = "spiders"

USER_AGENT_RELEASE_DATE = '2021-11-01'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept-Language": "en-US,en;q=0.5",
    "Cache-Control": "max-age=0",
}

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE") if os.getenv("LOG_FILE", "") else None

EXTENSIONS = {}

NAPSTER_API_URL = os.getenv("NAPSTER_API_URL", "")
NAPSTER_API_KEY = os.getenv("NAPSTER_API_KEY", "")

configure_logging()
