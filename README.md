# Annotation Platform

## Importing claims

Download the claim dataset:
```
mkdir data
wget "https://drive.google.com/uc?export=download&id=1aZdXaS9YDGx7Bt6qYK-hoCUBj_QSEP7l" -P data -O partiledardebatt-22-01-12-filtered.csv
```

To import claims from the .csv file, run the following command:

```
python manage.py import_claims data/artiledardebatt-22-01-12-filtered.csv
```

