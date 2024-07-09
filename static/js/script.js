document.addEventListener('DOMContentLoaded', function () {
    const elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
    fetchBooks();
});

const bookTableBody = document.getElementById('book-table-body');
const modalElement = document.getElementById('modal1');
let modal;
if (modalElement) {
    modal = M.Modal.init(modalElement);
}
const bookForm = document.getElementById('book-form');
const saveBookBtn = document.getElementById('save-book-btn');
const cancelBookBtn = document.getElementById('cancel-book-btn');
let editMode = false;

const fetchBooks = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api/books');
        const books = response.data.data;
        bookTableBody.innerHTML = '';
        books.forEach(book => {
            const row = document.createElement('tr');
            row.innerHTML = `
        <td>${book.author}</td>
        <td>${book.title}</td>
        <td>${book.isbn}</td>
        <td>${book.pages}</td>
        <td>${book.published_date}</td>
        <td>
          <a href="#!" class="btn-small blue edit-btn" data-id="${book.id}">Edit</a>
          <a href="#!" class="btn-small red delete-btn" data-id="${book.id}">Delete</a>
        </td>
      `;
            bookTableBody.appendChild(row);
        });
    } catch (error) {
        console.error("Error fetching books:", error);
    }
};

document.addEventListener('click', async (e) => {
    if (e.target.classList.contains('edit-btn')) {
        const id = e.target.getAttribute('data-id');
        editMode = true;
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/books/${id}`);
            const book = response.data.data;
            if (book) {
                document.getElementById('author').value = book.author || '';
                document.getElementById('title').value = book.title || '';
                document.getElementById('isbn').value = book.isbn || '';
                document.getElementById('pages').value = book.pages || '';
                document.getElementById('published_date').value = book.published_date || '';
                document.getElementById('book-id').value = book.id || '';
                M.updateTextFields();
                modal.open();
            } else {
                console.error("Book data is undefined");
            }
        } catch (error) {
            console.error("Error fetching book data:", error);
        }
    }
    if (e.target.classList.contains('modal-trigger')){
        modal.open();
        editMode = false;
    }

    if (e.target.classList.contains('delete-btn')) {
        const id = e.target.getAttribute('data-id');
        try {
            await axios.delete(`http://127.0.0.1:5000/api/books/${id}`);
            fetchBooks();
        } catch (error) {
            console.error("Error deleting book:", error);
        }
    }
});
cancelBookBtn.addEventListener('click', () => {
    const modalOverlay = document.querySelector('.modal-overlay');
    if (modalOverlay) {
        modalOverlay.attributes[1].nodeValue = "";
    }
    modal.close();
    bookForm.reset();
    editMode = false;
})
saveBookBtn.addEventListener('click', async () => {
    const formData = new FormData(bookForm);
    const book = {
        author: formData.get('author').trim(),
        title: formData.get('title').trim(),
        isbn: formData.get('isbn').trim(),
        pages: parseInt(formData.get('pages'), 10),
        published_date: formData.get('published_date')
    };

    if (!validateBook(book)) {
        return;
    }

    try {
        if (editMode) {
            const id = formData.get('id');
            await axios.put(`http://127.0.0.1:5000/api/books/${id}`, book);
        } else {
            await axios.post('http://127.0.0.1:5000/api/books', book);
        }
        fetchBooks();
        modal.close();
        bookForm.reset();
        editMode = false;
    } catch (error) {
        console.error("Error saving book:", error);
    }
});


function validateBook(book) {
    const today = new Date().toISOString().split('T')[0];
    if (book.author === '' || book.title === '') {
        alert('Author and Title cannot be empty');
        return false;
    }
    if (book.published_date > today) {
        alert('Published Date cannot be in the future');
        return false;
    }
    if (isNaN(book.pages) || book.pages < 1) {
        alert('Pages must be a number greater than 0');
        return false;
    }
    if (!validateISBN(book.isbn)) {
        alert('Invalid ISBN');
        return false;
    }
    return true;
}

function validateISBN(isbn) {
    const isbn10Pattern = /^[0-9]{9}[\dX]$/;
    return isbn10Pattern.test(isbn);
}