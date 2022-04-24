<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Discord][discord-shield]][discord-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />


<h1 align="center">Discord Job Finder</h3>

  <p align="center">
    Learning how to code is a rewarding, yet difficult task. Finding a job is even more difficult! This bot intends on making the job search easier for programmers so that they can focus more attention on building their skills and staying updated with the latest trends.
    <br />
    <br />
    This project grabs 25 job postings from LinkedIn and sends them to our discord chat, where you can find a ton of helpful resources and community members that are all looking to uplift one another. The postings are all remote Software Engineering positions that are either listed as entry level or internships.
    <br />
    <br />
    This bot alleviates some of the stresses and pressure of searching for jobs by taking care of that for you. I believe that coders should be able to spend more time coding and less time worrying about finding the right opportunity!
    <br />
    <a href="https://github.com/OREdwardsJr/job-scraping-bot><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OREdwardsJr/job-scraping-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/OREdwardsJr/job-scraping-bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was birthed from a desire to contribute to the Computer Science/Tech community. One of the most important aspects of this community is its willingness to help and share. Therefore, I desire to do the same.
                                  
Within this project are two bots that have a loose connection with one another:
                                  
#### Linked-In Job Scraper [(linked-in-bot.py)](https://github.com/OREdwardsJr/job-scraping-bot/blob/main/modules/linked_in_bot.py)
This bot scrapes LinkedIn for 25 Remote(USA) Entry-Level Software Engineer positions. It is packaged to be used immediately without any prior knowledge of webscraping, unless you'd like to change the search configurations. If you'd like to do so, but are unsure of how to adjust the bot, then please contact me. If enough interest is captured then I'll expand this ReadMe to include instructions on how to do so.                            

#### Discord Automated Poster [(discord-bot.py)](https://github.com/OREdwardsJr/job-scraping-bot/blob/main/modules/discord-bot.py)
This bot posts to Discord at 8am PST everyday with jobs that are passed as an argument from the linked-in bot. It is configured to receive the job postings as an import from [linked-in-bot.py](https://github.com/OREdwardsJr/job-scraping-bot/blob/main/modules/linked_in_bot.py). The jobs are passed as a nested list, which are sent individually until all inner-lists are popped.

                                  
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.10](https://docs.python.org/3/)
* [Discord API](https://discordpy.readthedocs.io/en/stable/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [Amazon EC2](https://docs.aws.amazon.com/ec2/index.html)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The LinkedIn bot is ready for execution as long as you have the appropriate dependencies - [imports.py](https://github.com/OREdwardsJr/job-scraping-bot/blob/main/modules/imports.py) has a list of necessary dependencies for the Python script. While some libraries come pre-installed with Python (EG: Requests), others may not. A few simple pip3 install commands will get the necessary dependencies added to your machine. If you are unfamiliar with how to install Python packages, then I'd recommend that you simply google how to do so. It's a simple process.
                                
Discord's API, however, requires that you register for unique keys. This is to prevent someone misusing your bot and having your permissions stripped. Take a quick peek at the [Discord Developer Portal](https://discord.com/developers/docs/intro) to grab your own set of keys. I have used environment variables to protect my keys from public viewing. You will need to replace assign your token to the TOKEN variable. You will also need to grab your desired [Discord Channel ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) and insert it into the GUILD variable. However, once those variables are configured then you are ready to go 😄                                

### Automatic posting

If you would like to have this project run automatically then there are a few ways to do so. You will need to decide the best way to execute this for yourself. I ran into challenges in the two methods that I've tried. I will list my methods below:
                                
#### Cron (Functional but currently deprecated in favor of [launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html)
Using Cron, I can schedule my task to run in the background successfully. The problem with this method is that your server needs to be active at the scheduled time or the job will be skipped until the next scheduled time. I find it unreliable to depend on having my computer active at a certain time, everyday.
                                
#### EC2
This was my preferred method until I ran into a block from LinkedIn. After launching my instance, LinkedIn gave me 999 responses to my request through the Ubuntu AMI. It appears that you can make successful requests from your computer but LinkedIn blocks requests to his site from EC2 Ubuntu servers. I will update this if I come across a workaround.                              


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

If you are inexperienced with web-scraping then please make sure you are aware of [LinkedIn's Policy](https://www.linkedin.com/robots.txt) for bots. They are prohibited without express written-consent. **You should use the LinkedIn bot as a study tool until you have been provided written-consent**. 
                                
Discord is more friendly to bots. It's still important that you read their terms and conditions. However, generally speaking, you should be able to use discord-bot.py safely.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Orlando Edwards Jr. - [@LinkedIn](https://linkedin.com/in/orlando-edwards-jr)

Project Link: [https://github.com/OREdwardsJr/job-scraping-bot](https://github.com/OREdwardsJr/job-scraping-bot)

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[discord-shield]: https://raw.githubusercontent.com/OREdwardsJr/job-scraping-bot/main/images/Discord-Logo%2BWordmark-Color.svg
[discord-url]: https://discord.gg/NrJyxXQgdz
[linkedin-shield]: https://raw.githubusercontent.com/OREdwardsJr/job-scraping-bot/main/images/LI-Logo.png
[linkedin-url]: https://www.linkedin.com/in/orlando-edwards-jr/
[product-screenshot]: images/screenshot.png
