import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'stripe_auto_fulfillment.py'
spec = importlib.util.spec_from_file_location('stripe_auto_fulfillment', MODULE_PATH)
stripe_auto_fulfillment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stripe_auto_fulfillment)


class StripeAutoFulfillmentTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)
        self.template = self.root / 'welcome.txt'
        self.template.write_text('Hi {{customer_name}}\nDownload: example')
        self.product_map = {
            'plink_test_123': {
                'slug': 'gr2-ess2-unit1-bundle',
                'draftSubject': 'Your bundle is ready',
                'emailTemplatePath': self.template.relative_to(self.root).as_posix(),
                'downloadUrl': 'https://littlelabcoats.co/gr2-ess2-unit1-download.html',
            }
        }
        self.event = {
            'id': 'evt_test_123',
            'data': {
                'object': {
                    'id': 'cs_test_123',
                    'livemode': True,
                    'payment_status': 'paid',
                    'payment_link': 'plink_test_123',
                    'customer_details': {
                        'email': 'parent@example.com',
                        'name': 'Test Parent',
                    },
                }
            },
        }

    def tearDown(self):
        self.tmpdir.cleanup()

    def _run_process_events(self, log, dry_run=False, replay_session_ids=None):
        with patch.object(stripe_auto_fulfillment, 'ROOT', self.root), \
             patch.object(stripe_auto_fulfillment, 'stripe_request', return_value={'data': [self.event]}), \
             patch.object(stripe_auto_fulfillment, 'send_email', return_value={'sent': True}) as send_email, \
             patch.object(stripe_auto_fulfillment.time, 'time', return_value=1234567890):
            sent, skipped = stripe_auto_fulfillment.process_events(
                'sk_test',
                self.product_map,
                log,
                dry_run=dry_run,
                replay_session_ids=replay_session_ids,
            )
        return sent, skipped, send_email

    def test_dry_run_does_not_mutate_log_or_mark_session_processed(self):
        log = {'processedSessions': {}, 'lastRunAt': None}

        sent, skipped, send_email = self._run_process_events(log, dry_run=True)

        self.assertEqual(len(sent), 1)
        self.assertEqual(skipped, [])
        send_email.assert_called_once()
        self.assertEqual(log, {'processedSessions': {}, 'lastRunAt': None})

    def test_real_run_marks_session_processed_and_sets_last_run(self):
        log = {'processedSessions': {}, 'lastRunAt': None}

        sent, skipped, send_email = self._run_process_events(log, dry_run=False)

        self.assertEqual(len(sent), 1)
        self.assertEqual(skipped, [])
        send_email.assert_called_once()
        self.assertIn('cs_test_123', log['processedSessions'])
        self.assertEqual(log['processedSessions']['cs_test_123']['eventId'], 'evt_test_123')
        self.assertEqual(log['lastRunAt'], 1234567890)

    def test_real_run_after_dry_run_still_sends_order(self):
        log = {'processedSessions': {}, 'lastRunAt': None}

        first_sent, _, _ = self._run_process_events(log, dry_run=True)
        second_sent, second_skipped, second_send_email = self._run_process_events(log, dry_run=False)

        self.assertEqual(len(first_sent), 1)
        self.assertEqual(len(second_sent), 1)
        self.assertEqual(second_skipped, [])
        second_send_email.assert_called_once()
        self.assertIn('cs_test_123', log['processedSessions'])


if __name__ == '__main__':
    unittest.main()
