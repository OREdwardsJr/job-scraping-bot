#LinkedIn Bot
import requests
from bs4 import BeautifulSoup

#Discord Bot
from dotenv import load_dotenv
import os, asyncio, datetime
from discord.ext import commands
from pytz import timezone