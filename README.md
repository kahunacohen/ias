# israelapartheidstate.com
A simple feed of real photos taken in Israel challenging the simplistic notion that Israel is an apartheid state.

# Development  
This is a [flask](http://flask.pocoo.org/) app. In development it should be run
by doing: `python israelapartheidstate.py`. A server will automatically be run,
then point your browser to the location indicated by the terminal.

# Deploy
Deploying code changes involves a git bare repository on the production server. See [https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks).

The master branch is considered stable. Push the master to the production bare remote: `git push production master`. Don't
forget to push commits to the default remote branch, this remote on github.
