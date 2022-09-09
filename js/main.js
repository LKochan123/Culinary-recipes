document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link')
    const navList = document.querySelector('.navbar-collapse')

    navLinks.forEach(link => link.addEventListener('click', () => navList.classList.remove('show')))
})