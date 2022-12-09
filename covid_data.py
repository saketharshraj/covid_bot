import pymongo


def new_patient(data):
    patient = {}
    last_id = [x for x in status.find().sort([('_id', -1)])][0]['ctfid']  # to get last ctfid inserted
    patient['ctfid'] = last_id + 1
    status.insert_one({'ctfid': patient['ctfid'], 'status': 'Unassigned'})
    data[1] = data[1].upper()
    for i in range(1, len(data)):
        patient[info[i]] = data[i]
    # patient['by'] = acov.give_update()['message']['from']['first_name']
    patients.insert_one(patient)
    return 'New Patient Added Successfully'


def patients_info(command):
    response = ""
    if len(command) == 1:
        for record in patients.find():
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

    else:
        command.pop(0)
        if command[0] == 'and' or command[0] == 'or':
            cond = '$' + command.pop(0)
        else:
            cond = '$and'
        filters = []
        for constraint in command:
            colon_index = constraint.find(':')
            key = constraint[0:colon_index].strip()
            # key = key[0].upper() + key[1:]
            value = constraint[colon_index + 1:].strip()
            if key == 'ctfid':
                value = int(value)
            filters.append({key: value})
            print(filters)

        for record in patients.find({cond: filters}):
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

    return response


def getinfo(command):
    response = ""
    if len(command) == 1:
        for record in done.find():
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

        for record in patients.find():
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

    else:
        command.pop(0)
        if command[0] == 'and' or command[0] == 'or':
            cond = '$' + command.pop(0)
        else:
            cond = '$and'
        filters = []
        for constraint in command:
            colon_index = constraint.find(':')
            key = constraint[0:colon_index].strip()
            # key = key[0].upper() + key[1:]
            value = constraint[colon_index + 1:].strip()
            if key == 'ctfid':
                value = int(value)
            filters.append({key: value})
            print(filters)

        for record in done.find({cond: filters}):
            print(filters)
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

        for record in patients.find({cond: filters}):
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'

    return response


def update_status(command):
    command.pop(0)
    status.update(
        {'ctfid': int(command[0])},
        {"$set": {
            'status': command[1]},
            "$currentDate": {"lastModified": True}
         }
    )
    return "Updated Successfully"


def remove_done():
    for stat in status.find():
        if stat['status'].lower() == 'done':
            done_id = stat['ctfid']
            for record in patients.find({'ctfid': done_id}):
                record.pop('_id')
                done.insert_one(record)
                patients.delete_one({'ctfid': done_id})
    return "List Refreshed"


def getstatus(command):
    response = ''
    if len(command) > 1:
        command.pop(0)
        for ctfid in command:
            for record in status.find({'ctfid': int(ctfid)}):
                record.pop('_id')
                for s in record:
                    response = response + s + ' : ' + str(record[s]) + '\n'
                response += '\n'

    else:
        for record in status.find():
            record.pop('_id')
            for s in record:
                response = response + s + ' : ' + str(record[s]) + '\n'
            response += '\n'
    return response


info = ['NA', 'name', 'place', 'age', 'spo2', 'requirement', 'hospital', 'attendant', 'contact', 'extra', 'by']
client = pymongo.MongoClient(host='localhost', port=27017)
covid_db = client['Covid']
patients = covid_db.patientinfo
leads = covid_db.leadsinfo
status = covid_db.status
done = covid_db.helped


