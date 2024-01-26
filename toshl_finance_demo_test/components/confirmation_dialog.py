from selene import browser


def confirm_delete():
    browser.element('.modal-dialog [ng-click^="onDelete"]').click()
