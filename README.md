My Contact
----------

My contact book app that runs on Google App engine python 2.7 standard runtime.

Please use data/sample_contactbook.csv for testing.

The CSV must have a header with following columns

```
first_name,last_name,email
```

## Setup

`$ make install`

## Development

To turn on debug mode, set environment variable `FLASK_DEBUG` to `True`

## Deploy to Google App Engine

`$ make deploy`
