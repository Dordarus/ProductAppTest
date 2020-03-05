app_name=product-app
build:
	@docker build -t $(app_name) .
run:
	docker run --name $(app_name) -d -p 5000:5000 --rm $(app_name):latest
stop:
	@echo 'Stoping container...'
	@docker stop $(app_name)