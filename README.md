# (Biased) Text Suggestion Service

* Python (Flask) application text-suggestion service
* Deployable to Google Cloud Platform App Engine
* Delivers current/next word suggestions based on given text
* Underlying Language Model loaded from Hugging Face [models](https://huggingface.co/models)
* Text suggestions *biased* using sentiment-based re-ranking
* Parameters fine-tuned using custom [simulation environment](https://github.com/North-AIMC/text-suggestion-experiments/blob/master/evaluation.py)
* Cloud resources decided using [LOCUST](https://locust.io/) load testing

Motivation for the services can be found in the related [paper](https://aclanthology.org/2021.hcinlp-1.17.pdf).

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
