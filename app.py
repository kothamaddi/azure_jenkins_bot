from flask import Flask, request, jsonify
import jenkins_integration

app = Flask(__name__)

@app.route("/create-pipeline", methods=["POST"])
def create_pipeline():
    # Parse request JSON
    data = request.json

    # Extract message text from request
    message_text = data["message"]["text"]

    # Check if the message contains the command to create a pipeline
    if "create pipeline" in message_text.lower():
        # Call Jenkins API to create pipeline
        success = jenkins_integration.create_pipeline()

        if success:
            return jsonify({"message": "Jenkins pipeline created successfully!"})
        else:
            return jsonify({"message": "Failed to create Jenkins pipeline. Please try again later."})

if __name__ == "__main__":
    app.run()
