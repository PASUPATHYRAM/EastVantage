# FastAPI Address Book

This is a simple address book application built with FastAPI.

## Features

- Add an address with name and phone number.
- Get all addresses.
- Update an address by ID.
- Delete an address by ID.
- Makes third-party requests to get latitude, longitude, state, city, and country based on the provided address.

## Endpoints

The application provides the following endpoints:

- `POST /v1/address/add`: Add a new address.
- `GET /v1/getall`: Get all addresses.
- `PUT /v1/update/{id}`: Update an address by ID.
- `DELETE /v1/delete/{id}`: Delete an address by ID.

## Installation

1. Clone this repository.
2. Install the dependencies.

```bash
pip install fastapi uvicorn sqlalchemy

## ApiCall
- Create an account in opencage and have the apikey
- Should use the apikey while making request (Please refer requestcall.py)
