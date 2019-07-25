# Docker

Docker allows users to create a light weight environment that mimics a specific OS while still sharing low level hardware systems. This makes Docker containers much easier to use than virtual machines. Docker containers are very useful for security, reliability, and ease of deployment. There are some amazing things you can do with docker containers. I use them for many of my cloud deployments from website infrastructure to data pipelines. This crash course will get you started, but you should take the time alter on top play around with docker to really explore its potential.

## Installation

```
brew install docker
```

## Use

Docker builds our containers using DockerFiles. First we define such a file. We'll be using the dockerfile in this directory. If you look at this file you'll notice some nice things. At the top we define a "base image". For simplicity I'm using a vanilla ubuntu 18.04 distribution. We then upgrade and install a few useful packages using `apt-get`. Finally, we add a file from this directory to the container and install the packages defined in that file.

To build out "image" we run the following command in the directory containing our dockerfile.

~~~Bash
docker build -t test_container .
~~~

We can then run the container from the image that we just built. We use `-dti` to start the container in an interactive mode, don't worry too much about that. We also share a volume with the host (our computer) using the `-v` argument. This means that we can move files to the docker container using the `Desktop` directory and move files out of the docker container using the `Desktop` directory! Desktop is now shared between the host computer and the container.

~~~Bash
docker run -dti -v ~/Desktop:/Desktop test_container
~~~

The container is running....how to we use it? This is why we started the container in interactive mode. All we need to do is attach to it. TO attach we need the container's id. Let's try to find that:

~~~Bash
docker ps
~~~

use the docker ID to attach to the container.

~~~Bash
docker attach <ID>
~~~

Now we're in the container! We can use the container as we would use our own laptop. Any files saved to `Desktop` will show up on our host computer's `Desktop` directory.

When we are done with the container we can shut it down:

~~~Bash
docker stop $(docker ps -a -q --filter ancestor=test_container --format="{{.ID}}")
~~~

## Using Jupyter

Let's say that we want to run jupyter inside our container. The container doesn't have access to a browser/screen to display the notebook. How can we run the notebook in the container (in our custom environment), but see the notebook on the host browser?

It's actually really easy. First we need to map some ports when running the container:

~~~Bash
docker run -dti -v ~/Desktop:/Desktop -p 8888:8888 test_container
~~~

Now attach to the container:

~~~Bash
docker attach <ID>
~~~

Once in the container run:

~~~Bash
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
~~~

Now open a browser on your host to `localhost:8888` and you should see your jupyter notebook! You may be asked for a token. The token is printed to the terminal when the jupyter notebook is created in the container.

If you want to exit the container but keep the container running, type `cntrl q p` together. The container will run in the background allowing you to work with the notebook without needing the container open on the terminal.
