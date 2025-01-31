import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Я', 'Турецкий гамбит', 'Удивительные приключения Робинзона Крузо'])
    def test_add_new_book_one_book_true(self, name, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_name_false(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_true(self, collector):
        collector.add_new_book('Турецкий гамбит')
        collector.set_book_genre('Турецкий гамбит', 'Детективы')
        assert collector.get_book_genre('Турецкий гамбит') == 'Детективы'

    def test_get_book_genre_true(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_true(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre(self, collector):
        collector.add_new_book('Турецкий гамбит')
        collector.set_book_genre('Турецкий гамбит', 'Детективы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_true(self, collector):
        collector.add_new_book('Турецкий гамбит')
        collector.set_book_genre('Турецкий гамбит', 'Детективы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert 'Турецкий гамбит' not in collector.get_books_for_children()

    def test_add_book_in_favorites_true(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_true(self, collector):
        collector.add_new_book('Турецкий гамбит')
        collector.add_new_book('Властелин колец')
        for book in collector.get_books_genre():
            collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites('Турецкий гамбит')
        assert 'Турецкий гамбит' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_true(self, collector):
        collector.add_new_book('Турецкий гамбит')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')
        for book in collector.get_books_genre():
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == ['Турецкий гамбит', 'Властелин колец', 'Гарри Поттер']