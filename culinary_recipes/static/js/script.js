const nav = document.querySelector('.navbar')
const colorBtn = document.querySelector('nav .navbar-nav .color-btn')

let theme = localStorage.getItem('theme') || 'dark'
let root = document.documentElement

const addShadow = () => {
    window.scrollY > 1 ? nav.classList.add('shadow-bg') : nav.classList.remove('shadow-bg')
}

const darkTheme = () => {
    root.style.setProperty('--backgorund-color', 'black')
    root.style.setProperty('--text-color', 'white')
    colorBtn.innerHTML = '<i class="fa-regular fa-lightbulb"></i>'
    // theme = 'dark'
    // localStorage.setItem('theme', theme)
}

const lightTheme = () => {
    root.style.setProperty('--backgorund-color', '#F5F5F5')
    root.style.setProperty('--text-color', '#000000')
    colorBtn.innerHTML = '<i class="fa-regular fa-moon"></i>'
    // theme = 'light'
    // localStorage.setItem('theme', theme)
}

const checkColorMode = () => {
    !colorBtn.classList.contains('dark') ? darkTheme() : lightTheme()
    colorBtn.classList.toggle('dark')
}

colorBtn.addEventListener('click', checkColorMode)
window.addEventListener('scroll', addShadow)