build:
	@docker build -t architecture-diagrams .

run:
	@docker run \
		--name architecture-diagrams \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-it \
		-v $(PWD):/src \
		architecture-diagrams src/$(file).py
