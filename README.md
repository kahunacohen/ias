# ias
A simple feed of real photos taken in Israel challenging the simplistic notion that Israel is an apartheid state.

# Development  
This is a [flask](http://flask.pocoo.org/) app. In development it should be run
by doing: `python ias.py`. A server will automatically be run,
then point your browser to the location indicated by the terminal. To change the host and/or the default port,
pass them as positional parameters to ias.py. Eg. `$ python ias.py somehost 8040` 


# Deploy
Deploying code changes involves a git bare repository on the production server. See [https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks).

The file in this repo, post-receive is the hook that should go in the bare repository on the remote server's `hooks` directory.
To deploy from a local machine to production server:

    !

The master branch is considered stable. Push the master to the production bare remote: `git push production master`. Don't
forget to push commits to the default remote branch, this remote on github.
