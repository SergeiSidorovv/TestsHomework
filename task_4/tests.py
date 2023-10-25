from unittest import TestCase, main
from unittest.mock import patch, Mock, MagicMock

from book_repository import BookRepository


class TestBook(TestCase):
    @patch.object(BookRepository, 'get_all_data')
    def test_get_all_data(self, get_all_data_mock):
        get_all_data_mock = MagicMock()
        get_all_data_mock.return_value = ['name', 'author', 1999]

        self.assertEqual(['name', 'author', 1999],
                         get_all_data_mock.return_value)


if __name__ == '__main__':
    main()
