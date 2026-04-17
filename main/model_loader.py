import joblib
from django.conf import settings

model = joblib.load(settings.MODEL_PATH)