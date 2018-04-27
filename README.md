# The circles life automation testing examination
This project is base on the assignment.
1. Go to Our Website, Circles.Life and list down your observations.
2. Write test scenarios for the same website.
3. Write a detailed test case for the same website.
4. Write the script for, Login in to website. Verify your email address under My account.
5. Write a script to login into Facebook account (test account) from website. And Post a test comment.
6. Now, write a script to check the same posted comment by logging into Facebook App. And verify the same comment is posted or not.

For the assignment No.1-3, I did it for only desktop version the home page of the website. It is in [test-specification-homePage.md] at root of this project.
The script for login to website is in src/tests/test.cl.login.py
The script for verify email is in src/tests/test.cl.verifyEmail.py
The script for facebook posting a status is in src/tests/test.fb.py

Not familiar with mobile app testing, just started studying on it yesterday (Appium)

## How to set up env.
1. Match with Windows env because some path (filefox execution file) is in windows format.
2. Install filefox version 59.
3. Install python 2.7.10 or newer
4. pip install -r requirements.txt

## How to run it.
1. at root project path
2. src\tests\test.cl.login.py
3. src\tests\test.cl.verifyEmail.py
4. src\tests\test.fb.py

Test results are in the commandline interface.