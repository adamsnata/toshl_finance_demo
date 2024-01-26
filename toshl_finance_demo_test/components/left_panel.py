from selene import browser, have


def verify_user(name):
    (browser.element('[ng-bind-html="viewData.titles.userDisplayName"]')
     .with_(timeout=10).should(have.exact_text(name)))
