Feature: A page to submit a new articles
In order to create a new article
I want to have a page that has
The basic fields and a submit button

Background:
  Given that Liberator is running
  And the homepage is at http://localhost:8000
  And no access privileges are implemented
  
Scenario: User opens /newarticle
  Given I load the page for new article submission
  Then I should see the info "Submit a new article"
  And I should see current time and date
  And I should see "Article title" field
  And I should see "Article subtitle" field
  And I should see "Article author ID" field
  And I should see "Article body" field
  And I should see "Article script" selection with "Cyrillic" and "Latin"
  And I should see "Article subtitle" field
  And I should see "Submit" button
  
Scenario: User clicks on "Submit"
  Given I load the page and fill in some of the fields
  When I click on "Submit" button
  Then I should see a message "The data is to be checked and saved" 