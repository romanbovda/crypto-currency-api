develop:
	docker build --no-cache -t crypto-currency-api . && docker run -it -p 5000:5000 crypto-currency-api

test:
	 python -m venv .venv && source .venv/bin/activate && pytest .
