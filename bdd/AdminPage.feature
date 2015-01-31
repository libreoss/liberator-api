Feature: Liberator Superadmin Homepage
In order to access Liberator main features
I want to see a homepage that has
A link to the page that lists all articles
A link to to the page that creates a new article

Background:
  Given that Liberator is running
  And the homepage is at http://localhost:8000
  And no access privileges are implemented
  
Scenario: User opens /
  Given I load the homepage 
  Then I should see the links "Show all articles" and "Create an article"

Scenario Outline: Homepage links
  Given I am on the homepage
  When I click on <link> shown on the page
  Then I should see <page> or content loading.
  
  Examples:
  | link              | page               |
  | Show all articles | article_show_all   |
  | Create an article | article_create_new |