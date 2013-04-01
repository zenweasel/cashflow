Feature: Input Expenses and Income
    In order to track my finances
    as an individual
    I want to input my expenses and income

    Scenario: Input 3 entries
        Given I have input the 3 entries in the database
        | name              | incurred_date     | amount    | category
        | Yummy.com         | 03/30/2013        | 70.23     | Groceries
        | iTunes            | 03/30/2013        | 9.99      | Subscription Services
        | So. Cal. Edison   | 03/31/2013        | 85.51     | Utilities
        When I view the list of Entries
        I see 3 entries

