class Student(Resource):
    def get(self, registration=None, department=None):
        data = []

        if registration:
            studnet_info = mongo.db.student.find_one(
                {"registration": registration}, {"_id": 0})
            if studnet_info:
                resp = jsonify(studnet_info)

                return set_response_headers(resp)
            else:
                return {"response": "no student found for {}".format(registration)}

        elif department:
            cursor = mongo.db.student.find(
                {"department": department}, {"_id": 0}).limit(10)
            for student in cursor:
                student['url'] = APP_URL + \
                    url_for('students') + "/" + student.get('registration')
                data.append(student)
            resp = jsonify({"department": department, "response": data})
            return set_response_headers(resp)

        else:
            cursor = mongo.db.student.find(
                {}, {"_id": 0, "update_time": 0}).limit(10)

            for student in cursor:
                print student
                student['url'] = APP_URL + \
                    url_for('students') + "/" + student.get('registration')
                data.append(student)
            resp = jsonify(data)
            return set_response_headers(resp)

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            registration = data.get('registration')
            if registration:
                if mongo.db.student.find_one({"registration": registration}):
                    return {"response": "student already exists."}
                else:
                    mongo.db.student.insert(data)
            else:
                return {"response": "registration number missing"}

        return redirect(url_for("students"))

    def put(self, registration):
        data = request.get_json()
        mongo.db.student.update({'registration': registration}, {'$set': data})
        return redirect(url_for("students"))

    def delete(self, registration):
        mongo.db.student.remove({'registration': registration})
        return redirect(url_for("students"))
