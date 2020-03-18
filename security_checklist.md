### Restaurant Recommender Security Checklist


##### GITHUB
- [ ] Set up a page for security researchers to report vulnerabilities.
- [ ] Never commit secrets or passwords in your code.
- [ ] Keep track of the dependencies and libraries used. We could quickly check for known vulnerabilities.
- [ ] Prepare a Threat Model that will consider the possible attacks on the web application.

##### OPERATIONS
- [ ] Since we are a small team, consider using a Platform as a Service to run the Restaurant Recommender app.
- [ ] Use periodically backups to save a copy of the OS or Virtual Enviroment where the web application will run.
- [ ] Do not leave the DEBUG mode on. In some frameworks, DEBUG mode can give access or expose critical data in error messages.

##### SANITIZATION OF INPUT
- [ ] `Sanitize` all user inputs or any input parameters exposed to user to prevent [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).
- [ ] Always use parameterized queries to prevent [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection).
- [ ] Do not hand code or build JSON by string concatenation ever, no matter how small the object is. Use your language defined libraries or framework.
- [ ] Sanitize inputs that take some sort of URLs to prevent [SSRF](https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM/edit#heading=h.t4tsk5ixehdd).
- [ ] Sanitize Outputs before displaying to users.

##### AUTHENTICATION
- [ ] Use HTTPS.
- [ ] Use standard libraries to manage Encryption. For example: store password hashes using `Bcrypt`.
- [ ] Destroy the session identifier after `logout`.
- [ ] No open redirects after successful login or in any other intermediate redirects.
- [ ] When parsing Signup/Login input, sanitize for javascript://, data://, CRLF characters.
- [ ] Set secure, httpOnly cookies.


##### USER DATA & AUTHORIZATION
- [ ] `Edit email` feature should be accompanied by a verification email to the owner of the account.
- [ ] For user ids and other ids, use [RFC compliant ](http://www.ietf.org/rfc/rfc4122.txt) `UUID` instead of integers.
- [ ] Use JWT tokens if possible. Use them if required for your single page app/APIs.


##### SECURITY HEADERS & CONFIGURATIONS

- [ ] Best practices include adding headers such as HSTS, X-Frame-Options, X-Content-Type-Options, etc.
- [ ] `Add` a Content Security Policy.
- [ ] Use random CSRF tokens and expose business logic APIs as HTTP POST requests. Do not expose CSRF tokens over HTTP for example in an initial request upgrade phase.
- [ ] Do not use critical data or tokens in GET request parameters. Exposure of server logs or a machine/stack processing them would expose user data in turn.
