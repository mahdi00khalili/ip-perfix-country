
# IP Prefix Country

## Description

`ip-prefix-country` is a project that retrieves all IP addresses for every country from [ip2location.com](https://www.ip2location.com/) and stores them in a database categorized by IP prefix and country. It also provides a Flask API to retrieve the saved data.

## Setup Instructions

### Step 0: Clone the Project Repository

Clone the project repository to your local machine using the following command:

```bash
git clone <repository-url>
cd ip-prefix-country
```

### Step 1: Install Dependencies

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 2: Set the PYTHONPATH

Add the project path to your `PYTHONPATH` environment variable:

```bash
export PYTHONPATH=$PYTHONPATH:path-to-project/ip-prefix-country
```

Make sure to replace `path-to-project` with the actual path to the project on your local machine.

### Step 3: Create the `config.py` File

Copy the example configuration file and rename it to `config.py`:

```bash
cp settings/config.example.py settings/config.py
```

Edit the `settings/config.py` file to configure your project settings (e.g., database connection, API keys, etc.).

### Step 4: Run the Project

To manage the project, run the following command:

```bash
python3 manage.py
```

This will present you with a menu:

```
1. Initialize the project
2. Run the Flask app
0. Quit
```

#### Operation 1: Initialize the Project

Select `1` to initialize the project. This will retrieve all the IP data for every country and save it into the database.

#### Operation 2: Run the Flask App

Once the data is saved, select `2` to start the Flask web application. The Flask app will run on `http://127.0.0.1:5000/`.

### Using the API

After the Flask app is running, you can request data from the following endpoint:

```
http://127.0.0.1:5000/x.y/api
```

Make sure to replace `x.y` with the desired parameters or endpoint specifics as defined in the Flask API.
