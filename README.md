# Opt-ID-Env-Test

[![Build Status](https://travis-ci.com/JossWhittle/Opt-ID-Env-Test.svg?branch=master)](https://travis-ci.com/JossWhittle/Opt-ID-Env-Test) [![Coverage Status](https://coveralls.io/repos/github/JossWhittle/Opt-ID-Env-Test/badge.svg?branch=main)](https://coveralls.io/github/JossWhittle/Opt-ID-Env-Test?branch=main)

Uses Travis CI to test Docker images for the environments needed by the Opt-ID software developed by the Rosalind Franklin Institute and Diamond Light Source. https://github.com/DiamondLightSource/Opt-ID

Docker image pulled from `josswhittle/opt-id:env-v3` (see: https://hub.docker.com/r/josswhittle/opt-id/tags).

Pull down the environment image we're going to use

```
docker pull josswhittle/opt-id:env-v3
```

Start a container running the image that will keep running until we stop it...

  - `-itd` 
 	to run the container in interactive mode, and detached so that it keeps running after this line

  - `--name` 
 	env We can refer to this running container by the name "env"

  - `--env-file <(env | grep TRAVIS)`
	Grab all environment varaibles from the host starting with "TRAVIS" and forward them into the container to allow coveralls to report properly

  - `-v $(pwd):/tmp/repo/`
	Mount the current directory on the host (git repo root) to the directory /tmp/repo/ in the container
 
  - `-w /tmp/repo/`
 	Set the current working directory inside the container to the root of the git repo

  - `josswhittle/opt-id:env-v3`
	The docker image to run

```
docker run -itd --name env --env-file <(env | grep TRAVIS) -v $(pwd):/tmp/repo/ -w /tmp/repo/ josswhittle/opt-id:env-v3
```

Install the git repo into the running container (executes its setup.py)

```
docker exec env pip install -e .
```

Run the python unit tests with code coverage on the git repo

```
docker exec env python -m pytest --cov=src/optidenvtest tests/
```

Report the code coverage results to coveralls

```
docker exec env coveralls
```

Kill the container

```
docker stop env
```