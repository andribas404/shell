#!/bin/bash
heroku login

heroku container:login

heroku container:push web
