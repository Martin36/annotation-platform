# Annotation Platform

## Importing claims

Download the claim dataset:
```
mkdir data
wget "https://drive.google.com/uc?export=download&id=1aZdXaS9YDGx7Bt6qYK-hoCUBj_QSEP7l" -P data -O partiledardebatt-22-01-12-filtered.csv
```

To import claims, run the following command:

```
python manage.py import_claims
```

It will import the claims from the file in dropbox

## Deploying

Before being able to deploy the app, some environment variables needs to be set. First set the `DJANGO_ENV` to `production` with the following command:
```
heroku config:set DJANGO_ENV=production
```

Set the `SECRET_KEY` in Heroku:
```
heroku config:set SECRET_KEY=<your_secret_key>
```

Verify that the key was set correctly:
```
heroku config:get SECRET_KEY
```

To deploy the app to Heroku:
```
git push heroku master
```

