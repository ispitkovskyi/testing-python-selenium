Feature: Test navigation between page
  blabla bla
  bla bla

  Scenario: Homepage can go to the Blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page

  Scenario: Homepage can go to the Homepage
    Given I am on the blog page
    When I click on the link with id "home-link"
    Then I am on the homepage