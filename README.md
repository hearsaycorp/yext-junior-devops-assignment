# Yext Junior DevOps Assignment

## Introduction

Welcome to the DevOps assignment part of your Yext journey! We present you
with a small set of tasks that will help us decide your skill level with various
tools and technologies.

The assignment should take less than 2 hours to complete.

We created a basic setup for you which includes:

* an API and tests for it
* a Dockerfile
* a docker-compose
* a small Github Actions pipeline to do the tests, linting and the build of the
  docker image

Some of these have bugs which you should fix. If you are not familiar with some
of these technologies don't be discouraged, we designed these tasks so that
people without prior knowledge can still be able to do them.  

## Guidance

To help you we'll provide you with some docs that might be helpful while working
on the assignment:

* [Git branching introduction](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
* [Docker installation manual](https://docs.docker.com/engine/install/)
* [Docker build guide](https://docs.docker.com/build/guide/)
* [How to use docker-compose](https://docs.docker.com/get-started/08_using_compose/#run-the-application-stack)
* [Python Flask quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
* [Nginx Reverse Proxy reference](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
* [GitHub Actions quickstart](https://docs.github.com/en/actions/quickstart)

## First steps

As a first step you should create a new **private repository** of your own from
this template. To do so click the green `Use this template` button and then
select `Create a new repository`, from then set yourself as `Owner` give a name
to the repo and **click the radio button next to `Private`** to make it private.

## Tasks

From here you can proceed with the following tasks:

* Add a new URL endpoint to the Flask API with the `/coffee` route. It should
  return the text `Let's make some tea!` with the HTTP status code of `418`
  (hint: check the docs for this status code)
* Build the Docker image described in the `Dockerfile` and tag it with a name
  that will be recognized by the `docker-compose.yml`
* Update the pipeline by adding the build and tag command you used in the
  previous step to the `.github/workflows/build-and-test.yml` right after the
  `run:` command on line 22
* As you might notice the current Dockerfile created a huge image, slim it down
  to a smaller size, you can combine multiple approaches to do this
* There is a misconfiguration in the `docker-compose.yml` which stops Nginx from
  serving the API, fix that (you can use `docker-compose up` or
  `docker-compose up -d`
  [dont forget to use `docker-compose down` in this case] to start the stack).
  You can use `curl -s 127.0.0.1:8080/coffee` to check if your API endpoint and
  `docker-compose` works correctly 
* Push your changes to your feature branch, it will automatically kick off the
  pipeline (as can be seen in the Actions tab of the repo), both jobs should
  succeed, but the build might pass even if there is an issue, check the logs to
  verify this (there is some helpful output provided at the end of the
  `Build app image` job). If you see an issue feel free to work on the code
  further, every new push will start the pipeline again

## Wrap up

When you successfully finished the assignment or your time has ran out it's time
to submit the link to your repository while also sharing it with us. Go to
`Settings`, in the left panel click `Collaborators` and add the following
people:

* csizmaziakiki
* lopezm1
* renegillson
