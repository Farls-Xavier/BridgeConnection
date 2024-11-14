from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = {}

@app.route("/send_data", methods=["GET"])
def send_data():
    client_id = request.args.get("client_id")
    data = request.args.get("data")
    userId = request.args.get("userId")

    if client_id and data and userId:
        if client_id not in data_store:
            data_store[client_id] = {}
        if userId not in data_store[client_id]:
            data_store[client_id][userId] = []
        data_store[client_id][userId].append(data)       
        print(f"Data received - client_id: {client_id}, userId: {userId}, data: {data}")
        return jsonify({"status": "success"})   
    return jsonify({"status": "error", "message": "Missing params"})

@app.route("/get_data", methods=["GET"])
def get_data():
    client_id = request.args.get("client_id")

    if client_id in data_store:
        data = data_store[client_id]
        data_store[client_id] = {}
        print(f"Data sent - client_id: {client_id}, data: {data}")
        return jsonify({"data": data})
    return jsonify({"data": {}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
