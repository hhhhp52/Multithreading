
## Build image
build-image:
	docker build --no-cache -t thread:latest .

run-docker-job:
	docker run thread:latest

run-local-job:
	python3 thread.py