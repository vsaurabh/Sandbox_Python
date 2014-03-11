from bottle import route, run, template, get, post, put, request, delete
p_dict={}

@post('/patient') #@route('/add_patient', method='POST')
def add_patient():

    '''Function For Adding a new Patient'''

    #import pdb
    #pdb.set_trace()
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    pa_phone = request.POST['phone']
    store_info = [p_name,p_gender,p_age,p_address,pa_phone]
    p_dict.update({p_id:store_info})
    return p_dict

@get('/patient/<id>')
def show_patient(id):

    '''Function For Showing a Patient with his ID'''

    #import pdb
    #pdb.set_trace()
    return p_dict[id]
    
@put('/patient/<id>')
def update_patient(id):

    '''Function For Updating a Patient with his ID'''

    #import pdb
    #pdb.set_trace()
    if id in p_dict.keys():
        p_name = request.POST['name']
        p_gender = request.POST['gender']
        p_age = request.POST['age']
        p_address = request.POST['address']
        pa_phone = request.POST['phone']
        update_info = [p_name,p_gender,p_age,p_address,pa_phone]
        p_dict[id]=update_info
        return p_dict
    else:
        return 'Patient With id=>' + str(id) + ' is not found'

@delete('/patient/<id>')
def delete_patient(id):

    '''Function For Deleting a Patient with his ID'''

    if id in p_dict.keys():
        deleted_patient = p_dict.pop(id)
        return "Patient with id " + str(id) + ' and info ' + str(deleted_patient) + ' is deleted '

    else:
        return 'Patient With id=>' + str(id) + ' is not found'
            

run(host='localhost',port=8080)