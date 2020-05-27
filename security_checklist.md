### Restaurant Recommender Security Checklist 


##### GITHUB
- [ ] Set up a page for security researchers to report vulnerabilities and upcoming threats(ASAP steps can be taken to protect the application and users).
- [x] Never commit secrets or passwords in your code.
- [x] Keep track of the dependencies and libraries used.
- [ ] Prepare a Threat Model that will consider the possible attacks on the web application.

##### OPERATIONS
- [x] Since we are a small team, consider using a Platform as a Service to run the app.
- [x] Use periodically backups to save a copy of the OS or Virtual Enviroment where the web application will run.
- [x] Do not leave the DEBUG mode on. In some frameworks, DEBUG mode can give access or expose critical data in error messages.

##### SANITIZATION OF INPUT
- [ ] All data sources classify into trusted/ untrusted and validate untrusted data (e.g., databases).
- [ ] Specify character set, for all sources of input.(e.g., CP1250, ISO 8859-2).
- [ ] Sanitize all user inputs or any input parameters exposed to user to prevent [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).
- [ ] Always use parameterized queries to prevent [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection).
- [ ] Do not hand code or build JSON by string concatenation. Use your language defined libraries or framework.
- [ ] Sanitize inputs that take some sort of URLs to prevent [SSRF](https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM/edit#heading=h.t4tsk5ixehdd).

##### SANITIZATION OF OUTPUT
- [ ] Manage all data validation on a trusted system(e.g., server).
- [ ] Sanitize Outputs before displaying to users.

##### AUTHENTICATION
- [ ] All authentification must be managed on a trusted system (e.g., server).
- [ ] Password hashing must be managed on a trusted system (e.g., server).
- [ ] Set minimal length of password (e.g., commonly 8 character).
- [ ] Stregthening password policies (e.g., inclusion of one big and small letter, inclusion of one special character, etc.).
- [ ] Password entry when logging in will be obscured.
- [ ] False authentication of the user will not display which part of login data was incorrect - username/password, only display "Invalid Log-In".  
- [x] Use HTTPS.
- [x] Use standard libraries to manage Encryption. For example: store password hashes using Bcrypt.
- [ ] Destroy the session identifier after logout.
- [ ] No open redirects after successful login or in any other intermediate redirects.
- [ ] When parsing Signup/Login input, sanitize for javascript://, data://, CRLF characters.
- [ ] Set secure, httpOnly cookies.

##### USER DATA & AUTHORIZATION
- [ ] `Edit email` feature should be accompanied by a verification email to the owner of the account.
- [ ] Use JWT tokens if possible. Use them if required for your single page app/APIs.

##### SESSION MANAGEMENT
- [ ] Session identifier must be managed on a trusted system (e.g., server).
- [ ] Log-out function will fully terminate the session.
- [ ] Automatic log-out function will log out the user after specific ammount of time(e.g., 30min).
- [x] Do not allow several log-ins with the same username ID, terminate sessions that were made before.

##### SECURITY HEADERS & CONFIGURATIONS
- [ ] Best practices include adding headers such as HSTS, X-Frame-Options, X-Content-Type-Options, etc.
- [ ] `Add` a Content Security Policy.
- [ ] Use random CSRF tokens and expose business logic APIs as HTTP POST requests. Do not expose CSRF tokens over HTTP for example in an initial request upgrade phase.
- [ ] Do not use critical data or tokens in GET request parameters. Exposure of server logs or a machine/stack processing them would expose user data in turn.

##### SYSTEM UPDATES
- [x] Ensure the framework and all other software is running up to date version of the system with all approved patches installed.
- [x] Restrict access to files, folders etc. to the least priviliges as possible.
- [x] Remove all unnecessary files(they might become vulnerability in system). 

##### SYSTEM BACKUP
- [x] The server will have a backup in case of a failure or in case of unknown threats, so it can be rolled back quickly.
