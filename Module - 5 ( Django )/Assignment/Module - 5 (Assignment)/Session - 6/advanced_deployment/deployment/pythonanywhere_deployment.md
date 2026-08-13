# PythonAnywhere Deployment

1. Upload the project.
2. Create a virtualenv and install `requirements.txt`.
3. Run `python manage.py migrate`.
4. Run `python manage.py collectstatic --noinput`.
5. Configure the WSGI file using `pythonanywhere_wsgi.py`.
6. Replace `YOUR_USERNAME` with the PythonAnywhere username.
7. Configure Mailgun, Twilio, Stripe and Google environment variables.
8. Reload the web app.
9. Test `POST /api/v1/send-email/` with Postman.
10. Include a screenshot of the live response in the submission.

The live URL is account-specific and is not hard-coded.
