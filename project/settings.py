SECRET_KEY='dummy'
DEBUG=True
ALLOWED_HOSTS=['*']

INSTALLED_APPS=[
    'django.contrib.staticfiles',
]

MIDDLEWARE=[]

ROOT_URLCONF='project.urls'

TEMPLATES=[{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':['project/templates'],
    'APP_DIRS':True,
    'OPTIONS':{},
}]

STATIC_URL='/static/'
STATICFILES_DIRS=['project/static']
