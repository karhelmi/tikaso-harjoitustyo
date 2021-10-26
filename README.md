# Tietokantasovellus / Database application (period 1, fall 2021)

## Status

I started planning this application on 10 Sep 2021 and have now delivered the final version. There were two intermediate releases before the final
delivery date.

## Subject of the Project

The application is a web-based application that uses PostreSQL database and Python Flask library. The application contains seven (7) data tables.

The purpose of my application is to support an entity in product improvement by providing a platform for product users to share their ideas for product improvement, initiate product improvement projects based on the raised ideas and monitor all this.

## Key Functions of the Application
One role: normal user

1. A user can create a new username and password.
1. A user can login and logout.
1. A user view a list of Products after login (+ since when or until when the Product has been part of the company's selection).
1. A user can insert an idea for Product improvement (date and user information collected).
1. A user can view a list of the raised ideas (all and by product).
1. A user can add a new project to a Product improvement project list by specifying the related improvement idea, project team and team members.
1. A user can view a list of all the company's employees and add them to a project team.
1. A user can view a list of the projects.
1. A user can view a list of the involvement of employees in various projects.
1. A user can view the team members of a team.


Potential additional functions for later development
* two user roles: administrator, normal user
* A user can mark a project as completed and see a list of completed projects.
* Search page where a user can look for info based on various parameters.

## Testing of the application in Heroku

The application is available in Heroku through [this link](https://tikaso-app.herokuapp.com/). Please create a username and password to access the contents of the application.
