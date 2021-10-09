# KBTU Kampus API

This is the complete source code of REST API 
for working with internal system of [KBTU]. It contains
operations related with students' studying process.

Any [KBTU] student can be accessed to operations 
of internal system via this API.

## Run

Project uses python 3.6.9 and fastapi 0.68.1. 
Also project uses selenium as web driver. 
Currently, it uses geckodriver (firefox).
Guide how to [install](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/) it

Install requirements with

```
pip install -r requirements.txt
```

and run project with

```
uvicorn main:app --reload
```

Use `.env` file in the root of project 
with following configurations

```dotenv
SECRET_KEY=<key>
ACCESS_TOKEN_EXPIRATION=15 # minutes
BACKEND_CORS_ORIGINS='["http://localhost:8000"]'
POSTGRADUATE_PORTAL_URL=https://pge.kbtu.kz
```

## Contributing

TODO: write down contributing section

[KBTU]: https://kbtu.kz
