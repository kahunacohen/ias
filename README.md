# ias
A simple feed of real photos taken in Israel challenging the simplistic notion that Israel is an apartheid state.

# Development  
This is a [flask](http://flask.pocoo.org/) app. In development it should be run
by doing: `python ias.py`. A server will automatically be run,
then point your browser to the location indicated by the terminal. To change the host and/or the default port,
pass them as positional parameters to ias.py. Eg. `$ python ias.py somehost 8040` 


# Deploy
Deploying code changes involves a git bare repository on the production server. See [https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks). The
bit on the production is already set up, so all you have to do is setup the local part. See below.

The master branch is considered stable. Push the master to the production bare remote: `git push production master`. Don't
forget to push commits to the default remote branch, this remote on github.

To set up deploy from a new local repo:

1. *Set up SSH keys*. See: https://help.github.com/articles/generating-ssh-keys/
1. *Clone the repo from github*: `git clone git@github.com:kahunacohen/ias.git;cd ias`
1. * Add a "production" remote branch, linking to the remote bare repo: `git remote add production ssh://kahunacohen@HOST/PATH_TO_IAS_BARE_REPO`.
1. To deploy changes, ensure the local branch is up-to-date with the remote: `git pull`. Then: 
`git push production master`.
