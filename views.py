from app import app
import funcs


@app.route('/')
@app.route('/home')
def index():
    return funcs.result()


@app.route('/tree')
def tree():
    # funcs.sorted_list_to_str()
    return funcs.result()
