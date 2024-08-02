import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger.listeners import ConsoleLogger, FileLogger
from src.logger.logger import Logger

class TestConsoleLogger(unittest.TestCase):
    @patch('builtins.print')
    def test_console_logger_update(self, mock_print):
        console_logger = ConsoleLogger()
        test_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        console_logger.update(test_date, 'test_source', 'INFO', 'test_message')
        self.assertTrue(mock_print.called)

class TestFileLogger(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_file_logger_update(self, mock_open):
        file_logger = FileLogger()
        test_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file_logger.update(test_date, 'test_source', 'INFO', 'test_message')
        mock_open.assert_called_with('app.log', 'a')
        mock_open().write.assert_called_once_with(f"{test_date} - INFO - test_source - test_message\n")

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()
        self.console_logger = ConsoleLogger()
        self.file_logger = FileLogger()
        self.logger.register_listener(self.console_logger)
        self.logger.register_listener(self.file_logger)

    def test_register_listener(self):
        self.assertIn(self.console_logger, self.logger.listeners)
        self.assertIn(self.file_logger, self.logger.listeners)

    def test_remove_listener(self):
        self.logger.remove_listener(self.console_logger)
        self.assertNotIn(self.console_logger, self.logger.listeners)

    @patch.object(ConsoleLogger, 'update')
    @patch.object(FileLogger, 'update')
    def test_notify_listeners(self, mock_file_update, mock_console_update):
        self.logger.activity('test_source', 'INFO', 'test_message')
        self.assertTrue(mock_console_update.called)
        self.assertTrue(mock_file_update.called)

if __name__ == '__main__':
    unittest.main()
