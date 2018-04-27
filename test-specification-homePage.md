
# Circles.Life Testing TOC
<!-- TOC -->

- [Circles.Life Testing TOC](#circleslife-testing-toc)
- [Test strategies](#test-strategies)
    - [Menu bar should exist and functional](#menu-bar-should-exist-and-functional)
        - [Test scenario](#test-scenario)
        - [Teardown each steps Menu bar](#teardown-each-steps-menu-bar)
        - [All users - Menu bar](#all-users---menu-bar)
            - [Pre-Condition for all users - Menu bar](#pre-condition-for-all-users---menu-bar)
            - [STEPS for all users - Menu bar](#steps-for-all-users---menu-bar)
        - [Unautorized user - Menu bar](#unautorized-user---menu-bar)
            - [Pre-Condition for Unautorized users - Menu bar](#pre-condition-for-unautorized-users---menu-bar)
            - [STEPS for Unautorized users - Menu bar](#steps-for-unautorized-users---menu-bar)
        - [Authorized user - Menu bar](#authorized-user---menu-bar)
            - [Pre-Condition for Authorized users - Menu bar](#pre-condition-for-authorized-users---menu-bar)
            - [STEPS for Authorized users - Menu bar](#steps-for-authorized-users---menu-bar)
    - [Footer should exist and functional](#footer-should-exist-and-functional)
        - [Test scenario](#test-scenario)
        - [Teardown each step Footer](#teardown-each-step-footer)
        - [All users - Footer](#all-users---footer)
        - [Pre-Condition for All users - Footer](#pre-condition-for-all-users---footer)
        - [STEPS for All users - Footer](#steps-for-all-users---footer)
        - [Unautorized user - Footer](#unautorized-user---footer)
            - [Pre-Condition for Unautorized users - Footer](#pre-condition-for-unautorized-users---footer)
            - [STEPS for Unautorized users - Footer](#steps-for-unautorized-users---footer)
        - [Authorized user - Footer](#authorized-user---footer)
            - [Pre-Condition for Authorized users - Footer](#pre-condition-for-authorized-users---footer)
            - [STEPS for Autorized users - Footer](#steps-for-autorized-users---footer)
    - [pages.circles.life](#pagescircleslife)
        - [Test scenario](#test-scenario)
        - [Teardown each steps pages.circles.life](#teardown-each-steps-pagescircleslife)
        - [Menu bar in pages.circles.life](#menu-bar-in-pagescircleslife)
        - [Footer in pages.circles.life](#footer-in-pagescircleslife)
        - [All User - pages.circles.life](#all-user---pagescircleslife)
            - [Pre-Condition for all users -page body of pages.circles.life](#pre-condition-for-all-users--page-body-of-pagescircleslife)
            - [STEPS for all users - page body of pages.circles.life](#steps-for-all-users---page-body-of-pagescircleslife)
        - [Unauthorized user - page body of pages.circles.life](#unauthorized-user---page-body-of-pagescircleslife)
            - [Pre-Condition for unautorized users - page body of pages.circles.life](#pre-condition-for-unautorized-users---page-body-of-pagescircleslife)
            - [STEPS for unautorized users - page body of pages.circles.life](#steps-for-unautorized-users---page-body-of-pagescircleslife)
        - [Authorized user - page body of pages.circles.life](#authorized-user---page-body-of-pagescircleslife)
            - [Pre-Condition for autorized users - page body of pages.circles.life](#pre-condition-for-autorized-users---page-body-of-pagescircleslife)
            - [STEPS for Autorized users - page body of pages.circles.life](#steps-for-autorized-users---page-body-of-pagescircleslife)

<!-- /TOC -->
# Test strategies
The test strategies here are in desktop version only at the size more than 1024 pixel width.
Currently, It focuses on the Home page only.
## Menu bar should exist and functional
### Test scenario
All Users can visit desktop version webpage circles.life and be able to access the links they can see.

### Teardown each steps Menu bar
action | expected result
--- | ---
go back to the landing page | The landing page is loaded successfully.

### All users - Menu bar
#### Pre-Condition for all users - Menu bar
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

#### STEPS for all users - Menu bar
action | expected result
--- | ---
User clicks **CIRCLES.LIFE** logo | Home page loaded.
User clicks **Plan Only** menu | No-Contact Plan page loaded.
User clicks **Plan with phone** menu | No-Contact Plan with phone page loaded.
User clicks **Roaming** menu | Roaming page loaded.
User clicks **Porting** menu | Porting page loaded.
User clicks **Why us** menu | About Us page loaded.
User clicks **Help** menu | Help page loaded.
User clicks **Buy** button | Login page loaded.
User clicks **Sign up** button | Sign up page loaded.

### Unautorized user - Menu bar
#### Pre-Condition for Unautorized users - Menu bar
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User has no session in web browser | Calling Log in page is loaded successfully
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

#### STEPS for Unautorized users - Menu bar
action | expected result
--- | ---
User clicks **Buy** button | Login page loaded.
User clicks **Sign up** button | Sign up page loaded.

### Authorized user - Menu bar
#### Pre-Condition for Authorized users - Menu bar
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User logged in to circles.life website | Calling Log in page is redirected to user account page.
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

#### STEPS for Authorized users - Menu bar
action | expected result
--- | ---
User clicks **Buy** button | Login page loaded.
User clicks **Sign up** button | Sign up page loaded.

## Footer should exist and functional
### Test scenario
All user can visit desktop version webpage pages.circles.life and be able to access the page body information and the the link they can see.

### Teardown each step Footer
action | expected result
--- | ---
go back to the landing page | The landing page is loaded successfully.

### All users - Footer
### Pre-Condition for All users - Footer
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

### STEPS for All users - Footer
action | expected result
--- | ---
User see the footer in grid format | Footer section and links displayed in grid format
User see **Explore** section | Explore section is displayed with separate line of 5 links are clickable **Login** , **CirclesCare App** , **Roadshows** , **Partnerships** , **Bonus Data**
User clicks **Login** under Explore section | **Login** page is loaded successfully
User clicks **CirclesCare App** under Explore section | **CirclesCare App** page is loaded successfully
User clicks **Roadshows** under Explore section | **Roadshows** page is loaded successfully
User clicks **Partnerships** under Explore section | **Partnerships** page is loaded successfully
User clicks **Bonus Data** under Explore section | **Bonus Data** page is loaded successfully
User see **Company** section | Company section is displayed with separate line of 5 links are clickable **About Us** , **Careers** , **CIS Corporate Discounts** , **Terms and Conditions** , **Privacy**
User clicks **About Us** under Explore section | **About Us** page is loaded successfully
User clicks **Careers** under Explore section | **Careers** page is loaded successfully
User clicks **CIS Corporate Discounts** under Explore section | **Corporate** page is loaded successfully
User clicks **Terms and Conditions** under Explore section | **Term** page is loaded successfully
User clicks **Privacy** under Explore section | **Privacy** page is loaded successfully
User see **Help** section | Help section is displayed with separate line of 5 links are clickable **Contact Us** , **Track My Order** , **Billing** , **Lost SIM** , **FAQ**
User clicks **Contact Us** under Explore section | **Help** page is loaded successfully and Jump to **contact us** section
User clicks **Billing** under Explore section | **Billing** page is loaded successfully
User clicks **FAQ** under Explore section | **FAQ** page is loaded successfully

### Unautorized user - Footer
#### Pre-Condition for Unautorized users - Footer
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User has no session in web browser | Calling Log in page is loaded successfully
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

#### STEPS for Unautorized users - Footer
User clicks **Track My Order** under Explore section | **Login** page is loaded successfully
User clicks **Lost SIM** under Explore section | **Login** page is loaded successfully

### Authorized user - Footer
#### Pre-Condition for Authorized users - Footer
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User logged in to circles.life website | Calling Log in page is redirected to user account page.
User is on the landing page *the page to be tested* | The landing page is loaded successfully.

#### STEPS for Autorized users - Footer
User clicks **Lost SIM** under Explore section | **Lost SIM** page is loaded successfully
User clicks **Track My Order** under Explore section | **My Order** page is loaded successfully

## pages.circles.life
### Test scenario
All users can visit desktop version webpage pages.circles.life and be able to access the links they can see.

### Teardown each steps pages.circles.life
action | expected result
--- | ---
go back to the pages.circles.life | The pages.circles.life is loaded successfully

### Menu bar in pages.circles.life
[Menu bar should exist and functional](#menu-bar-should-exist-and-functional)

### Footer in pages.circles.life
[Footer should exist and functional](#footer-should-exist-and-functional)

### All User - pages.circles.life
#### Pre-Condition for all users -page body of pages.circles.life
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User is on the pages.circles.life | The pages.circles.life is loaded successfully

#### STEPS for all users - page body of pages.circles.life
action | expected result
--- | ---
User clicks **28$/Month** picture at The Best No-Contract Mobile Plan ads | No-Contract-plan page is loaded successfully
User clicks **$3/day** picture at The Best No-Contract Mobile Plan ads | 3-unlimited-data page is loaded successfully
User clicks **More about best plan** at The Best No-Contract Mobile Plan ads | No-Contract-plan page is loaded successfully
User clicks **More on Unlimited Data on Demand** at The Best No-Contract Mobile Plan ads | 3-unlimited-data page is loaded successfully
User clicks **Term and conditions apply** at The Best No-Contract Mobile Plan ads | CIRCLES.LIFE MOBILE TERMS & CONDITIONS page is loaded successfully
User see the warnging text | *Unlimited WhatsApp does not include video calling. Voice calling is capped at 10,000 minutes per month.* is displayed in The Best No-Contract Mobile Plan ads
User sees **How it works** | gif image loopback graphic shows how it works.
User see **Network coverage** picture | The percentage picture for network coverage is displayed.
User clicks **source link of network coverage report** | It brings user to correct website that provide network coverage report.
User see **Stuck in contract** picture | The picture of stuck in contract 2 years is displayed.
User clicks **Set Reminders** button | The reminder setup page is loaded successfully.
User clicks to the circles.life story links | It brings user to correct website.
User see Why circles.life | It shows 4 pictures and links of **Never run out of data** , **Easy to join** ,**No contracts ever again** , **you're in control**.
User clicks the **20 GB for $20** link or the picture above it | The page **campaign 20-plus** is loaded successfully.
User clicks the **Transfer your number** link or the picture above it | The page **porting** is loaded successfully.
User clicks the **Bonus Data** link or the picture above it | The page **Bonus Data** is loaded successfully.
User clicks the **CirclesCare** link or the picture above it | The page **circle care** is loaded successfully.

### Unauthorized user - page body of pages.circles.life
#### Pre-Condition for unautorized users - page body of pages.circles.life
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User has no session in web browser | Calling Log in page is loaded successfully
User is on the pages.circles.life | The pages.circles.life is loaded successfully

#### STEPS for unautorized users - page body of pages.circles.life
action | expected result
--- | ---
User clicks **Buy now** at 8GB ads | Signup page is loaded successfully
User clicks **Get it now** | **Sign up** page is loaded successfully.

### Authorized user - page body of pages.circles.life
#### Pre-Condition for autorized users - page body of pages.circles.life
action | expected result
--- | ---
Open web browser to 1280x960 | The web browser is open up with 1280x960 pixel.
User logged in to circles.life website | Calling Log in page is redirected to user account page.
User is on the pages.circles.life | The pages.circles.life is loaded successfully

#### STEPS for Autorized users - page body of pages.circles.life
action | expected result
--- | ---
User clicks **Buy now** at 8GB ads | **Plan** page is loaded successfully
User clicks **Get it now** | **Plan** page is loaded successfully
