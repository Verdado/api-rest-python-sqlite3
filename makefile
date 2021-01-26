load_sqlite3:
	curl -X POST -H "Content-Type: application/json" http://localhost:8000/event -d @json_payload_samples/create_event.json
	curl -X POST -H "Content-Type: application/json" http://localhost:8000/user -d @json_payload_samples/create_user.json
