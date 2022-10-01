# LAB - Cookie Stand API Deployement
### Author: Brendon
### Links and Resources
- [back-end server url]([#](http://100.27.22.255/)) (HTTP not HTTPS)
- [front-end application](#) (when applicable)
### Setup
`.env` requirements (where applicable)

**i.e.**

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db
#### How to initialize/run your application (where applicable)
- e.g. `python main.py`
#### How to use your library (where applicable)
#### Tests
- How do you run tests?
- Any tests of note?
- Describe any tests that you did not complete, skipped, etc





# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `things` folder to the app name of your choice
- Search through entire code base for `Thing`,`Things` and `things` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
- Update ThingModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
- Run makemigrations and migrate commands
- Run `collectstatic` if needed.
- Optional: Update `api_tester.py`
