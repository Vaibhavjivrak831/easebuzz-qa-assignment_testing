def test_form_interaction(page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.check("input[value='radio2']")
    page.select_option("#dropdown-class-example", "option2")
    page.check("#checkBoxOption1")
    page.fill("#name", "Test User")

    page.click("#alertbtn")
    page.on("dialog", lambda dialog: dialog.accept())

    assert "Practice Page" in page.title()
