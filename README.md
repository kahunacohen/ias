# What is it?
An "infinitely" scrolling feed of Israeli street-scenes challenging the simplistic notion that Israel is an apartheid state. 

# Technical Details
It's a [flask](http://flask.pocoo.org/) app. Flask is a minimalistic Python web framework that mainly routes requests
to handler functions and renders data to templates. Think Django or Ruby on Rails, without a lot of jazz.

Paging is done server-side, but JavaScript injects new pages dynamically on page-scroll. This makes the app SEO friendly
and addressable yet gives the impression that the photo feed never stops... 

`process-images.py` at the root directory is responsible for batch normalizing images before deploy. When deploying
the app (see below) this script is called automatically. When running a local server for development, you must call
this script on the command-line. See comments in the script for more details.

# Development  
In development it should be run
by doing: `python ias.py`. A server will automatically be run,
then point your browser to the location indicated by the terminal. To change the host and/or the default port,
pass them as positional parameters to ias.py. Eg. `$ python ias.py somehost 8040` 

# Deploy
Deploying code changes involves a git bare repository on the production server. See [https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks). The
bit on the production is already set up, so all you have to do is setup the local part. See below.

The file in this repo, post-receive is the hook that should go in the bare repository on the remote server's `hooks` directory.
To deploy from a local machine to production server:

    !

The master branch is considered stable. Push the master to the production bare remote: `git push production master`. Don't
forget to push commits to the default remote branch, this remote on github.

To set up deploy from a new local repo:

1. *Set up SSH keys*. See: https://help.github.com/articles/generating-ssh-keys/
1. *Clone the repo from github*: `git clone git@github.com:kahunacohen/ias.git;cd ias`
1. * Add a "production" remote branch, linking to the remote bare repo: `git remote add production ssh://kahunacohen@HOST/PATH_TO_IAS_BARE_REPO`.
1. To deploy changes, ensure the local branch is up-to-date with the remote: `git pull`. Then: 
`git push production master`.
1. On the host server, make sure the following environment variables are set:
   * `$PATH_TO_WSGI_APP`
   * `$PATH_TO_BARE_GIT_REPO`
   * `$PATH_TO_VIRTUAL_ENV`
1. Ensure the file `post-receive` in this github repo is in the `hooks` directory in the bare-repo on the host server. 
