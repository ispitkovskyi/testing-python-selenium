Feature: Test navigation between page
  blabla bla
  bla bla

  Scenario: Homepage can go to the Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page

  Scenario: Homepage can go to the Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage