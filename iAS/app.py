# Copyright 2016 Team - iAS, University Of Peradeniya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __init__ import *

app = Flask(__name__)
api = Api(app)


api.add_resource(Main, '/')

api.add_resource(Applications, '/applications')


api.add_resource(Login, '/login')


@app.route('/callback')
@google.authorized_handler
def authorized(resp):
    session['access_token'] = resp['access_token']
    getUserInfo(session["access_token"])
    session["User"] = json.loads(getUserJson())
    return redirect('/')


@google.tokengetter
def get_access_token():
    return session.get('access_token')

