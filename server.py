
#!./env/bin/python
from flask import * 
from worker import *

app = Flask(__name__)

@app.route('api/tasks', methods=['POST']) 
def create_task(): 
    if not request.json or not 'type' in request.json or 'id' in request.json: 
        abort(400) 
    task_type =  request.json['type']
    target_id = request.json['id']
    if task_type == "skill":
        analyze_all_job_one_skill(target_id)
        return jsonify({'status': "success"}), 201
    elif task_type == "job":
        analyze_one_job_all_skill(target_id)
        return jsonify({'status': "success"}), 201

if __name__ == '__main__': 
    app.run(port= 5007)