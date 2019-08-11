# code-backup

A backup script for backing up my projects

## Why build this?

There were/are 2 main reasons why I started this project.
1. I wanted a mean to backup projects that may not be hosted on GitHub, and didn't want to backup the projects manually.
2. It was a fun project idea

## Who is this for?

I designed it to suit my needs, and the way I backup projets -- and basically everything else. Although it can be altered slightly to suit your needs. You would need to change 3 things if you decide to use this yourself.

1. `src_dir` this is where you work on your projects. I work on projects in one directory - to keep things organised - and then backup them up to 2 other directories. 1) A external HDD 2) A online directory. In this case a OneDrive folder on my PC, which acts as a local git repo
2. `git_dir` this is my online/git backup directory. Change this to your online backup folder if you have one -- highly recommend you do. Read [this](https://www.hanselman.com/blog/TheComputerBackupRuleOfThree.aspx) or [this](https://www.nakivo.com/blog/3-2-1-backup-rule-efficient-data-protection-strategy/) for more info.
3. `external_dir` this is essentially the same as above, but for your external backup location.

## Contributing?

Any code improvements or best practices are welcome. Fork this project, make your changes and then submit a PR. Your PR should explain what you did, and why you did it -- rule of thumb, be descriptive.
