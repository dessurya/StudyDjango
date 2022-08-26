from django.urls import path
from ..views_dir import trialView

urlpatterns = [
    path('', trialView.Index, name='pageTo.trial'),
    path('list-data', trialView.ListData, name='trial.list-data'),
    path('open-data', trialView.OpenData, name='trial.open-data'),
    path('store-data', trialView.StoreData, name='trial.store-data'),
    path('delete-data', trialView.DeleteData, name='trial.delete-data'),
]