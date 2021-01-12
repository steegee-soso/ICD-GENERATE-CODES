from flask import Flask, jsonify, request, Response,abort
from controller.generate_icd_codes import *
from controller.Validator import *
import math

app = Flask(__name__)

generate_code = GenerateIcDCode()
validator = Validate()


def build_ic_types():
    record = generate_code.get_all_icd_code_type()
    build_icd = {}
    if len(record) > 0:
        for data in record:
            build_icd[data[1]] = {"min_num": data[2], "max_num": data[3], "id": data[0]}
    return build_icd
    pass


build_records = build_ic_types()


@app.route('/api/v1/test', methods=['GET'])
def function():
    if request.method != "GET":
        return abort(400,mesage="jdjdj")

    return jsonify({"msg": "Testing the Program"})


@app.route("/api/v1/create", methods=['POST'])
def create_new_code():
    flag = True
    data = request.get_json()
    icd_code_type = data['icd_type'].strip().upper()
    icd_full_code = data['full_icd_code'].strip().upper()
    record = build_records[icd_code_type]
    validate_build_record = validator.valid_code_length(icd_full_code, record['min_num'], record['max_num'])
    icd_type_id = record['id']

    if not validator.is_empty_field(data['full_icd_code']):
        flag = False
        return jsonify({"status": "error", "message": " Full ICD-10 code is required", "status_error": "401"}), 401

    if not validate_build_record:
        flag = False
        message = f'{icd_code_type} Character length required should not be less than 3 or more the 7'
        return jsonify({"status": "error", "message": message, "status_code": "401"}), 401

    if generate_code.is_icd_exists(icd_full_code)[0] > 0:
        flag = False
        return jsonify({"status": "error", "message": "Full ICD code already exists", "status_code": "401"}), 401

    if flag:
        create = generate_code.create_icd_code(data['category_code'],
                                               data['diagnosis_code'],
                                               data['full_icd_code'],
                                               data['abbreviated_description'],
                                               data['full_description'],
                                               data['category_title'],
                                               icd_type_id)
        if create:
            return jsonify({"status": "success", "message": "New ICD code has been created successfully ",
                            "status_code": "201"}), 201
        else:
            return jsonify({"status": "error", "message": "New ICD code creation operation failed"}), 401
    pass


@app.route("/api/v1/update/<int:id>", methods=['PUT'])
def update_code(id):
    if request.is_json:
        flag = True
        data = request.get_json()
        icd_code_type = data['icd_type'].strip().upper()
        icd_full_code = data['full_icd_code'].strip().upper()
        record = build_records[icd_code_type]
        validate_build_record = validator.valid_code_length(icd_full_code, record['min_num'], record['max_num'])
        icd_type_id = record['id']

        if not validator.is_empty_field(data['full_icd_code']):
            flag = False
            return jsonify({"status": "error", "message": " Full ICD-10 code is required", "status_error": "401"}), 401

        if not validate_build_record:
            flag = False
            message = f'{icd_code_type} Character length required should not be less than 3 or more the 7'
            return jsonify({"status": "error", "message": message, "status_code": "401"}), 401

        if flag:
            update = generate_code.update_all_codes(data['category_code'], data['diagnosis_code'],
                                                    data['full_icd_code'],
                                                    data['abbreviated_description'],
                                                    data['full_description'], data['category_title'], data['icd_type'],
                                                    id)
        if update > 0:
            return jsonify({"status": "success", "message": "Record updated", 'status_code': "200"}), 200
        else:
            return jsonify({"status": "failed", "message": "Update failed", "status_code": "401"}), 401
    pass


@app.route("/api/v1/delete/<int:id>", methods=['DELETE'])
def delete_code(id):
    if id < 1:
        return jsonify({"status": "error", "message": "Code ID is required", "status_code": "401"}), 401
    else:

        if generate_code.code_exist(id)[0] > 0:

            delete = generate_code.delete_icd_code(id)

            if delete:
                return jsonify({"status": "success", "message": "Code has been Deleted", "status_code": "200"}), 200
            else:
                return jsonify({"status": "failed", "message": "Delete failed", "status_code": "401"}), 401
        else:
            return jsonify({"status": "failed", "message": "Record does not exist", "status_code": "401"}), 401


@app.route("/api/v1/list", methods=['GET'])
def list_codes():
    start = request.args.get("start")
    get_limit = request.args.get("limit")
    max_limit = 2

    int_start = None

    if start is None and get_limit is None:
        int_start = 0
    else:
        int_start = int(start)
        int_limit = int(get_limit)

    total = generate_code.count_all_record()[0]
    numberOfPages = (int(math.ceil(total) / max_limit))

    meta_data = {"count": total,
                 "limit": 20,
                 "page_size": numberOfPages,
                 "base_url": "http://127.0.0.1:5000",
                 "next": f'/api/v1/list?start=1&limit={max_limit}'
                 }

    offset_start = ((int_start + 1) - 1) * max_limit

    list_data = generate_code.list_all_codes(offset_start, max_limit)
    format_data = generate_code.process_all_records(list_data)

    return jsonify({"meta": meta_data, "start": offset_start,
                    "number_per_page": numberOfPages,
                    "data": format_data})

    pass


@app.route("/api/v1/list/<int:id>", methods=['GET'])
def list_code_byid(id):
    if id < 1:
        return jsonify({"status": "error", "message": "Valid code ID is required", "status": "401"}), 401

    else:
        fetch_one = generate_code.fetch_one_record(id)

        if len(fetch_one) > 0:

            data = {"category_code": fetch_one[0], "diagnosis_code": fetch_one[1],
                    "full_icd_code": fetch_one[2], "abbreviated_description": fetch_one[3],
                    "full_description": fetch_one[4],
                    "category_title": fetch_one[5],
                    "icd_type": fetch_one[6]
                    }

            return jsonify({"status": "success", "data": data, "status_code": "200","count":fetch_one[8]}), 200
        else:
            return jsonify({"status": "empty", "data": {}, "status_code": "403"}), 403
    pass

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')