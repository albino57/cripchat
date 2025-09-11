/***↓ Global Variables ↓***/
const toggleButton = document.getElementById('toggle-sidebar-btn');
const container = document.querySelector('.container');
/***↑ Global Variables ↑***/

/***↓ Functions ↓***/
toggleButton.addEventListener('click', () => {
    container.classList.toggle('sidebar-collapsed'); // When clicked, toggle the 'sidebar-collapsed' class on the container
});
/***↑ Functions ↑***/