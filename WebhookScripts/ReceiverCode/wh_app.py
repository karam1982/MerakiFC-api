from flask import Flask, request

app = Flask(__name__)

@app.route('/whtest', methods=['POST'])
def test_only():
    from apiConn import envTest
    objPayload = request.get_json()  # Get the JSON payload from the request
    # Process the payload and perform necessary actions
    print ("Testing Connection...")
    envTest()
    return (objPayload), 200


@app.route('/mvmotionalert', methods=['POST'])
def mv_task():
    import mvtask
    objPayload = request.get_json()  # Get the JSON payload from the request
    # Process the payload and perform necessary actions
    #print(objPayload)
    urlSnap = mvtask.getsnapshot(objPayload)
    print (urlSnap)
    return urlSnap, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8116, debug=True)