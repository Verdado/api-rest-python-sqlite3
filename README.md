# Pre - setup

1. Make sure to download docker desktop
```
https://www.docker.com/products/docker-desktop
```
2. Go to gmail security and enable app access
```
https://myaccount.google.com/security
enable less secure app access
```
3. Setup your admin email: (modify docker-compose file)
sample below:
```
gmail_uid=myemail@gmail.com
gmail_password=myp@ssword
```
4. Make sure no proxy in your environment.

# Building

```
1. cd events_api
2. docker-compose build (building the images.)
3. docker-compose up -d (starting the application.)
4. make load_sqlite3 (this will load sample data in database if you want it pre-loaded.)
```

# Pre - load tables (load one event and one user)
```
make load_sqlite3
```

# GET

List all events:
```
http://localhost:8000/events
```

list all users:
```
http://localhost:8000/users
```

list all signed users for a particular event:
```
http://localhost:8000/event_users/<event_uid>
http://localhost:8000/event_users/1
```

List specific event information:
```
http://localhost:8000/events/<event_uid>
```

# POST

Create an event:
```
curl -X POST -H "Content-Type: application/json" http://localhost:8000/event -d @json_payload_samples/create_event.json
```

Create user:
```
curl -X POST -H "Content-Type: application/json" http://localhost:8000/user -d @json_payload_samples/create_user.json
```

Event signup (Auto email invite):
```
curl -X POST -H "Content-Type: application/json" http://localhost:8000/event_signup -d @json_payload_samples/event_signup.json
```

Signing up email that doesn't exists in users will fail with below constraint:
```
sqlite3.IntegrityError: FOREIGN KEY constraint failed
```

# Delete

Remove email from the event (unsign):
```
curl -X DELETE -H "Content-Type: application/json" http://localhost:8000/event_unsign -d @json_payload_samples/event_unsign.json
```
