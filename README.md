# Tietokantasovellus / Database application (period 1, fall 2021)

## Status

I started planning this application on 10 Sep 2021 and the final delivery date is on 24 October 2021. There are two intermediate releases before the final
delivery date.

The current status is that I have now delivered the first intermediate release to this GitHub site on 26 September 2021. The application currently includes three data tables and seven webpages. Few of the planned key functionalities have been completed. No CSS formatting has been done yet. A lot of my time has gone to trying to get the database connection to work.

## Subject of the Project

The application is a web-based application that uses PostreSQL database and Python Flask library. The application should contain 5-10 tables.

The purpose of this application is to support a company in product improvement by having related information available in the application and also to provide a platform for users to share their ideas for Product improvement.

## Key Functions of the Application
One role to start with: normal user

1. A user can create a new username and password. DONE
1. A user can login and logout. DONE
1. A user sees a list of Products after login (+ since when or until when the Product has been part of the company's selection). DONE
1. A user can add a new Product or remove and existing Product from the list.
1. A user can insert an idea for Product improvement (date and user information collected). PARTLY DONE
1. A user (administrator, if exists) can add a new project to a Product improvement project list specifying the Product, related improvement idea, project team and project start & target end dates.
1. A user can view a list of all the company's employees and add them to a project team.
1. A user can view a list of all the project teams.
1. A user (administraton, if exists) can mark a project as completed and see a list of completed projects.

Potential additional functions
* two user roles: administrator, normal user
* administrator can select some of the ideas for improvement to a short list

## Testing of the application in Heroku

The application is available in Heroku through [this link](https://tikaso-app.herokuapp.com/). Please create a username and password to access the contents of the application. 

## Other
