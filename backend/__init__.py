"""
The backend code has been split into separate modules that concern different aspects of the app:

- :mod:`routers` - FastAPI routers and endpoints are defined here
- :mod:`models` - Response & Body models used in communication with the API
- :mod:`services` - all the data processing logic, independent from the rest
  of the code
- :mod:`dependencies` - FastAPI dependencies and other components which help
  connect `routers` and `services`
"""