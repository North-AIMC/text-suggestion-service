# Biased Text Suggestion Service
* Python (Flask) application text-suggestion service
* Deployable to Google Cloud Platform App Engine
* Deliver current/next word suggestions based given text
* *Importantly*, text suggestions are biased based on sentiment
More details can be found in the related [paper](https://aclanthology.org/2021.hcinlp-1.17.pdf).

## Run locally or deploy the app to GCP
Setup virtual environment:
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
Run locally:
```
python app.py
```
Deploy:
```
gcloud app deploy app.yaml
```
