# Tietokantasovellus / Database application (period 1, fall 2021)

## Status

I started planning this application on 10 Sep 2021 and the final delivery date is on 24 October 2021. There are two intermediate releases before the final
delivery date.

The current status is that I have now delivered the third intermediate release to this GitHub site on 8 October 2021. The application includes seven data tables, which include all the needed information. The planned key functionalities have been completed. CSS formatting has been initiated and will be completed before the final release.

Please note that I by mistake named the commits as for the 2nd release, but those are for this 3rd release.

## Subject of the Project

The application is a web-based application that uses PostreSQL database and Python Flask library. The application should contain 5-10 tables.

The purpose of my application is to support a company in product improvement by providing a platform for users to share their ideas for product improvement and by having related information available in the application.

## Key Functions of the Application
One role: normal user

1. A user can create a new username and password. DONE
1. A user can login and logout. DONE
1. A user sees a list of Products after login (+ since when or until when the Product has been part of the company's selection). DONE
1. A user can insert an idea for Product improvement (date and user information collected). DONE
1. A user can view a list of the raised ideas.
1. A user can add a new project to a Product improvement project list by specifying the related improvement idea, project team and project start & target end dates. DONE
1. A user can view a list of all the company's employees and add them to a project team. DONE
1. A user can view a list of the projects. DONE

Potential additional functions
* two user roles: administrator, normal user
* A user can view a list of all the project teams.
* A user can mark a project as completed and see a list of completed projects.
* Search page where a user can look for info based on various parameters.

## Testing of the application in Heroku

The application is available in Heroku through [this link](https://tikaso-app.herokuapp.com/). Please create a username and password to access the contents of the application. 

## Other
