# weather-application
The weather application is Google Cloud Function using the Python language, to minimize overhead.
The API_KEY for Openweathermap API is stored in Secrets Manager. The function will bea 
automatically deployed, when a code update is pushed to the github repo, using Cloud Build Github APP
to connect the repository.

Triggered by: 
```
curl -m 70 -X POST https://europe-west1-op-test-service-project.cloudfunctions.net/weather-application-function \
-H "Authorization:bearer $(gcloud auth print-identity-token)" \
-H "Content-Type:application/json" \
-d '{"place": "Stockholm"}'
```

To be able to receive global weather alerts:
* First ask for access
* Setup a callback endpoint to receive, implement a new cloud function which transforms the json structure,
* and pushes a pub/sub event captured by another function which handles the way the end-user output should be

Architecture decisions:
Start simple and continue to add complexity when needed

Improve error handling
Clean up code and separate for further reuse of functionality

Automate with terraform setup everything with the Infrastructure as code
Add unittests
Update configuration
Clear separation in GCP projects for different environments
Add a LoadBalancer in front, managed certificate, NEG, backend service, https, dns a record and caa records(terraform)