const header = document.querySelector('header')
const sidebar = document.getElementById('sidebar')
const mainContent = document.querySelector('.main-content')
const toggleBtn = document.getElementById('toggleBtn')


toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed')
    mainContent.classList.toggle('expanded')
    header.classList.toggle('expanded')
})