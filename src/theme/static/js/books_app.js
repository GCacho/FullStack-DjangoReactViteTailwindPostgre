document.addEventListener("DOMContentLoaded", function () {
    const letterLinks = document.querySelectorAll('[data-letter]');
    const bookItems = document.querySelectorAll('.book-item');
    const searchInput = document.getElementById('searchInput');

    // Función para mostrar u ocultar libros basados en la letra seleccionada
    function filterBooks(letter) {
        bookItems.forEach(function (bookItem) {
            const titleLetter = bookItem.getAttribute('data-title-letter');
            if (titleLetter === letter.toLowerCase()) {
                bookItem.style.display = 'block';
            } else {
                bookItem.style.display = 'none';
            }
        });
    }

    // Función para filtrar libros basados en el texto de búsqueda
    function searchBooks(query) {
        bookItems.forEach(function (bookItem) {
            const title = bookItem.textContent.toLowerCase();
            if (title.includes(query.toLowerCase())) {
                bookItem.style.display = 'block';
            } else {
                bookItem.style.display = 'none';
            }
        });
    }

    // Agregar un controlador de eventos a cada enlace de letra
    letterLinks.forEach(function (letterLink) {
        letterLink.addEventListener("click", function (event) {
            event.preventDefault();
            const selectedLetter = letterLink.getAttribute('data-letter');
            filterBooks(selectedLetter);
        });
    });

    // Controlador de eventos para el campo de búsqueda
    searchInput.addEventListener('input', function () {
        const query = searchInput.value;
        if (query !== '') {
            searchBooks(query);
        } else {
            // Si no hay texto de búsqueda, mostrar todos los libros
            bookItems.forEach(function (bookItem) {
                bookItem.style.display = 'block';
            });
        }
    });
});