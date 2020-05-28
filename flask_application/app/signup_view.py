from app import app, request, mysql, escape_string, bcrypt, jsonify, render_template, re



@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.json.get('name', None)
        if not re.match('[A-Za-z]*$', name):
            return jsonify({"msg": "Your name can only contain literals"}), 401
        else:
            user_name = name

        email = request.json.get('email', None)
        if not re.match('^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$',
                        email):
            return jsonify({"msg": "Please, enter a valid email"}), 401
        else:
            user_email = email

        password = request.json.get('password', None)

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!?:@#$*%^&_+.])[A-Za-z\d!?:@#$*%^&_+.]{8,20}$",password):
            return jsonify({"msg": "Please, enter a valid password"}), 401
        else:
            user_password = password

        confirm = request.json.get('confirm', None)

        cur = mysql.connection.cursor()

        if user_password == confirm:
            query_email = "SELECT EXISTS(SELECT email FROM user WHERE email = '%(email)s') " % {"email": user_email}
            cur.execute(query_email)
            check_email = cur.fetchone()

            if check_email[0] == 0:
                secure_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')

                query_insert = ("""INSERT INTO user(name, email, password)
                                VALUES ('%(name)s', '%(email)s', '%(password)s')""" %
                                {"email": user_email, "name": user_name, "password": secure_password})

                cur.execute(query_insert)
                mysql.connection.commit()

                return jsonify({'signup': True})

            else:
                return jsonify({"msg": "This e-mail is already in use"}), 401
        else:
            return jsonify({"msg": "Passwords do not match"}), 401

    return render_template('signup.html')
