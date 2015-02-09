import unittest

from selenium import webdriver


class ArticleImportWizardTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_get_list_of_articles_on_a_wiki_page(self):
        # Open the /manager URL
        # There's the list articles which are linked to the the page
        # "test_prikupljeni_clanci"
        # Every article has links to cyr and lat pages
        # Every article has the import button
        self.fail("Finish the test!")

    def test_can_start_import_of_article(self):
        # On /manager page you get the list of articles on "test_prikupljeni_clanci"
        # We choose to import the first article
        # Article title and author fields are already filled in with recommendation
        # There's combobox with other recommendations for slug/URL if initial guess is incorrect
        # If there's no page for lat or cyr script, there's a button for creating such page
        # We have wiki slug, URL i article content side by side for cyr and lat.
        # Article content shouldn't be editable
        # If you edit something, and click refetch, it should update current form
        # When youc lick on import, the article is imported in the database

        self.fail("Finish the test!")

    def test_can_mark_unimported_articles(self):
        # Open /manager
        # Choose an article to import
        # Import the article
        # Go back to /manager
        # Make sure that the article is marked as already imported

        self.fail("Finish the test!")
