COSMOS
======

### Run
Export the necessary environment variables.

You MUST set the environment variable `REQUIRED_ENV_VARS` which is
a comma seperated list of strings to tell Django which environment variables to check for.

Example
```
export REQUIRED_ENV_VARS="core,postgres,mailgun"
```

Check settings.py for the full list.

Check the Makefile to understand how to run this project.
