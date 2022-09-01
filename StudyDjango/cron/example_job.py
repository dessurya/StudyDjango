import time
from ..models_dir.user import UserModel

def jobs_add_user():
    getTime = str(time.time())
    store_name = 'aaa_cron_jobs_store_'+getTime
    store_email =  getTime+'mail.cron@cron.mail'
    users = UserModel.objects.using('servlaraqu').create(name=store_name,email=store_email)