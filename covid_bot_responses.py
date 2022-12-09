from datetime import datetime
import covid_data as cd


def replies(command, update):
    command = str(command).lower().lstrip().split("\n")

    if command[0][0] == "/":
        command[0] = command[0][1:]

    # if "update@anti_covidbot" in command:
    #     command = command[0:-9]

    if command[0] in ('hello', 'hii', 'hi'):
        return "Hey ! How's its going ?"

    if command[0] == 'fine':
        return 'Great !! Keep it up.'

    if command[0] in ('time', 'time?'):
        now = datetime.now()
        tm = now.strftime("%H:%M:%S")
        return str(tm)

    if command[0] in 'date':
        now = datetime.now()
        tm = now.strftime("%d/%m/%y")
        return str(tm)

    if command[0] in ('who are you ?', 'who are you?', 'who are you', 'myinfo'):
        return "I am an Anti-Covid bot. I am here to make the Covid Task Force work easy."

    if command[0] in 'format':
        return "Name\nPlace\nAge\nspo2\nrequirement\nhospital\nattendant\ncontact\nAlternate Contact\nextra\n\nWrite 'NA' if " \
               "you don't " \
               "have " \
               "the information "

    if command[0] in ('new', 'insert'):
        response = cd.new_patient(command)
        return response

    if command[0] == 'leads':
        return 'No leads at this moment'

    if command[0] in ('update', 'updateinfo'):
        return cd.update_status(command)

    if command[0] in ('remove', 'refresh'):
        return cd.remove_done()

    if command[0] in ('getstatus', 'status'):
        return cd.getstatus(command)

    if 'getinfo' in command[0]:
        response = cd.getinfo(command)
        return response

    if command[0] in ('patients', 'patient', 'patientlist'):
        return cd.patients_info(command)
