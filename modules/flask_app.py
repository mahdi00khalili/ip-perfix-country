from flask import Flask, jsonify
from finding_countries import finding_countries

app = Flask(__name__)


@app.route('/<prefix>/api', methods=['GET'])
def api_with_prefix(prefix):
    # Extract the "a.b" part from the prefix
    prefix_parts = prefix.split('.')
    # Ensure there are exactly 2 parts and both are numeric
    if len(prefix_parts) == 2 and all(part.isdigit() for part in prefix_parts):
        api_prefix = '.'.join(prefix_parts)
    else:
        return jsonify({"error": "Invalid prefix format; it must contain exactly two numeric parts."}), 400

    # Handle the GET request

    countries = finding_countries(api_prefix)

    return jsonify(countries)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
