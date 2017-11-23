install:
	pip install -r requirements/prod.txt -Yt lib

run:
	make install
	dev_appserver.py .

deploy:
	gcloud app deploy

browse:
	gcloud app browse
