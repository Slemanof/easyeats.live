from app import (app, request, escape_string, mysql, jsonify, bcrypt, re,
                 create_access_token, set_access_cookies, unset_jwt_cookies, render_template)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.json.get('email', None)
        if not re.match('^[A-Za-z0-9@.]*$', email):
            return jsonify({"msg": "Please, enter a valid email"}), 401
        else:
            user_email = email

        password = request.json.get('password', None)

        cur = mysql.connection.cursor()
        check_email = "SELECT EXISTS(SELECT email FROM user WHERE email = '%(email)s') " % {"email": user_email}
        cur.execute(check_email)
        check_email = cur.fetchone()

        if check_email[0] == 0:
            return jsonify({"msg": "Incorrect credentials"}), 401
        else:
            query = "SELECT * FROM user WHERE email = '%(email)s' " % {"email": user_email}
            cur.execute(query)
            data = cur.fetchone()

            if bcrypt.checkpw(password.encode('utf-8'), data[3].encode('utf-8')):
                access_token = create_access_token(identity=data[0])
                resp = jsonify({'login': True})
                set_access_cookies(resp, access_token)
                return resp
            else:
                return jsonify({"msg": "Incorrect credentials"}), 401

    return render_template('login.html')


@app.route('/logout')
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200
