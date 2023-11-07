document.querySelectorAll('.letter-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const letter = this.getAttribute('data-letter');
        fetch(`/ruta-a-tu-vista-de-filtrado?letter=${letter}`)
            .then(response => response.json())
            .then(data => updateBookList(data.books));
    });
});

function updateBookList(books) {
    const container = document.getElementById('books-list');
    container.innerHTML = '';
    books.forEach(book => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<a href="${book.url}">${book.title}</a>`;
        container.appendChild(listItem);
    });
}