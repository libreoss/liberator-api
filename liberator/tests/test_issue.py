import liberator.models
from . import TestCase
import liberator.factories

#
# class TestIssue(TestCase):
#     def setUp(self):
#         super(TestIssue, self).setUp()
#         self.language = liberator.factories.LanguageFactory()
#         self.language.save()
#
#     def test_create_issue(self):
#         issue = liberator.factories.IssueFactory()
#         issue.save()
#         issue_title = liberator.factories.IssueTitleFactory(
#             issue=issue,
#             language=self.language
#         )
#         issue_title.save()
#         url = '/api/v1/issues/{0}/'.format(issue.pk)
#         issue_api = self.client.get(url, **self.args)
#         self.assertEqual(issue.pk, issue_api.data['id'])
#         title = issue.titles.get(pk=issue_title.pk)
#         title_api = issue_api.data['titles'][0]
#         self.assertEqual(title.title, title_api['title'])
#         self.assertEqual(title.language.pk, title_api['language'])
