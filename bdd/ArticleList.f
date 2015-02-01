Feature: A page with all articles listed
In order to see and access articles
I want to have a page that lists the
titles of the articles and shows 
the number of all articles

Background:
  Given that Liberator is running
  And the homepage is at http://localhost:8000
  And no access privileges are implemented
  
Scenario: User opens the page with all articles
  Given I load /articles from the homepage
  Then I should see the list with the titles of all articles
  And Next to the each title should be link "Show"
  And Next to the each title should be link "Edit"
  And Next to the each title should be link "Delete"
  And I should see a sentence stating "There are %s articles."

Scenario Outline: Article links
  Given I see the list with all articles
  When I click on <link> next to an article title
  Then I should see the message: "<action> this article?>

  Examples:
  | link   | action |
  | edit   | Edit   |
  | show   | Show   |
  | delete | Delete |